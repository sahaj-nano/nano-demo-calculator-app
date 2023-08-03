from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    json_data = request.get_json()
    first_number = json_data['first']
    second_number = json_data['second']
    sum = first_number + second_number
    return jsonify(result=sum), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    json_data = request.get_json()
    first_number = json_data['first']
    second_number = json_data['second']
    sub = first_number - second_number
    return jsonify(result=sub), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
