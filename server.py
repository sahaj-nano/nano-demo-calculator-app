from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.json
        if "first" in data and "second" in data:
            first = data["first"]
            second = data["second"]
            result = first + second
            return jsonify({"result": result})
        else:
            return jsonify({"error": "Missing 'first' or 'second' parameter"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.json
        if "first" in data and "second" in data:
            first = data["first"]
            second = data["second"]
            result = first - second
            return jsonify({"result": result})
        else:
            return jsonify({"error": "Missing 'first' or 'second' parameter"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
