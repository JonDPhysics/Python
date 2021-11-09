from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at'] 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        dojos = [] 
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def insert(cls,data):
        pass