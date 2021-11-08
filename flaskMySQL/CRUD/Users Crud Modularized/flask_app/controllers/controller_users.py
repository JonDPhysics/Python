from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_user import User

@app.route("/")
def start():
    return render_template("index.html", users = User.get_all())

@app.route("/new")
def add_user():
    return render_template("add.html")

@app.route ("/edit", methods=['POST'])
def edit():
    data = {
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.create(data)
    return redirect("/")
