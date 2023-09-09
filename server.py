from flask import Flask,request,url_for

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    a=request.form['first']
    b=request.form['second']
    answer=a+b 
    return {'result ':answer}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    a=request.form['first']
    b=request.form['second']
    ans=a-b 
    return {'result ':ans}
    

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
