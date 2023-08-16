from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    # return 200, "Hello world!"
    # response = {"code":200,"content":"hello world!"}
    # return response
    # return "Hello world!", 200
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.get_json()
        if data is None or "first" not in data or "second" not in data:
            raise ValueError("Invalid JSON data")
        first_number = data["first"]
        second_number = data["second"]
        result = first_number+second_number

        response = {
            "Status code": 200,
            "result": result
        }

        return jsonify(response)
    
    except Exception as e:
        error_response = {
            "Status code": 400,
            "error": str(e)
        }

        return jsonify(error_response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if data is None or "first" not in data or "second" not in data:
        raise ValueError("Invalid JSON Data")
    first_number = data["first"]
    second_number = data["second"]
    result = first_number-second_number

    response = {
        "Status code": 200,
        "result": result
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
