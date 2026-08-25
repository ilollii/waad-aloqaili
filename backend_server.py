import http.server
import json
import urllib.parse
import os
import random
from database import get_db, init_db

PORT = 8088
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

init_db()

class BoutiqueHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == '/api/admin/stats':
            try:
                conn = get_db()
                cursor = conn.cursor()
                cursor.execute('SELECT COUNT(*), COALESCE(SUM(total_amount), 0) FROM orders')
                orders_count, total_sales = cursor.fetchone()
                cursor.execute('SELECT COUNT(*) FROM appointments')
                appointments_count = cursor.fetchone()[0]
                cursor.execute('SELECT COUNT(*) FROM orders WHERE order_status = "processing"')
                pending_orders = cursor.fetchone()[0]
                conn.close()

                return self._send_json({
                    'success': True,
                    'stats': {
                        'total_sales_sar': total_sales,
                        'total_orders': orders_count,
                        'pending_orders': pending_orders,
                        'total_fittings': appointments_count,
                        'avg_order_value_sar': round(total_sales / orders_count, 2) if orders_count > 0 else 0
                    }
                })
            except Exception as e:
                return self._send_json({'success': False, 'error': str(e)}, 500)

        elif path == '/api/admin/orders':
            try:
                conn = get_db()
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM orders ORDER BY id DESC')
                orders = [dict(r) for r in cursor.fetchall()]
                conn.close()
                return self._send_json({'success': True, 'orders': orders})
            except Exception as e:
                return self._send_json({'success': False, 'error': str(e)}, 500)

        elif path == '/api/admin/appointments':
            try:
                conn = get_db()
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM appointments ORDER BY id DESC')
                appts = [dict(r) for r in cursor.fetchall()]
                conn.close()
                return self._send_json({'success': True, 'appointments': appts})
            except Exception as e:
                return self._send_json({'success': False, 'error': str(e)}, 500)

        elif path == '/api/config':
            try:
                with open(os.path.join(BASE_DIR, 'config.json'), 'r', encoding='utf-8') as f:
                    cfg = json.load(f)
                return self._send_json({'success': True, 'config': cfg})
            except Exception as e:
                return self._send_json({'success': False, 'error': str(e)}, 500)

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('Content-Length', 0))
        raw_body = self.rfile.read(length).decode('utf-8') if length > 0 else '{}'
        try:
            payload = json.loads(raw_body)
        except Exception:
            payload = {}

        if path == '/api/orders/create':
            try:
                conn = get_db()
                cursor = conn.cursor()
                order_num = 'WA-2026-' + str(random.randint(1000, 9999))
                customer = payload.get('customer', {})
                total = float(payload.get('total_amount', 14950))
                cursor.execute('''
                INSERT INTO orders (order_number, customer_name, customer_phone, customer_email, country, city, address, notes, payment_method, payment_status, subtotal, total_amount, order_status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'processing')
                ''', (
                    order_num,
                    customer.get('name', 'VIP Client'),
                    customer.get('phone', ''),
                    customer.get('email', ''),
                    customer.get('country', 'SA'),
                    customer.get('city', 'Riyadh'),
                    customer.get('address', ''),
                    customer.get('notes', ''),
                    payload.get('payment_method', 'mada'),
                    'paid',
                    total,
                    total
                ))
                conn.commit()
                conn.close()
                return self._send_json({'success': True, 'order_number': order_num, 'total_amount': total})
            except Exception as e:
                return self._send_json({'success': False, 'error': str(e)}, 500)

        elif path == '/api/admin/orders/update':
            try:
                conn = get_db()
                cursor = conn.cursor()
                cursor.execute('UPDATE orders SET order_status = ?, tracking_number = ? WHERE id = ?', 
                               (payload.get('status'), payload.get('tracking_number', ''), payload.get('order_id')))
                conn.commit()
                conn.close()
                return self._send_json({'success': True, 'message': 'Updated'})
            except Exception as e:
                return self._send_json({'success': False, 'error': str(e)}, 500)

        elif path == '/api/config/save':
            try:
                with open(os.path.join(BASE_DIR, 'config.json'), 'w', encoding='utf-8') as f:
                    json.dump(payload, f, ensure_ascii=False, indent=2)
                return self._send_json({'success': True, 'message': 'Saved'})
            except Exception as e:
                return self._send_json({'success': False, 'error': str(e)}, 500)

        return self._send_json({'error': 'Not found'}, 404)

if __name__ == '__main__':
    http.server.test(HandlerClass=BoutiqueHandler, port=PORT)
