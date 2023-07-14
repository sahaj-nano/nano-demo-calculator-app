from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    first = Flask.request.args.get('first')
    second = Flask.request.args.get('second')
    return Flask.jsonify({'data':f'<p>The result is: {first+second}</p>'})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    first = Flask.request.args.get('first')
    second = Flask.request.args.get('second')
    return Flask.jsonify({'data':f'<p>The result is: {first-second}</p>'})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
