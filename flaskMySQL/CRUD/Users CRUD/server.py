from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from user import User
app = Flask(__name__)
app.secret_key = "TOP-SECRET: need to know required"

@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    return render_template("index.html", users = User.get_all())

@app.route("/show")
def show_user():
    return render_template("show.html", users = User.get_one())

@app.route("/edit")
def edit_user():
    all_users = user.User.get_all()
    return render_template("edit.html", all_users=all_users)

@app.route('/change_info', methods=['POST'])
def change_info():
    
    return redirect("/users")

@app.route("/delete")
def delete_user():
    User.remove()
    return render_template("index.html")

@app.route("/new")
def new_user():
    return render_template("add.html")

@app.route("/create_user", methods = ["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)