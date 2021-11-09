from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import model_user

@app.route("/")
def start():
    return render_template("index.html", users = model_user.User.get_all())

@app.route("/new")
def add_user():
    return render_template("add.html")

@app.route ("/add", methods=['POST'])
def add():
    data = {
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    model_user.User.create(data)
    return redirect("/")

@app.route("/edit_user")
def edit_user():
    return render_template("edit.html", users = model_user.User.get_all())

@app.route("/edit", methods=['POST'])
def edit():
    model_user.User.update(request.form)
    return redirect("/") 

@app.route("/show/<int:id>")
def show_one(id):
    context = {
        'users': model_user.User.get_by_id({'id': id}),
    }
    return render_template("show.html", **context)


@app.route("/delete/<int:id>")
def delete_user(id):
    model_user.User.remove({'id': id})
    return redirect("/")
