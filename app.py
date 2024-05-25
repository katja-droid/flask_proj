from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Sample data for products
products = [
    {"id": 1, "name": "Product 1", "price": 10},
    {"id": 2, "name": "Product 2", "price": 20},
    {"id": 3, "name": "Product 3", "price": 30},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
