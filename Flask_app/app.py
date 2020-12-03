from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    app.logger.error('Processing default request')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


