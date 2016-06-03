#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, abort
from flask.ext.cors import CORS
from models import *

app = Flask(__name__)
CORS(app)

@app.route('/getplayers', methods=['GET'])
def getplayers():
    if request.method == 'GET':
        result = {'data':[]}
        rs = Player.select().dicts()
        for row in rs:
            result['data'].append(row)
        return jsonify(result)

@app.route('/addpoints', methods=['POST'])
def addpoints():
    if request.method == 'POST':
        payload = request.get_json(force=True)
        pid = payload['pid']
        points = payload['points']
        try:
            rs = Player.select().where(Player.id == pid).get()
            val = int(points)
        except:
            abort(404)
        rs.points += val
        rs.save()
        return jsonify({'update':'pid:%d, points:%d' % (pid, points)})


if __name__ == '__main__':
    app.run()