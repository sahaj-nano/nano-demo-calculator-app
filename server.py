from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.get_json()
    f= numbers["first"]
    s= numbers["second"]
    res= f+s
    return jsonify({"result": res}), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    numbers = request.get_json()
    f= numbers["first"]
    s= numbers["second"]
    res= f-s
    return jsonify({"result": res}), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
