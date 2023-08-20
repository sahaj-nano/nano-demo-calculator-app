from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    if 'first' in data and 'second' in data:
        result = data['first'] + data['second']
        return jsonify({'result':result}),200
    else:
        return jsonify({'error':'Invalid input'}),400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    if 'first' in data and 'second' in data:
        result = data['first'] - data['second']
        return jsonify({'result':result}),200
    else:
        return jsonify({'error':'Invalid input'}),400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
