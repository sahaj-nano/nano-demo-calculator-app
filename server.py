from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()  # Get JSON data from the request
    first = data.get('first', 0)
    second = data.get('second', 0)
    result = first + second
    response = {'result': result}
    return jsonify(response), 200  # Return JSON response with result and status code 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()  # Get JSON data from the request
    first = data.get('first', 0)
    second = data.get('second', 0)
    result = first - second
    response = {'result': result}
    return jsonify(response), 200  # Return JSON response with result and status code 200

if _name_ == '_main_':
    app.run(port=8080, host='0.0.0.0')