from flask_app.models.user import User
from flask_app.models.account import Account
from flask.globals import request
from flask_app import app
from flask import render_template, redirect, request, session


@app.route("/accounts/new")
def new_account():
    context = {
        "user": User.get_user_by_id({"id": session['uuid']})
    }
    return render_template("add_account.html", **context)

@app.route("/accounts/add", methods = ["POST"])
def add_account():
    if not Account.account_val(request.form):
        return redirect("/accounts/new")

    data = {
        **request.form,
        'user_id': session['uuid']
    }
    Account.insert_account(data)
    return redirect("/dashboard")

@app.route("/accounts/edit/<int:id>")
def edit_account(id):
    context = {
        "user": User.get_user_by_id({"id": session['uuid']}),
        "account": Account.get_account_by_id({"id": id})
    }
    return render_template("edit_account.html", **context)

@app.route("/accounts/update/<int:id>", methods = ["POST"])
def update_account(id):
    data = {
        'id': id,
        **request.form,
        "user_id": session['uuid']
    }
    Account.updated_account(data)
    return redirect("/dashboard")

@app.route("/accounts/delete/<int:id>")
def delete_account(id):
    Account.delete_account({"id": id})
    return redirect("/dashboard")
