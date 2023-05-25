from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
