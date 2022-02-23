from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_ninja import Ninja

#from flask_app.models.model_table_name import class_name

@app.route("/ninjas")
def ninjas():
    return render_template('add_ninja.html', dojos=Dojo.get_all())

@app.route("/create/ninja", methods=["post"])
def create_ninja():
    if Ninja.is_valid(request.form):
        id = Ninja.create(request.form)
        return redirect('/ninjas')
    return redirect('/ninjas')


# @app.route("/tablename/<int:id>")
# def show_tablename():
#     pass

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