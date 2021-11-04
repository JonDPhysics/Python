from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    return render_template("index.html", users = User.get_all())

@app.route("/users/new")
def new_user():

    render_template("add.html")

@app.route("/create_user", methods = ["POST"])
def create_user():
    data = {
        "fullname": request.form["fname", "lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/users")

@app.route("/add_user", methods = ["POST"])
def add_users():

    return redirect("/users/new")

if __name__ == "__main__":
    app.run(debug=True)