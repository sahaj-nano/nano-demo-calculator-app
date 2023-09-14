from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add(first,second):
    return first+second

@app.route("/calculator/subtract", methods=['POST'])
def subtract(first,second):
    return first-second

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
    greetings=greeting()
    operation=input('What do you want to do "Add" or "Subtract"')
    first,second=list(map(int,input().split()))
    if operation=='add':
        print(add(first,second))
    else:
        print(subtract(first,second))

