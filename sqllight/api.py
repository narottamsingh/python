#!/usr/bin/env python
from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'name': 'Narottam Singh',
                    'email': 'n.kumar9@yahoo.com'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)