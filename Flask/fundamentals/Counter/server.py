from logging import debug
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def counting():
    count = 0
    return render_template('index.html', count = count + 1)

if __name__=='__main__':
    app.run(debug=True)