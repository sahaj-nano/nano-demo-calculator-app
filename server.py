from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    # data = request.json()
    # first = data.get('first')
    # second = data.get('second')
    
    # if first is None or second is None:
    #     return 'Bad Request', 400
    return ''

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
