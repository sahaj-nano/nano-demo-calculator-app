from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    f= numbers['first']
    s= numbers['second']
    res= f+s
    return jsonify(res)
@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.json
    f= numbers['first']
    s= numbers['second']
    res= f-s
    return jsonify(res)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
