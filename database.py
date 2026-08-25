import sqlite3
import json
import os
import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), 'boutique.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # 1. Orders Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_number TEXT UNIQUE NOT NULL,
        customer_name TEXT NOT NULL,
        customer_phone TEXT NOT NULL,
        customer_email TEXT NOT NULL,
        country TEXT NOT NULL,
        city TEXT NOT NULL,
        address TEXT NOT NULL,
        notes TEXT,
        payment_method TEXT NOT NULL,
        payment_status TEXT DEFAULT 'pending',
        transaction_id TEXT,
        subtotal REAL NOT NULL,
        discount REAL DEFAULT 0,
        total_amount REAL NOT NULL,
        currency TEXT DEFAULT 'SAR',
        order_status TEXT DEFAULT 'processing',
        tracking_number TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 2. Order Items Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id TEXT NOT NULL,
        title TEXT NOT NULL,
        size TEXT,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        image_url TEXT,
        FOREIGN KEY (order_id) REFERENCES orders(id)
    )
    ''')

    # 3. Appointments Table (Atelier Fittings)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_code TEXT UNIQUE NOT NULL,
        client_name TEXT NOT NULL,
        client_phone TEXT NOT NULL,
        branch TEXT NOT NULL,
        service_type TEXT NOT NULL,
        appointment_date TEXT NOT NULL,
        time_slot TEXT NOT NULL,
        status TEXT DEFAULT 'confirmed',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 4. Settings / Logs Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        log_type TEXT NOT NULL,
        payload TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Seed sample orders if empty
    cursor.execute('SELECT COUNT(*) FROM orders')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
        INSERT INTO orders (order_number, customer_name, customer_phone, customer_email, country, city, address, notes, payment_method, payment_status, total_amount, subtotal, order_status)
        VALUES ('WA-2026-8891', 'الأميرة نورة آل سعود', '+966501234567', 'noura@royal.sa', 'SA', 'الرياض', 'حي السفارات، الرياض', 'تعديل طول الذيل 5 سم', 'applepay', 'paid', 28600.0, 28600.0, 'completed')
        ''')
        order_id = cursor.lastrowid
        cursor.execute('''
        INSERT INTO order_items (order_id, product_id, title, size, price, quantity, image_url)
        VALUES (?, '8545370734777', 'AURORA GOWN', '38 EU', 14300.0, 2, 'https://cdn.shopify.com/s/files/1/0609/7181/1001/files/038A6BF2-CF4C-45F4-8747-76F0DEE93B2D.jpg?width=1800')
        ''', (order_id,))

        cursor.execute('''
        INSERT INTO appointments (appointment_code, client_name, client_phone, branch, service_type, appointment_date, time_slot, status)
        VALUES ('FIT-2026-104', 'سارة العتيبي', '+966555112233', 'riyadh', 'جلسة قياس فستان زفاف ملكي', '2026-08-28', '05:00 PM', 'confirmed')
        ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully at:", DB_PATH)

if __name__ == '__main__':
    init_db()
