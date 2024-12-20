from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.json
    return jsonify({"message": "Order placed", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
