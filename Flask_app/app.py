from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello')
def hello_world():
    return '<h1>hello</h1>'

