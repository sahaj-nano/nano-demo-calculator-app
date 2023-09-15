import flask from Flask
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return ''
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    return ''
    numbers = request.get_json()
    a= numbers["first"]
    b= numbers["second"]
    ans= f+s
    return jsonify({"result": ans}), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''
    numbers = request.get_json()
    a= numbers["first"]
    b= numbers["second"]
    ans= a-b
    return jsonify({"result": ans}), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
Footer
