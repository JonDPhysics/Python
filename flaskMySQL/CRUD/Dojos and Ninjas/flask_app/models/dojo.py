from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import DATAB
from flask_app.models.ninja import Ninja


class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATAB).query_db(query)
        dojos = [] 
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_dojos_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATAB).query_db(query, data)
        if not results:
            return False
        dojo = cls(results[0])
        for data in results:
            ninja_data = {
                "id" : data["ninjas.id"],
                "first_name" : data["first_name"],
                "last_name" : data["last_name"],
                "age" : data["age"],
                "dojo_id": data["dojo_id"],
                "created_at" : data["ninjas.created_at"],
                "updated_at" : data["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

    @classmethod
    def insert_dojo(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUE (%(name)s, NOW(), NOW());"
        return connectToMySQL(DATAB).query_db(query, data)
