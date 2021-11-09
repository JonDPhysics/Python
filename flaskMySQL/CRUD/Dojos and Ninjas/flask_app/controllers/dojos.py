from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo

@app.route("/dojos")
def start():
    return render_template("dojo.html", dojos = dojo.Dojo.get_all())

@app.route ("/add/dojo", methods=['POST'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    dojo.Dojo.add(data)
    redirect("/dojos")
