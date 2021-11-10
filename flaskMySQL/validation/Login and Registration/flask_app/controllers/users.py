from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

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

    User.insert_user(data)
    return redirect("/dashboard")

@app.route("/dashboard")
def dash():
    return render_template("dashboard.html")

@app.route("/logout")
def out():
    pass