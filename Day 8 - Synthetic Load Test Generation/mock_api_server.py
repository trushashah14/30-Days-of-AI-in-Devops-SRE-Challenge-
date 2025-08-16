from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/resource', methods=['GET', 'POST'])
def resource():
    return jsonify({"message": "Resource endpoint reached"}), 200

@app.route('/api/v1/item', methods=['GET', 'POST'])
def item():
    return jsonify({"message": "Item endpoint reached"}), 200

@app.route('/api/v1/user', methods=['GET', 'POST'])
def user():
    return jsonify({"message": "User endpoint reached"}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=80)
