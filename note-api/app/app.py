from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest
import time

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency')

notes = []

@app.route('/notes', methods=['GET'])
def get_notes():
    REQUEST_COUNT.labels(method='GET', endpoint='/notes').inc()
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    REQUEST_COUNT.labels(method='POST', endpoint='/notes').inc()
    data = request.json
    notes.append(data)
    return jsonify(data), 201

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)