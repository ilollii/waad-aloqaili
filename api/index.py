from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class handler(BaseHTTPRequestHandler):
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

        if '/admin/stats' in path:
            return self._send_json({
                'success': True,
                'stats': {
                    'total_sales_sar': 43550.0,
                    'total_orders': 2,
                    'pending_orders': 1,
                    'total_fittings': 1,
                    'avg_order_value_sar': 21775.0
                }
            })
        elif '/admin/orders' in path:
            return self._send_json({
                'success': True,
                'orders': [
                    {
                        'id': 1,
                        'order_number': 'WA-2026-8891',
                        'customer_name': 'الأميرة نورة آل سعود',
                        'customer_phone': '+966501234567',
                        'city': 'الرياض',
                        'payment_method': 'applepay',
                        'payment_status': 'paid',
                        'total_amount': 28600.0,
                        'order_status': 'completed',
                        'created_at': '2026-08-25',
                        'items': [{'title': 'AURORA GOWN', 'size': '38 EU', 'quantity': 2}]
                    }
                ]
            })
        elif '/admin/appointments' in path:
            return self._send_json({
                'success': True,
                'appointments': [
                    {
                        'appointment_code': 'FIT-2026-104',
                        'client_name': 'سارة العتيبي',
                        'client_phone': '+966555112233',
                        'branch': 'riyadh',
                        'service_type': 'جلسة قياس فستان زفاف ملكي',
                        'appointment_date': '2026-08-28',
                        'time_slot': '05:00 PM',
                        'status': 'confirmed'
                    }
                ]
            })
        elif '/config' in path:
            try:
                cfg_path = os.path.join(BASE_DIR, 'config.json')
                with open(cfg_path, 'r', encoding='utf-8') as f:
                    cfg = json.load(f)
                return self._send_json({'success': True, 'config': cfg})
            except Exception as e:
                return self._send_json({'success': False, 'error': str(e)}, 500)

        return self._send_json({'success': True, 'message': 'Waad Aloqaili API Serverless Engine'})

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('Content-Length', 0))
        raw_body = self.rfile.read(length).decode('utf-8') if length > 0 else '{}'
        try:
            payload = json.loads(raw_body)
        except Exception:
            payload = {}

        if '/orders/create' in path:
            order_num = 'WA-2026-' + str(random.randint(1000, 9999))
            total = float(payload.get('total_amount', 14950))
            return self._send_json({'success': True, 'order_number': order_num, 'total_amount': total})

        elif '/appointments/book' in path:
            appt_code = 'FIT-2026-' + str(random.randint(100, 999))
            return self._send_json({'success': True, 'appointment_code': appt_code, 'message': 'Confirmed'})

        return self._send_json({'success': True, 'message': 'Processed'})
