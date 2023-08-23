from flask import Flask

app = Flask(__name__)

#abc
@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello'

@app.route("/calculator/add", methods=['POST'])
def add(a,b):
    return 'a+b'

@app.route("/calculator/subtract", methods=['POST'])
def subtract(a,b):
    return 'a-b'

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
