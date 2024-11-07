from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_file(file_path, file_type):
    if file_type == 'json':
        with open(file_path, 'r') as file:
            return json.load(file)
    if file_type == 'csv':
        with open(file_path, 'r') as file:
            return [row for row in csv.DictReader(file)]
    if file_type == 'sql':
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in cursor.fetchall()]
        conn.close()
        return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    try:
        products = read_file(f'products.{source}', source)
    except Exception as e:
        return render_template('product_display.html', error=str(e))

    if product_id:
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
