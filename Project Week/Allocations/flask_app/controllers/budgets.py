from flask_app.models.user import User
from flask_app.models.account import Account
from flask_app.models.budget import Budget
from flask_app import app
from flask import render_template, redirect, request, session

@app.route("/display/<int:id>")
def display(id):
    context = {
        "user": User.get_user_by_id({"id": session["uuid"]}),
        "account": Account.get_accounts_with_budgets({"id": id}),
    }
    return render_template("display.html", **context)

@app.route("/budgets/new/<int:id>")
def new_budget(id):
    context = {
        "account": Account.get_account_by_id({"id": id})
    }
    return render_template("add_budget.html", **context)

@app.route("/budgets/add/<int:id>", methods=["POST"])
def add_budget(id):
    data = {
        **request.form,
        "account_id": id
    }
    Budget.insert_budget(data)
    return redirect(f"/display/{id}")

@app.route("/budgets/edit/<int:id>/<input_name>")
def edit_budget(id, input_name):
    context = {
        "account_id": Account.get_account_by_id({"id": id}),
        "budget": Budget.get_budget_by_name({"input_name": input_name})
    }
    return render_template("edit_budget.html", **context)

@app.route("/budgets/update/<int:bid>/<int:aid>", methods=["POST"])
def update_budget(bid, aid):
    data = {
        "account_id": Account.get_account_by_id({"id": aid}),
        "budget": Budget.get_budget_by_id({"id": bid})
    }
    Budget.update_budget(data)
    return redirect(f"/display/{aid}")