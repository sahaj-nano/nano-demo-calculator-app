from flask import Flask, request

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return '<p style="color:red">hehe</p>'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('first')
    num2 = data.get('second')
    result = num1 + num2
    return str(result)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data.get('first')
    num2 = data.get('second')
    result = num1 - num2
    return str(result)

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
