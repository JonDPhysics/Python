from logging import debug
from flask_app.controllers import users, routes # name change needed 
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)