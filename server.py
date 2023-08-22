from flask import Flask,request,json

app = Flask(__name__)

@app.route("/hello",methods=['GET'])
def hello():
    return "Hello!"


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data=json.loads(request.data)
    return {"result": data["first"] + data["second"]}


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    sub=json.loads(request.data)
    Dict1 = {"result": sub["first"]-sub["second"]}
    
    return Dict1

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
