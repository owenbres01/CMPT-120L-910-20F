from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
def index():
    return '<h1>hello</h1>'

