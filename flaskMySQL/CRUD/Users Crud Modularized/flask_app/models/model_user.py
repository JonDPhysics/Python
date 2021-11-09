from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "users_cr_db"

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) Value (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def remove(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        connectToMySQL(DATABASE).query_db(query, data)
