from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import ninja
from flask_app.models import dojo


@app.route("/add/ninjas")
def index_ninja():
    return render_template("ninja.html", dojos = dojo.Dojo.get_dojos())

@app.route("/ninjas", methods=["POST"])
def insert_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    ninja.Ninja.insert_ninja(data)
    print(data)
    return redirect(f"/dojos/{data['dojo_id']}")