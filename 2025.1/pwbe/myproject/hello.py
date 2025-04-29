from flask import Flask
from flask import request
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('index.html', person=name)

# @app.route("/")
# def hello_world():
#     return render_template('index.html')

@app.route("/user/<int:username>")
def hello_user(username):
    print(username)
    print(type(username))
    return f'Hello, {escape(username)}'

@app.route("/user/<string:username>")
def hello_user_dois(username):
    print(username)
    print(type(username))
    return f'Hello, {escape(username)}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
    user = request.form['username']
    password =  request.form['password']
    print(user)
    print(password)
        return do_the_login()
    else:
        return render_template('login.html')


# @app.route("/user/<username>")
# def hello_username():
#     return "<p>Hello, World! -- Teste</p>"