from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo

@app.route("/dojos")
def start():
    return render_template("dojo.html", dojos = dojo.Dojo.get_dojos())

@app.route("/add/dojo", methods=['POST'])
def insert_dojo():
    data = {
        'name': request.form['name']
    }
    dojo.Dojo.insert_dojo(data)
    return redirect("/dojos")

@app.route("/dojos/<int:dojo_id>")
def get_dojo_by_id(dojo_id):
    context = {
        'dojo': dojo.Dojo.get_dojos_with_ninjas({'id': dojo_id})
    }
    return render_template("show.html", **context)
