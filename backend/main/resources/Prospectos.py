###Importamos el modulo  resource para crear los recursos de nuestra aplicación de las rutas del objeto cliente
from flask_restful import Resource
###importamos de flask jsonify para serializar objetos a formato json y request para poder recibir las peticiones del cliente
from flask import jsonify, request, Blueprint
###importamos la base de datos
from .. import db
###importamos modelo objetivo, en este caso prospecto models
from main.models import ProspectosModel

Resource_prospectos = Blueprint("Resource_prospectos", __name__)


@Resource_prospectos.route("/addprospecto", methods=["POST"])   
def addprospecto():
    prospecto = ProspectosModel.from_json(request.get_json())
    db.session.add(prospecto)
    db.session.commit()
    return 201 