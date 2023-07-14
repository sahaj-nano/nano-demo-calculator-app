from flask import Flask, request, jsonify, render_template, request

app = Flask(__name__)
@app.route("/")
def calculator():
    return render_template("index.html")
@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    num1 = data['first']
    num2 = data['second']
    result = num1 + num2
    return {'result': result}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['first']
    num2 = data['second']
    result = num1 - num2
    return {'result': result}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
