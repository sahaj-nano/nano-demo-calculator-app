from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    req = request.get_json()
    data1 = req['first']
    data2 = req['second']
    result = data1 + data2
    return jsonify({'result': result})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    req = request.get_json()
    data1 = req['first']
    data2 = req['second']
    result = data1 - data2
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')