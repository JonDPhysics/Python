from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.example import Example # name change needed

@app.route("/")
def start():
    return render_template("table.html", examples = Example.get_all())

@app.route ("/edit", methods=['POST'])
def edit():
    render_template("form.html")
