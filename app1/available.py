from flask import Flask

app = Flask(__name__)

@app.route('/')
def available_products():
    return """
    <h1>Available Products</h1>
    <ul>
        <li>Product 1 - $10</li>
        <li>Product 2 - $20</li>
        <li>Product 3 - $30</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
