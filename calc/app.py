# Put your app in here.

from unittest import result
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def to_add():
    ''' Add a and b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(add(a, b))

@app.route('/sub')
def to_sub():
    ''' Subract a and b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(sub(a, b))

@app.route('/mult')
def to_mult():
    ''' Multiply a and b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(mult(a, b))

@app.route('/div')
def to_div():
    ''' Divide a and b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(div(a, b))

""" Simplier Version """

operators = {
    'add' : add,
    'sub' : sub,
    'mult' : mult,
    'div' : div,
}

@app.route('/math/<oper>')
def do_math(oper):
    ''' Do math on a and b'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))   

    result = operators[oper](a, b) 

    return str(result)