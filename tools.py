# -*- coding: utf-8 -*-

# cookies management
# http://pwp.stevecassidy.net/bottle/cookies.html

from bottle import request, response

'''
def check_login():
    """
    ???
    """
    visits = request.get_cookie('visited')
    # response.set_cookie('test', 'hello')
'''

def check_login(username, password):
    """
    check the matching user name / password
    """
    return True
