from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "dojos_and_ninjas_schema"

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        ninja_id = connectToMySQL(DATABASE).query_db(query, data) #returs id of the new row created
        return ninja_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"

        results = connectToMySQL(DATABASE).query_db(query)

        if results: 
            table_names = []
            for ninja in results:
                table_names.append(cls(ninja))
            return table_names
        return []

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data) #returns us a LIST of DICTIONARIES
        if result:
            return cls(result[0])
        return False

    @classmethod
    def add_ninja_to_dojo(cls, data):
        query = "INSERT INTO dojos (first_name, last_name, age) VALUES (%(first_name)s, %(last_name)s, %(age)s);"
        

    @classmethod
    def update_one(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at=NOW() WHERE id = %(id)s;"
    #     updated_result = connectToMySQL(DATABASE).query_db(query, data)
    #     return updated_result

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_dba(query, data)

    # @classmethod
    # def save(cls, data):
    #     query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     return result