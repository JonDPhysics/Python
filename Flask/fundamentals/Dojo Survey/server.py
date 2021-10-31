from logging import debug
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Sweet Dude"

@app.route("/")
def start():
    return render_template('index.html')

@app.route("/results")
def result():
    return render_template('results.html')

@app.route("/process", methods=['POST'])
def proccess():
    session['name']= request.form['name']
    session['loco']= request.form['dojo_location']
    session['lang']= request.form['favorite_language']
    session['comment']= request.form['Comments']
    return redirect("/results")

if __name__=='__main__':
    app.run(debug=True)
