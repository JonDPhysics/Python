from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
import re

BCRYPT = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
SCHEMA = "log_reg_rep"

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.within = data['within']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def insert_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instruction, within, user_id) VALUE (%(name)s, %(description)s, %(instruction)s, %(within)s, %(user_id)s);"
        return connectToMySQL(SCHEMA).query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipe SET name= %(name)s, description = %(description)s, instruction = %(instruction)s, within = %(within)s, user_id = %(user_id)s)"
        connectToMySQL(SCHEMA).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL(SCHEMA).query_db(query, data)