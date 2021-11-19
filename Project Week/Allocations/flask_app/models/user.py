from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.account import Account
from flask_app.models.budget import EMAIL_REGEX, SCHEMA, BCRYPT
from flask import flash

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.accounts =[]

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
    def get_users_with_accounts(cls, data):
        query = "SELECT * FROM users LEFT JOIN accounts ON accounts.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if not results:
            return False
        user = cls(results[0])
        for data in results:
            account_data = {
                "id": data["accounts.id"],
                "name": data["name"],
                "balance": data["balance"],
                "user_id": data["user_id"],
                "created_at": data["accounts.created_at"],
                "updated_at": data["accounts.updated_at"]
            }
            user.accounts.append(Account(account_data))
        return user

    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUE (%(first_name)s, %(last_name)s, %(email)s, %(pw)s)"
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

        if not BCRYPT.check_password_hash(user.password, pd["pw"]):
            flash("Incorrect Password")
            return False

        return True