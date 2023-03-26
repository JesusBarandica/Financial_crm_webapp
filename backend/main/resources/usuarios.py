###Importamos el modulo  resource para crear los recursos de nuestra aplicación de las rutas del objeto cliente
from flask_restful import Resource
###importamos de flask jsonify para serializar objetos a formato json y request para poder recibir las peticiones del cliente
from flask import jsonify, request
###importamos la base de datos usuarios
from .. import db
###importamos modelo objetivo
from main.models import UsuariosModel


###Creamos los recursos de la subclase Usuarios la cual es heredada de recursos, para manipular la base de datos, de los
###roles que se crearan en el sistema de manera masiva.
class Usuarios(Resource):
    pass

##Creamos los recursos de la subclase Usuarios la cual es heredada de recursos, para manipular datos de usuario de manera individual
class Usuario(Resource):
    
    def post(self):

        usuario = UsuariosModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
    