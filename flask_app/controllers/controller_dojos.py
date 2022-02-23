from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_dojo import Dojo
#from fDask_app.models.model_table_name import class_name

@app.route("/")
def index():
    return render_template('index.html', dojos=Dojo.get_all())

# @app.route("/show_ninjas")
# def index():
#     return render_template('show_ninjas.html', )

@app.route("/dojo/create", methods=["post"])
def create_dojo():
    id = Dojo.create(request.form)
    return redirect('/')

@app.route("/dojos/<int:id>")
def show_dojo_with_ninjas(id):
    dojo = Dojo.get_dojo_with_ninjas({"id": id})
    return render_template('show_ninjas.html', dojo=dojo)

# @app.route("/tablename/<int:id>/edit")
# def edit_tablename(id):
#     tablename = tablename.get_one({'id':id})
#     return render_template('tablename_edit.html', tablename=tablename)

# @app.route("/tablename/<int:id>/update", methods=["post"])
# def update_tablename(id):
#     tablename.update_one(request.form)
#     return redirect('/')

# @app.route("/tablename/<int:id>/delete")
# def delete_tablename(id):
#     tablename.delete_one({'id': id})
#     return redirect('/')