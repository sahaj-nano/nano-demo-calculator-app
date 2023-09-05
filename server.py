from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    num = request.json
    first = num['first']
    second = num['second'] 
    return jsonify({'result': first+second}), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num = request.json
    first = num['first']
    second = num['second'] 
    return jsonify({'result': first-second}), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
