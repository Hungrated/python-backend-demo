from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Hello Python Web!</h1><br><br><a href="127.0.0.1:9090/signin">Sign In</a>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form><br><a href="127.0.0.1:9090/">Back To Home</a>'''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        return '<h3>Hello, admin!</h3><br><a href="127.0.0.1:9090/">Back To Home</a>'
    return '<h3>Bad username or password.</h3><br><a href="127.0.0.1:9090/">Back To Home</a>'


if __name__ == '__main__':
    app.run()
