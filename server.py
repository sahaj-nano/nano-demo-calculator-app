from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.get_json()
        first = data["first"]
        second = data["second"]
        result = first + second
        return jsonify({"result": result}), 200
    except KeyError:
        return "Invalid request data", 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        first = data["first"]
        second = data["second"]
        result = first - second
        return jsonify({"result": result}), 200
    except KeyError:
        return "Invalid request data", 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
