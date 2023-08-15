from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the Calculator API!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if 'numbers' in data and isinstance(data['numbers'], list):
        result = sum(data['numbers'])
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if 'numbers' in data and isinstance(data['numbers'], list):
        if len(data['numbers']) >= 2:
            result = data['numbers'][0]
            for num in data['numbers'][1:]:
                result -= num
            return jsonify({"result": result})
        else:
            return jsonify({"error": "At least two numbers required"}), 400
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
