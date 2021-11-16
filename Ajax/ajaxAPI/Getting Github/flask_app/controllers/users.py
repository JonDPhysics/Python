from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route("/")
def start():
    return render_template("reg_log.html")

@app.route ("/recipe/edit", methods=['POST'])
def edit(id):
    return redirect(f"/recipe/edit/{id}")
