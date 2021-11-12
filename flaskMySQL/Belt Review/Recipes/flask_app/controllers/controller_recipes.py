from typing import ParamSpecArgs
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.models_recipe import Recipe
from flask_app.models.models_user import User

@app.route("/recipes/new")
def new_recipe():
    return render_template("add_recipe.html")

@app.route("/recipes/add", methods=['POST'])
def add_recipes():
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    Recipe.insert_recipe(data)

    # Having trouble connecting users.id to user_id
    # without passing user_id or users.id through the url.
    return redirect("/dashboard")

@app.route("/recipes/<int:id>")
def edit_recipe(id):
    return render_template("edit_recipe.html", recipe = Recipe.get_recipe_by_id(id))

@app.route("/recipes/edit/<int:id>")
def display_recipe(id):
    return render_template("display.html", recipe = Recipe.get_recipe_by_id(id))

@app.route("/recipes/delete/<int:id>")
def delete(id):
    Recipe.delete_recipe(id)
    return render_template("dashboard.html", user = User.get_users(), recipe = Recipe.get_recipes())