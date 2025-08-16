from flask import Flask, request, jsonify
import math
import sympy as sp
import numpy as np

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data['operation']
    expression = data.get('expression', '')
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    
    try:
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            result = a / b
        elif operation == 'power':
            result = a ** b
        elif operation == 'sqrt':
            result = math.sqrt(a)
        elif operation == 'sin':
            result = math.sin(a)
        elif operation == 'cos':
            result = math.cos(a)
        elif operation == 'tan':
            result = math.tan(a)
        elif operation == 'log':
            result = math.log(a)
        elif operation == 'integral':
            x = sp.symbols('x')
            expr = sp.sympify(expression)
            result = str(sp.integrate(expr, (x, a, b)))
        elif operation == 'derivative':
            x = sp.symbols('x')
            expr = sp.sympify(expression)
            result = str(sp.diff(expr, x))
        elif operation == 'limit':
            x = sp.symbols('x')
            expr = sp.sympify(expression)
            result = str(sp.limit(expr, x, a))
        elif operation == 'solve':
            x = sp.symbols('x')
            expr = sp.sympify(expression)
            result = str(sp.solve(expr, x))
        else:
            result = "Geçersiz işlem"
        
        return jsonify({'result': str(result), 'error': None})
    except Exception as e:
        return jsonify({'result': None, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)