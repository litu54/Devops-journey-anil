from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Simple Calculator!'

@app.route('/add', methods=['GET', 'POST'])
def add():
    num1, num2 = get_numbers()
    return {'result': float(num1) + float(num2)}

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    num1, num2 = get_numbers()
    return {'result': float(num1) - float(num2)}

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    num1, num2 = get_numbers()
    return {'result': float(num1) * float(num2)}

@app.route('/divide', methods=['GET', 'POST'])
def divide():
    num1, num2 = get_numbers()
    if float(num2) == 0:
        return {'error': 'Division by zero not allowed'}
    return {'result': float(num1) / float(num2)}

def get_numbers():
    if request.method == 'POST':
        data = request.get_json()
        return data['num1'], data['num2']
    else:
        return request.args.get('num1'), request.args.get('num2')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

