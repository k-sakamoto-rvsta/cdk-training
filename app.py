#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from Flask!!' 
@app.route("/get/host", methods=["GET"])
def get_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
