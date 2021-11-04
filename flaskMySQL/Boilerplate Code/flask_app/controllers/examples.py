from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from example import Example # name change needed

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/add", methods=['POST'])
def add():
    return redirect("/")

@app.route ("/edit", methods=['POST'])
def edit():
    return redirect("/")
