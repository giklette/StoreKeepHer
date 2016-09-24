#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
# import json
from bottle import Bottle
from bottle import route, view, run, template, redirect 
from bottle import error, static_file
from bottle import get, post, request

from tools import check_login
from database import DataBase

# config launch.json : 
# https://github.com/DonJayamanne/pythonVSCode/wiki/Debugging

app = Bottle()
root = os.getcwd()

db = DataBase()
db.create_table()

@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

@app.route('/')
def index():
    redirect('/login')

@app.route('/about')
def about():
    args = { 'title': 'StoreKeepHer' }
    return template('templates/about', args)

@app.get('/login') # or @route('/login')
@view('templates/login')
def login_get():
    key = db.get_session()
    print key
    args = { 'title': 'StoreKeepHer' }
    # return template('templates/login', args)  
    # or add the decorator @view('template to use')
    return args

@app.post('/login') # or @route('/login', method='POST')
def login_post():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        redirect("/list")
    else:
        return "<p>Login failed.</p>"

@app.route('/list')
@view('templates/list')
def view_list():
    args = { 
        'title': 'StoreKeepHer',
        'values': 'bla bla bla'
    }
    return args

@app.route('/product/<product_id:int>')
def product(product_id):
    args = { 
        'product': product_id,
        'values': 'bla bla bla'
     }
    return template('this is the product sheet {{product}}', args)

@app.route('/static/<filename:path>')
def static(filename):
    static_path = os.path.join(root, 'static')
    file_path = os.path.join(static_path, filename)
    return static_file(filename=file_path, root=root)

run(app, host='localhost', port=8080, debug=True, reloader=True)

'''
if __name__ == "__main__":
    db = COMP249Db()
    create_table(db)
'''
