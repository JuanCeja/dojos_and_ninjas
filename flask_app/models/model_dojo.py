from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninja
from flask_app.models import model_dojo
from flask import flash

DATABASE = "dojos_and_ninjas_schema"

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo_id = connectToMySQL(DATABASE).query_db(query, data) #returs id of the new row created
        return dojo_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL(DATABASE).query_db(query)

        if results:
            table_names = []
            for dojo in results:
                table_names.append(cls(dojo))
            return table_names
        return []

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data) #returns us a LIST of DICTIONARIES
        if result:
            return cls(result[0])
        return False


    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        dojo = cls(results[0])
        for row in results:
            # ninja_data = {
            #     "id": row['ninjas.id'],
            #     "first_name": row['first_name'],
            #     "last_name": row['last_name'],
            #     "age": row['age'],
            #     "created_at": row['ninjas.created_at'],
            #     "updated_at": row['ninjas.updated_at']
            # }
            ninja_data = {
                **row,
                "id": row['ninjas.id'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at']
            }
            
            dojo.ninjas.append(model_ninja.Ninja(ninja_data))
        return dojo


    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_dba(query, data)

    @staticmethod
    def is_valid(model_dojo):
        is_valid = True
        if len(model_dojo['name']) < 3:
            is_valid = False
            flash("Dojo name must be atleast 3 characters.")
        return is_valid

    # @classmethod
    # def save(cls, data):
    #     query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     return result

    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at=NOW() WHERE id = %(id)s;"
    #     updated_result = connectToMySQL(DATABASE).query_db(query, data)
    #     return updated_result

    # @classmethod
    # def update_one(cls, data):
    #     query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)