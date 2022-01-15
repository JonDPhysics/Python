from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.budget import Budget, SCHEMA
from flask import flash



class Account:
    def __init__(self, data):
        self.id = data["id"]
        self.account_name = data["account_name"]
        self.account_balance = data["account_balance"]
        self.account_date = data["account_date"]
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
        query = "Select * FROM accounts WHERE account_name = %(account_name)s;"
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
                "input": data["input"],
                "amount": data["amount"],
                "date": data["date"],
                "account_id": data["account_id"],
                "created_at": data["budgets.created_at"],
                "updated_at": data["budgets.updated_at"]
            }
            account.budgets.append(Budget(budget_data))
        return account

    @classmethod
    def insert_account(cls, data):
        query = "INSERT INTO accounts (account_name, account_balance, account_date, user_id) VALUE (%(account_name)s, %(account_balance)s, %(account_date)s, %(user_id)s);"
        return connectToMySQL(SCHEMA).query_db(query, data)

    @classmethod
    def updated_account(cls, data):
        query ="UPDATE accounts SET account_name = %(account_name)s, account_balance = %(account_balance)s, account_date = %(account_date)s, user_id = %(user_id)s WHERE id = %(id)s;"
        connectToMySQL(SCHEMA).query_db(query, data)

    @classmethod
    def delete_account(cls, data):
        query = "DELETE FROM accounts WHERE id = %(id)s;"
        connectToMySQL(SCHEMA).query_db(query, data)

    @staticmethod
    def account_val(pd):
        is_valid = True
        if len(pd["account_name"]) < 1:
            flash("Name must be at least 1 characters.")
            return False
        return is_valid


