from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from user import User
app = Flask(__name__)
app.secret_key = "TOP-SECRET: need to know required"

@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    return render_template("index.html", users = User.get_all())

@app.route("/new")
def new_user():
    return render_template("add.html")

@app.route("/create_user", methods = ["POST"])
def create_user():
    data = {
        "fname": request.form["fname"], 
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)