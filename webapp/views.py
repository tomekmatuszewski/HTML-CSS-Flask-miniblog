from flask import Flask, render_template

app = Flask(__name__)


@app.route('/blog')
def main_page():
    return render_template('index.html')

@app.route('/entry')
def entry():
    return render_template('entry.html')
