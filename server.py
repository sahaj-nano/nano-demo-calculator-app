from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return jsonify({"Content": "Hello world!"}), 200

@app.route('/calculator/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        first = data['first']
        second = data['second']
        result = first + second
        return jsonify({"result": result}), 200
    except KeyError:
        return jsonify({"error": "Invalid input. Please provide 'first' and 'second' values."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        first = data['first']
        second = data['second']
        result = first - second
        return jsonify({"result": result}), 200
    except KeyError:
        return jsonify({"error": "Invalid input. Please provide 'first' and 'second' values."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
