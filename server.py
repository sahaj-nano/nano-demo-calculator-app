from flask import Flask,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    first = data['first']
    dusra = data['second']
    return { "result": first+dusra}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    first = data['first']
    second = data['second']
    return { "result": first-second}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
