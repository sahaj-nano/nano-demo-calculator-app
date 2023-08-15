from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if "first" in data and "second" in data:
        try:
            first = float(data["first"])
            second = float(data["second"])
            result = first + second
            return jsonify({"result": result}), 200
        except ValueError:
            return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400
    else:
        return jsonify({"error": "Missing 'first' or 'second' parameter in request body."}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if "first" in data and "second" in data:
        try:
            first = float(data["first"])
            second = float(data["second"])
            result = first - second
            return jsonify({"result": result}), 200
        except ValueError:
            return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400
    else:
        return jsonify({"error": "Missing 'first' or 'second' parameter in request body."}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')