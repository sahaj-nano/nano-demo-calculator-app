from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers= request.json
    response= numbers['first']+ numbers['second']
    return jsonify({'result':response})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers= request.json
    response= numbers['first']- numbers['second']
    return jsonify({'result':response})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
