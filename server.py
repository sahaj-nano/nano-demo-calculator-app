from flask import Flask, request, jsonify

app = Flask(_name_)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    first_number = data.get('first', 0)
    second_number = data.get('second', 0)
    result = first_number + second_number
    response = {'result': result}
    return jsonify(response), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    first_number = data.get('first', 0)
    second_number = data.get('second', 0)
    result = first_number - second_number
    response = {'result': result}
    return jsonify(response), 200

if _name_ == '_main_':
    app.run(port=8080,host='0.0.0.0')
