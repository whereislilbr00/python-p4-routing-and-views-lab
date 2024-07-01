# server/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text  # Return plain text
def test_print_text(client):
    """Displays text of route in browser."""
    response = client.get('/print/hello')
    assert response.data.decode() == 'hello'

@app.route('/count/<int:number>')
def count(number):
    numbers = '\n'.join(str(i) for i in range(number))
    return numbers + '\n'  # Add newline at the end
def test_count_range_10(client):
    """Counts through range of parameter in "/count/<parameter>" on separate lines."""
    response = client.get('/count/10')
    count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9'  # Adjusted expected output
    assert response.data.decode() == count

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Division by zero error!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation!'
    
    return f'Result: {result}'

if __name__ == '__main__':
    app.run(port=5555)
def test_math_route(client):
    """Has a resource available at '/math/<parameters>'."""
    response = client.get('/math/5/+/5')
    assert response.status_code == 200
