from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    first = int(request.args.get('first'))
    second = int(request.args.get('second'))
    return { "result": first+second }
    #return "Hello World"

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    first = int(request.args.get('first'))
    second = int(request.args.get('second'))
    return { "result": first-second }
if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
