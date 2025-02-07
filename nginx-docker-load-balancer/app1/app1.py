from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'app 1 RESPONDING\n'


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)
