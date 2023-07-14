from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return 'Hello world!', 200

@app.route('/calculator/add', methods=['POST'])
def add():
    data = request.get_json()
    first = data['first']
    second = data['second']
    result = first + second
    return jsonify({'result': result}), 200

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    first = data['first']
    second = data['second']
    result = first - second
    return jsonify({'result': result}), 200

if _name_ == '_main_':
    app.run()