###Importamos el modulo  resource para crear los recursos de nuestra aplicación de las rutas del objeto cliente
from flask_restful import Resource
###importamos de flask jsonify para serializar objetos a formato json y request para poder recibir las peticiones del cliente
from flask import jsonify, request, Blueprint, session, redirect, url_for
###importamos la base de datos
from .. import db
###importamos modelo objetivo, en este caso prospecto models
from main.models import ProspectosModel

Resource_prospectos = Blueprint("Resource_prospectos", __name__)


@Resource_prospectos.route("/addprospecto", methods=["POST"])   
def addprospecto():

        #datos para registrar prospecto
        Concesionario_aliado = int(request.form.get("concesionario_aliado"))
        ejecutivo = session.get("data")
        tipo_identi = int(request.form.get("tipo_identi"))
        identificacion = int(request.form.get("identificacion"))
        nombre = str(request.form.get("nombre"))
        segundo_nombre = str(request.form.get("segundo_nombre"))
        primer_apellido = str(request.form.get("primer_apellido"))
        segundo_apellido = str(request.form.get("segundo_apellido"))
        celular = str(request.form.get("celular"))
        email = str(request.form.get("email"))
        perfil = int(request.form.get("perfil"))
        vendedor = int(request.form.get("vendedor"))

        prospecto  =  ProspectosModel(
            Concesionario_aliado = Concesionario_aliado,
            ejecutivo = int(ejecutivo["id"]),
            tipo_identi = tipo_identi,
            identificacion = identificacion,
            nombre = nombre,
            segundo_nombre = segundo_nombre,
            primer_apellido = primer_apellido,
            segundo_apellido = segundo_apellido,
            celular = celular,
            email = email,
            perfil = perfil,
            vendedor = vendedor
        )

        db.session.add(prospecto)
        db.session.commit()

        #datos para registrar imagenes
        cedula_file = request.files["cedula"]
        consulta_file = request.files["consulta"]

        return redirect(url_for('menu.prospectar'))
        