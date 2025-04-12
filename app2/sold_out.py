from flask import Flask

app = Flask(__name__)

@app.route('/')
def sold_out_products():
    return """
    <h1>Sold Out Products</h1>
    <ul>
        <li>Product A - Sold Out</li>
        <li>Product B - Sold Out</li>
        <li>Product C - Sold Out</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
