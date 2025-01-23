from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "To jest pierwsza prosta aplikacja www - <B>framework FLASK!</B>"

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1')
