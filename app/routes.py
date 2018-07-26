from flask import render_template
from app import app

@app.route('/')
#@app.route('/index')
def index():
    return "Hello, World!"
if __name__== "__main__":
    app.run()