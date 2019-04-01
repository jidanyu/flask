from flask import Flask, render_template, url_for, redirect
from fromView import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key='123123'
Bootstrap(app)

@app.route('/')
def hello_world():
    return 'Hello World!222'




if __name__ == '__main__':
    app.run()

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)