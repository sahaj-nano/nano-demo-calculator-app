from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'helloo'

@app.route("/calculator/add", methods=['POST'])
def add():
    return ''

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0')
