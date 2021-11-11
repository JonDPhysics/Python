from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
import re

bcrypt =Bcrypt(app)

SCHEMA = 'log_reg_rep'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(SCHEMA).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if len(results) < 1:
            return False
        return User(results[0])

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if len(results) < 1:
            return False
        return User(results[0])

    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO user (first_user, last_name, email, password,) VALUE (%(first_name)s, %(last_name)s, %(email)s, %(pw)s)"
        return connectToMySQL(SCHEMA).query_db(query, data)


    @staticmethod
    def reg_val(pd):
        is_valid = True

        if len(pd["first_name"]) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False

        if len(pd["last_name"]) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False

        if not EMAIL_REGEX.match(pd['email']): 
            flash("Invalid email address!")
            is_valid = False
        else:
            user = User.get_user_by_email({'email': pd['email']})
            if user:
                flash("Email is already in use!")
                is_valid = False

        if len(pd["pw"]) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False

        if pd["pw"] != pd['cpw']:
            flash("Password and Confirm Password must match.")
            is_valid = False

        return is_valid

    @staticmethod
    def log_val(pd):
        user = User.get_user_by_email({"email": pd["email"]})

        if not user:
            flash("Email not registered")
            return False

        if not bcrypt.check_password_hash(user.password, pd["pw"]):
            flash("Incorrect Password")
            return False

        return True