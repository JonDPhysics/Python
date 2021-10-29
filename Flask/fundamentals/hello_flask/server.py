from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately followin
def hello_world():
    return render_template('index.html')  # Return the result of the render_template method with the name of our HTML file as a parameter

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<string:banana>/<int:num>')
def hello(dude,num):
    return f"Hello {dude * num}"

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: "+username+", id: "+id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug = True)    # Run the app in debug mode.

