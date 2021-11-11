from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route("/recipes/new")
def new_recipe():
    return render_template("add_recipe.html")

@app.route("/recipes/add", methods=['POST'])
def add_recipes():
    data 
    #Recipe.insert_recipe(request.form)
    """
    Having trouble connecting users.id to user_id
    without passing user_id or users.id through the url.
    """
    return redirect("/dashboard")

@app.route("/recipes/<int:id>")
def display_recipe(id):
    return render_template("display.html", recipe =  Recipe.get_recipe_by_id(id))
