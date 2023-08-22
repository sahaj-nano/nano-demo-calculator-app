from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    first = data['first']
    second = data['second']
    result = first + second 
    ans = {'result': result}
    return jsonify(ans), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    first = data['first']
    second = data['second']
    result = first - second 
    ans = {'result': result}
    return jsonify(ans), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')