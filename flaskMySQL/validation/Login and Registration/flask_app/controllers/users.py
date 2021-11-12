from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User, bcrypt


@app.route("/")
def start():
    return render_template("log_reg.html")

@app.route("/register", methods=['POST'])
def register():
    if not User.reg_val(request.form):
        return redirect("/")

    hash_it_out = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": hash_it_out
    }

    user_id = User.insert_user(data)
    session["uuid"] = user_id
    return redirect("/dashboard")

@app.route("/dashboard")
def dash():
    return render_template("dashboard.html", user = User.get_user_by_id({"id": session["uuid"]}))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/login", methods=['POST'])
def login():
    if not User.log_val(request.form):
        return redirect("/")

    user = User.get_user_by_email({"email": request.form["email"]})
    session["uuid"] = user.id
    return redirect("/dashboard")

