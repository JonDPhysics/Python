from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.account import Account
from flask_app.models.budget import BCRYPT



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
    if not session:
        return redirect("/")
    context = {
        "user": User.get_users_with_accounts({"id": session['uuid']}),
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
