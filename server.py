from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'


@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()  # Get JSON data from the request
    first = data.get('first', 0)
    second = data.get('second', 0)
    result = first + second
    response = {'result': result}
    # Return JSON response with result and status code 200
    return jsonify(response), 200


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()  # Get JSON data from the request
    first = data.get('first', 0)
    second = data.get('second', 0)
    result = first - second
    response = {'result': result}
    # Return JSON response with result and status code 200
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
