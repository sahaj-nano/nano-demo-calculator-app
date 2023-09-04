from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world'

@app.route("/calculator/add", methods=['POST'])
def add():
    fNum = Flask.request.form["first"]
    sNum = Flask.request.form["second"]

    return fNum + sNum

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    fNum = Flask.request.form["first"]
    sNum = Flask.request.form["second"]

    return fNum - sNum

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
