from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the Calculator API!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if "num1" in data and "num2" in data:
        num1 = data["num1"]
        num2 = data["num2"]
        result = num1 + num2
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Missing 'num1' or 'num2' in request data"}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if "num1" in data and "num2" in data:
        num1 = data["num1"]
        num2 = data["num2"]
        result = num1 - num2
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Missing 'num1' or 'num2' in request data"}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
