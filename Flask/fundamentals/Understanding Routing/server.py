from logging import debug
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_planet():
    return "Hello World!"

@app.route('/dojo')
def coding():
    return "Dojo!"
    

@app.route('/say/<string:name>')
def the_flask(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_me(num,word):
    print(num)
    print(word)
    return f"{word * num}"

if __name__=="__main__":
    app.run(debug=True)

