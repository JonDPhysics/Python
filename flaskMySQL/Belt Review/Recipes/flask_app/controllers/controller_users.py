from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.models_user import User
from flask_app.models.models_recipe import Recipe, BCRYPT



@app.route("/")
def start():
    return render_template("reg_log.html")

@app.route ("/register", methods=['POST'])
def reg():
    if not User.reg_val(request.form):
        return redirect("/")
    hash_it_out = BCRYPT.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        "pw": hash_it_out
    }

    User.insert_user(data)
    return redirect("/dashboard")

@app.route("/dashboard")
def dash():
    return render_template("dashboard.html", user = User.get_users(), recipes = Recipe.get_recipes())

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    if not User.log_val(request.form):
        return redirect("/")
    user = User.get_user_by_email({"email": request.form["email"]})
    session["uuid"] = user.id
    return redirect("/dashboard")