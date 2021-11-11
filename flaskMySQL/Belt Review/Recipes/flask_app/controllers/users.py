from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import BCRYPT



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

    uid =User.insert_user(data)
    session["uuid"] = uid
    return redirect("/dashboard", session["uuid"])

@app.route("/dashboard")
def dash():
    context = {
        'user': User.get_users_with_recipes({'id': session["uuid"]})
    }
    return render_template("dashboard.html", **context)

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