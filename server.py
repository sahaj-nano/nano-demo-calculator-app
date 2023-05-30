from flask import Flask, request

app = Flask(__name__)

def makeJson(num):
    return {'result': num}


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    return makeJson(request.json['first'] + request.json['second'])

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return makeJson(request.json['first'] - request.json['second'])


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
