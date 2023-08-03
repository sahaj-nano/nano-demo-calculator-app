from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    json_data = request.get_json()
    first_number = json_data['first']
    first_number = abs(first_number)
    second_number = json_data['second']
    second_number = abs(second_number)
    sum = first_number + second_number
    return '{ "result": ' + str(sum) + ' }'

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    json_data = request.get_json()
    first_number = json_data['first']
    second_number = json_data['second']
    # second_number = abs(second_number)
    sub = first_number - second_number
    return '{ "result": ' + str(sub) + ' }'

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
