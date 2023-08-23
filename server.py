from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the Calculator API!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json  # Assuming you're sending JSON data in the request
    if 'numbers' in data:
        numbers = data['numbers']
        result = sum(numbers)
        response = {
            'operation': 'addition',
            'numbers': numbers,
            'result': result
        }
        return jsonify(response)
    else:
        return jsonify({'error': 'Missing numbers in request data'}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json  # Assuming you're sending JSON data in the request
    if 'numbers' in data:
        numbers = data['numbers']
        if len(numbers) >= 2:
            result = numbers[0]
            operation_steps = [numbers[0]]
            for num in numbers[1:]:
                result -= num
                operation_steps.append(f"- {num}")
            response = {
                'operation': 'subtraction',
                'numbers': numbers,
                'operation_steps': operation_steps,
                'result': result
            }
            return jsonify(response)
        else:
            return jsonify({'error': 'At least 2 numbers required'}), 400
    else:
        return jsonify({'error': 'Missing numbers in request data'}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
