from flask import request, Blueprint, redirect, render_template, session, url_for, jsonify, json
from .. import db
from main.models import UsuariosModel
from flask_jwt_extended import create_access_token


auth = Blueprint("auth",__name__,url_prefix="/auth")



@auth.route("/register",methods=["POST"])
def register():
    usuario = UsuariosModel.from_json(request.get_json())
    exits = db.session.query(UsuariosModel).filter(UsuariosModel.email == usuario.email).scalar() is not  None

    if exits:
        return "duplicated email", 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        
    return usuario.to_json, 201



@auth.route("/login",methods=["POST"])
def login():
    usuario = db.session.query(UsuariosModel).filter(UsuariosModel.email == request.form.get("email")).first_or_404()

    if usuario.validate_pass(request.form.get("password")):
        
        access_token = create_access_token(identity=str(usuario.id))

        session['access_token'] = access_token

        data = {
            "id": str(usuario.id),
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "access_token": access_token,
            "role": usuario.role
        }
        return redirect(url_for('menu.index'))
    
    else:
        return "incorrect password"
    

