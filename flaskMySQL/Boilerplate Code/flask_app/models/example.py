from flask_app.config.mysqlconnection import connectToMySQL

class Example: # name change needed
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name'] #name change needed
        self.last_name = data['last_name'] #name change needed
        self.occupation = data['occupation'] #name change needed
        self.created_at = data['created_at'] #name change needed
        self.updated_at = data['updated_at'] #name change needed

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        examples = [] #name change needed
        for example in results: #name change needed
            examples.append( cls(example) ) #name change needed
        return examples #name change needed
