from flask import Flask, request, make_response
from dataclasses import dataclass

@dataclass
class Computation:
    value: int

app = Flask(__name__)

@app.route("/calc/welcome", methods=['GET'])
def welcome():
    return 'Welcome to the calculator API!'

@app.route("/calc/sum", methods=['POST'])
def sum_numbers():
    data = request.get_json()
    total = Computation(data['a'] + data['b'])
    return make_response(total)

@app.route("/calc/difference", methods=['POST'])
def difference():
    data = request.get_json()
    diff = Computation(data['a'] - data['b'])
    return make_response(diff)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
