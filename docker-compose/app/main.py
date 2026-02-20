from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return jsonify({
        "message": "Hello from Secure AI Platform!",
        "visits": int(count)
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
