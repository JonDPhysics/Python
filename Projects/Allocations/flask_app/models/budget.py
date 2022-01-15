from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app
import re

BCRYPT =Bcrypt(app)
SCHEMA = 'allocations'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Budget:
    def __init__(self, data):
        self.id = data["id"]
        self.input = data["input"]
        self.amount = data["amount"]
        self.date = data["date"]
        self.account_id = data["account_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_budgets(cls):
        query = "SELECT * FROM budgets;"
        results = connectToMySQL(SCHEMA).query_db(query)
        budgets = []
        for budget in results:
            budgets.append(cls(budget))
        return budgets

    @classmethod
    def get_budget_by_id(cls, data):
        query = "SELECT * FROM budgets WHERE id = %(id)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if len(results) < 1:
            return False
        return Budget(results[0])

    @classmethod
    def get_budget_by_name(cls, data):
        query = "SELECT * FROM budgets WHERE input = %(input)s;"
        results = connectToMySQL(SCHEMA).query_db(query, data)
        if len(results) < 1:
            return False
        return Budget(results[0])

    @classmethod
    def insert_budget(cls, data):
        query = "INSERT INTO budgets (input, date, amount, account_id) VALUE (%(input)s, %(date)s, %(amount)s, %(account_id)s);"
        return connectToMySQL(SCHEMA).query_db(query, data)

    @classmethod
    def update_budget(cls, data):
        query ="UPDATE budgets SET input = %(input)s, date = %(date)s, amount = %(amount)s, account_id = %(account_id)s WHERE id = %(id)s;"
        connectToMySQL(SCHEMA).query_db(query, data)

    @classmethod
    def delete_budget(cls, data):
        query = "DELETE FROM budgets WHERE id = %(id)s;"
        connectToMySQL(SCHEMA).query_db(query, data)