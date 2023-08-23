from flask import Flask, request

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    fn = data["first"]
    sn = data["second"]
    res ={
        "result": fn + sn
    }
    return res
@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    fn = data["first"]
    sn = data["second"]
    res ={
        "result": fn - sn
    }
    return res

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')