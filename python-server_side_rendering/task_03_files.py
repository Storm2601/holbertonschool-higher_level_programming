from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_file(file_path, file_type):
    if file_type == 'json':
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_type == 'csv':
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    products = read_file(f'products.{source}', source)

    if product_id:
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
