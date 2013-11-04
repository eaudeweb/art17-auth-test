#!/usr/bin/env python

import flask
from path import path

app = flask.Flask(__name__)
app.config.from_pyfile(path(__file__).abspath().parent / 'settings.py')


@app.route('/')
def home():
    return 'hi'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
