#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(f'{string}')
    return string

@app.route('/count/<number>')
def count(number):
    list_of_num = ''
    for i in range(int(number)):
        list_of_num = list_of_num + str(i) +'\n'

    return list_of_num

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    print (type(num1))
    print(type(operation))
    print(type(num2))
    if operation == '+':
        value = int(num1) + int(num2)
        return str(value)
    elif operation == '-':
        value = int(num1) - int(num2)
        return str(value)
    elif operation == '*':
        value = int(num1) * int(num2)
        return str(value)
    elif operation == 'div':
        value = int(num1) / int(num2)
        return str(value)
    elif operation == '%':
        value = int(num1) % int(num2)
        return str(value)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
