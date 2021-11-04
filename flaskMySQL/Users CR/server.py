from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ='scooby-doo where are you???'

@app.route('/users')
def users():
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)