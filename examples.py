#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
# import json
from bottle import Bottle, route, run, template, redirect 
from bottle import error, static_file
from bottle import get, post, request

from tools import *

# config launch.json : https://github.com/DonJayamanne/pythonVSCode/wiki/Debugging

app = Bottle()
root = os.getcwd()

@app.error(404)
def error404(error):
    """
    default message for error 404
    """
    return 'Nothing here, sorry'

@app.route('/')
@app.route('/hello')
def index():
    """
    default route
    """
    return "Hello World!"
    # redirect("/login")

@app.route('/hello/<name>')
@app.route('/hello2/<name>')
def hello(name):
    """
    hello{name} route
    """
    return template('<b>Hello {{name}}</b>!', name=name)

@app.get('/login') # or @route('/login')
def login():
    """
    ???
    """
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.post('/login') # or @route('/login', method='POST')
def do_login():
    """
    ???
    """
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        # return "<p>Your login information was correct.</p>"
        redirect("/hello")
    else:
        return "<p>Login failed.</p>"

@app.route('/static/<path:path>')
def static(path):
    """
    load html file example 
    """
    return static_file(filename=path, root=root)

run(app, host='localhost', port=8080, debug=True, reloader=True)


"""
@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)

@route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()
"""
