from flask import request, Blueprint, redirect, session, url_for, flash
from .. import db
from main.models import UsuariosModel
from flask_jwt_extended import create_access_token
from flask_login import login_user, logout_user, login_required


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
        
    return usuario.to_json(), 201



@auth.route("/login",methods=["POST"])
def login():
    usuario = db.session.query(UsuariosModel).filter(UsuariosModel.email == request.form.get("email")).first()

    if usuario == None or not usuario.validate_pass(request.form.get("password")):

        flash("Usuario o clave incorrecto")
        return redirect(url_for('menu.login_init'))
    
    else:
        access_token = create_access_token(identity=str(usuario.id))

        session['access_token'] = access_token

        data = {
            "id": str(usuario.id),
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "access_token": access_token,
            "role": usuario.role
        }

        session["data"] = data

        login_user(usuario)
        
        return redirect(url_for('menu.index'))

    
    

@auth.route('/logout',methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('menu.login_init'))
    

