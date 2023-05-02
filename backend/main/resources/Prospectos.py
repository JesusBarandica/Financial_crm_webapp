###Importamos el modulo  resource para crear los recursos de nuestra aplicación de las rutas del objeto cliente
from flask_restful import Resource
###importamos de flask jsonify para serializar objetos a formato json y request para poder recibir las peticiones del cliente
from flask import jsonify, request, Blueprint, session, redirect, url_for
###importamos la base de datos
from .. import db
###importamos modelo objetivo, en este caso prospecto models y Imagenes model
from main.models import ProspectosModel, ImagenesModel
###importamos os para guardar imagenes localmente
import os
### para subir archivos tipo fotos en el servidor
from werkzeug.utils import secure_filename
### datetime para manejo de fechas
import datetime as dt

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

        fecha_actual = dt.datetime.today()

        consultado = ProspectosModel.query.filter(db.extract("year", ProspectosModel.fecha_prospeccion) == fecha_actual.year).filter(
        db.extract("month", ProspectosModel.fecha_prospeccion) == fecha_actual.month).filter(ProspectosModel.identificacion == identificacion).first()

        print(consultado.nombre)

        if consultado == None:

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

                #se instancia ruta para guardar imagenes
                route_upload =  os.getenv("ROUTE_IMAGE_PROSPECTOS")

                cedula_file = request.files["cedula"]                                 #imagen de la cedula que se va a guardar
                name_cedula = secure_filename(request.files["cedula"].filename)       # se crea nombre de cedula seguro
                add_to_route_cedula = os.path.join(route_upload,name_cedula)          #se agrega a la ruta del servidor la imagen
                cedula_file.save(add_to_route_cedula)                                 # se guarda archivo en ruta del servidor



                consulta_file = request.files["consulta"]                             #imagen de la consulta que se va guardar
                name_consulta = secure_filename(request.files["consulta"].filename)   #nombre de la consulta
                add_to_route_consulta = os.path.join(route_upload,name_consulta)      #se agrega a la ruta del servidor la imagen
                consulta_file.save(add_to_route_consulta)                             # se guarda archivo en ruta del servidor

                id_prospecto = prospecto.id                                           #id para relacionarlo con el prospecto


                Imagenes = ImagenesModel(
                        id_prospecto = id_prospecto,
                        name_cedula = name_cedula,
                        route_cedula = add_to_route_cedula,
                        name_consulta = name_consulta,
                        route_consulta = add_to_route_consulta
                )

                db.session.add(Imagenes)
                db.session.commit()

                return redirect(url_for('menu.prospectar'))
        
        else:
                return "El prospecto ya fue consultado"
                
        