from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World'

@app.route("/calculator/add", methods=['POST'])
def add(first,second):
    return first+second

@app.route("/calculator/subtract", methods=['POST'])
def subtract(first,second):
    return first-second

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
    greetings = greeting()
    print(greetings)
    op = input('add or sub')
    first = int(input())
    second = int(input())
    if op == add:
        print(add(first,second))
    else:
        print(subtract(first,second))

        