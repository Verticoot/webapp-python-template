from flask import Flask, Response
import json

from listamusica import songlist


app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/jquery-3.4.1.min.js')
def js():
    return app.send_static_file('jquery-3.4.1.min.js')

@app.route("/data")
def data():
    json_string = json.dumps([x for x in songlist])
    return Response(json_string.__dict__, mimetype='application/json')