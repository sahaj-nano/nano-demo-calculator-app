from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    res=request.get_json()
    ad=int(res['first']+res['second'])
    return jsonify(ad)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    res=request.get_json()
    su=int(res['first']-res['second'])
    return jsonify(su)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
