from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return jsonify(message='Hello world!')

@app.route('/calculator/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'first' not in data or 'second' not in data:
        return jsonify(error='Invalid request data'), 400
    
    result = data['first'] + data['second']
    return jsonify(result=result)

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'first' not in data or 'second' not in data:
        return jsonify(error='Invalid request data'), 400
    
    result = data['first'] - data['second']
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
