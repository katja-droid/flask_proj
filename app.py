import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Sample data for products
products = [
    {"id": 1, "name": "Product 1", "price": 10},
    {"id": 2, "name": "Product 2", "price": 20},
    {"id": 3, "name": "Product 3", "price": 30},
]

# Initialize an empty cart
cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = int(request.form['product_id'])
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    total_price = sum(product['price'] for product in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    global cart
    cart = [product for product in cart if product['id'] != product_id]
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
