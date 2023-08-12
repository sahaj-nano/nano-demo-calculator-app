from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    # return "Hey! Sahaj, I'm Dhananjay Kisan Jadhav, from PCE Panvel."
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    num1 = request.json.get('first')
    num2 = request.json.get('second')
    result = num1 + num2
    # return f'{num1} + {num2} = {result}'
    return f'result:{result}'

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num1 = request.json.get('first')
    num2 = request.json.get('second')
    result = num1 - num2
    # return f'{num1} - {num2} = {result}'
    return f'result: {result}'

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
