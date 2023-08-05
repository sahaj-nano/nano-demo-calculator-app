from dataclasses import dataclass
from flask import Flask, request, jsonify


@dataclass
class Result:
    result: int


app = Flask(__name__)


@app.route("/calculator/greeting", methods=["GET"])
def greeting():
    return "Hello world!"


@app.route("/calculator/add", methods=["POST"])
def add():
    numbers = request.json
    response = Result(numbers["first"] + numbers["second"])
    return jsonify(response)


@app.route("/calculator/subtract", methods=["POST"])
def subtract():
    numbers = request.json
    response = Result(numbers["first"] - numbers["second"])
    return jsonify(response)


@app.route("/calculator/multiply", methods=["POST"])
def multiply():
    numbers = request.json
    response = Result(numbers["first"] * numbers["second"])
    return jsonify(response)


@app.route("/calculator/divide", methods=["POST"])
def divide():
    numbers = request.json
    if numbers["second"] == 0:
        return jsonify({"error": "Cannot divide by zero."}), 400
    response = Result(numbers["first"] / numbers["second"])
    return jsonify(response)


@app.route("/calculator/power", methods=["POST"])
def power():
    numbers = request.json
    response = Result(numbers["base"] ** numbers["exponent"])
    return jsonify(response)


@app.route("/calculator/square-root", methods=["POST"])
def square_root():
    number = request.json["number"]
    if number < 0:
        return (
            jsonify({"error": "Cannot calculate square root of a negative number."}),
            400,
        )
    response = Result(number**0.5)
    return jsonify(response)


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
