from flask import Blueprint, render_template, session
from main.models import Aliados_comercialesModel, VendedoresModel, ProspectosModel
from sqlalchemy import column
from datetime import datetime
from .. import db
from flask_sqlalchemy import pagination



menu = Blueprint("menu",__name__)


@menu.route("/")
def login_init():
    return render_template('views/login.html')


@menu.route("/homepage")
def index():
    data = session.get("data")
    print(data["id"])
    type(data["id"])
    return render_template('index.html', data=data)


@menu.route("/prospectar")
def prospectar():
    data = session.get("data")
    concesionarios = Aliados_comercialesModel.query.with_entities(Aliados_comercialesModel.id, Aliados_comercialesModel.aliado).all()
    list_vendedores = VendedoresModel.query.with_entities(VendedoresModel.id, VendedoresModel.nombres, VendedoresModel.apellidos).all()
    return render_template('views/prospectar.html', list_vendedores=list_vendedores, concesionarios=concesionarios, data=data)


@menu.route("/portafolio")
def portafolio():

    data = session.get("data")
    ejecutivo_session = int(data["id"])
    prospectos_ejecutivo = ProspectosModel.query.filter(ProspectosModel.ejecutivo
                           == ejecutivo_session).with_entities(
                           db.func.DATE(ProspectosModel.fecha_prospeccion).label('fecha_prospecto'),
                           ProspectosModel.identificacion,
                           ProspectosModel.nombre,
                           ProspectosModel.primer_apellido,
                           ProspectosModel.segundo_apellido,
                           ProspectosModel.perfil,
                           ProspectosModel.celular,
                           ).all()
    
    return render_template('views/portafolio.html',data=data, prospectos_ejecutivo=prospectos_ejecutivo)