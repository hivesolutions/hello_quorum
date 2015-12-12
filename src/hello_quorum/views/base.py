#!/usr/bin/python
# -*- coding: utf-8 -*-

from hello_quorum.main import app
from hello_quorum.main import flask

@app.route("/", methods = ("GET",), json = True)
@app.route("/index", methods = ("GET",), json = True)
def index():
    return flask.redirect(
        flask.url_for("headers")
    )

@app.route("/headers", methods = ("GET",), json = True)
def headers():
    return dict(flask.request.headers)