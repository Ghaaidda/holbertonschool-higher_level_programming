from flask import Flask, render_template, request
import os
import json
import csv

app = Flask(__name__)


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


@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template('product_display.html', error='Wrong source')

    id = None
    if id_param is not None:
        try:
            id = int(id_param)
        except ValueError:
            return render_template('product_display.html', error='Invalid product ID')

    if source == 'json':
        result = read_json(id)
    else:
        result = read_csv(id)

    if result is None:
        return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
