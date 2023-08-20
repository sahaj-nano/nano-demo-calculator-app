from flask import Flask
app = Flask(__name__)
@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'greeting'
@app.route("/calculator/add", methods=['POST'])
def add():
    return 'add'
@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return 'subtract'
if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
