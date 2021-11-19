from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.budget import Budget, SCHEMA
from flask import flash



class Account:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.balance = data["balance"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.budgets = []

    @classmethod
    def get_accounts(cls):
        query = "SELECT * FROM accounts;"
        results = connectToMySQL(SCHEMA).query_db(query)
        accounts = []
        for account in results:
            accounts.append(cls(account))
        return accounts

    @classmethod
    def get_account_by_id(cls, data):
        query = "SELECT * FROM accounts WHERE id = %(id)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if len(results) < 1:
            return False
        return Account(results[0])

    @classmethod
    def get_account_by_name(cls, data):
        query = "Select * FROM accounts WHERE name = %(name)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if len(results) < 1:
            return False
        return Account(results[0])

    @classmethod
    def get_accounts_with_budgets(cls, data):
        query = "SELECT * FROM accounts LEFT JOIN budgets ON budgets.account_id = accounts.id WHERE accounts.id = %(id)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if not results:
            return False
        account = cls(results[0])
        for data in results:
            budget_data = {
                "id": data["budgets.id"],
                "input_name": data["input_name"],
                "amount": data["amount"],
                "date": data["date"],
                "transaction": data["transaction"],
                "account_id": data["account_id"],
                "created_at": data["budgets.created_at"],
                "updated_at": data["budgets.updated_at"]
            }
            account.budgets.append(Budget(budget_data))
        return account

    @classmethod
    def insert_account(cls, data):
        query = "INSERT INTO accounts (name, balance, user_id) VALUE (%(name)s, %(balance)s, %(user_id)s);"
        return connectToMySQL(SCHEMA).query_db(query, data)

    @classmethod
    def updated_account(cls, data):
        query ="UPDATE accounts SET name = %(name)s, balance = %(balance)s WHERE id = %(id)s;"
        connectToMySQL(SCHEMA).query_db(query, data)

    @classmethod
    def delete_account(cls, data):
        query = "DELETE FROM accounts WHERE id = %(id)s;"
        connectToMySQL(SCHEMA).query_db(query, data)

    @staticmethod
    def account_val(pd):
        is_valid = True
        if len(pd["name"]) < 1:
            flash("Name must be at least 1 characters.")
            return False
        return is_valid


