from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/error_rate')
def error_rate():
    # Simulate a dynamic error rate (could be random or fixed)
    return jsonify(error_rate=0.7)

@app.route('/latency')
def latency():
    # Simulate a latency metric (ms)
    return jsonify(latency=120)

@app.route('/health')
def health():
    # Simulate health status
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(port=5000)
