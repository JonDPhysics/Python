from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

SCHEMA = 'log_reg'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if len(results) < 1:
            return False
        return User(results[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if len(results) < 1:
            return False
        return User(results[0])

    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUE (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"
        return connectToMySQL(SCHEMA).query_db(query, data)

    @staticmethod
    def reg_val(user_data):
        is_valid = True

        if len(user_data["first_name"]) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False

        if len(user_data["last_name"]) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid email address!")
            is_valid = False
        else:
            user = User.get_user_by_email({'email': user_data['email']})
            if user:
                flash("Email is already in use!")
                is_valid = False

        if len(user["password"]) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False

        if user_data["password"] != user_data['confirm_password']:
            flash("Password and Confirm Password must match.")
            is_valid = False

        return is_valid

    @staticmethod
    def log_val(user_data):
        pass