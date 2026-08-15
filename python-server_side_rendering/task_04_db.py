from flask import Flask, render_template, request
import os
import json
import csv
import sqlite3

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'products.db')


def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()


def read_json(id=None):
    json_path = os.path.join(os.path.dirname(__file__), 'products.json')
    with open(json_path, 'r') as f:
        products = json.load(f)

    if id is not None:
        for product in products:
            if product['id'] == id:
                return [product]
        return None

    return products


def read_csv(id=None):
    csv_path = os.path.join(os.path.dirname(__file__), 'products.csv')
    with open(csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        products = []
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })

    if id is not None:
        for product in products:
            if product['id'] == id:
                return [product]
        return None

    return products


def read_sql(id=None):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if id is not None:
        cursor.execute('SELECT * FROM Products WHERE id = ?', (id,))
        rows = cursor.fetchall()
    else:
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()

    conn.close()

    products = [dict(row) for row in rows]

    if id is not None:
        return products if products else None

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error='Wrong source')

    id = None
    if id_param is not None:
        try:
            id = int(id_param)
        except ValueError:
            return render_template('product_display.html', error='Invalid product ID')

    try:
        if source == 'json':
            result = read_json(id)
        elif source == 'csv':
            result = read_csv(id)
        else:
            result = read_sql(id)
    except sqlite3.Error:
        return render_template('product_display.html', error='Database error')

    if result is None:
        return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=result)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
