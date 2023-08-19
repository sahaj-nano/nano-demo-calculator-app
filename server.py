from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World'

@app.route("/calculator/add", methods=['POST'])
def add():
    body = request.json
    response = int(body['first'])+int(body['second'])
    return jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    body = request.json
    response = int(body['first'])-int(body['second'])
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
