#!/usr/bin/env python

import flask
from path import path
import requests

app = flask.Flask(__name__)
app.config.from_pyfile(path(__file__).abspath().parent / 'settings.py')


@app.route('/')
def home():
    url = app.config['ART17_AUTH_SERVICE']
    resp = requests.post(url)
    return flask.Response(resp.text, content_type='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
