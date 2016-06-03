#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask.ext.cors import CORS
from models import *

app = Flask(__name__)
CORS(app)

@app.route('/foosball', methods=['GET','POST'])
def foosball():
    if request.method == 'GET':
        return jsonify({'status':'ok'})

if __name__ == '__main__':
    app.run()