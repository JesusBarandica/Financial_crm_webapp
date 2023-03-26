###Importamos el modulo  resource para crear los recursos de nuestra aplicación de las rutas del objeto cliente
from flask_restful import Resource
###importamos de flask jsonify para serializar objetos a formato json y request para poder recibir las peticiones del cliente
from flask import jsonify, request 
###importamos la base de datos
from .. import db
###importamos modelo objetivo, en este caso prospecto models
from main.models import ProspectosModel

###se crea la subclase prospectos heredada de la clase Resource para crear las rutas de las peticiones especifica de nuestro
###modelo prospectos, se reuniran en esta clase las consultas masivas de este modelo, definiendo los roles.
class Prospectos(Resource):
    pass

###se crea la subclase prospecto heredada de la clase Resource para crear las rutas de las peticiones especifica de nuestro
###modelo prospecto, se reuniran las operaciones que se ejecutaran a cada cliente en particular.
class Prospecto(Resource):
    
    def post(self):

        prospecto = ProspectosModel.from_json(request.get_json())
        db.session.add(prospecto)
        db.session.commit()
        return prospecto.to_json(), 201 