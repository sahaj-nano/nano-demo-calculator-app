from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    r=[]
    n1=request.json['first']
    n2=request.json['second']
    r.append(n1+n2)
    return jsonify(r)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    result=[]
    n1=request.json['first']
    n2=request.json['second']
    result.append(n1-n2)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
