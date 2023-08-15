from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    first = data.get('first')
    second = data.get('second')
    
    result = first + second
    response_data = {'result': result}
    return jsonify(response_data), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    first = data.get('first')
    second = data.get('second')

    result = first - second
    response_data = {'result':result}
    return jsonify(response_data),200


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
