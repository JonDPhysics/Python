from logging import debug
from flask_app.controllers import dojos, ninjas
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)