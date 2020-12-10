from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.error('Processing default request')
    return render_template('index.html')

@app.route('/AboutMe')
def about_me():
    return render_template('index2.html')

@app.route('/Contact')
def contact():
    return render_template('index3.html')

@app.route('/MyPersonality')
def my_personality():
    return render_template('index4.html')

if __name__ == "__main__":
    app.run(debug=True)


