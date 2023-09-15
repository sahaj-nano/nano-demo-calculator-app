from flask import Flask
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return ''
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    return ''
    numbers= request.json
    response= numbers['first']+ numbers['second']
    return jsonify({'result':response})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''
    numbers= request.json
    response= numbers['first']- numbers['second']
    return jsonify({'result':response})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')