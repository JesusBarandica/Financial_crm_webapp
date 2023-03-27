from flask import Blueprint, render_template
from main.models import Aliados_comercialesModel, VendedoresModel



menu = Blueprint("menu",__name__)


@menu.route("/")
def login_init():
    return render_template('views/login.html')


@menu.route("/homepage")
def index():
    return render_template('index.html')


@menu.route("/prospectar")
def prospectar():
    concesionarios = Aliados_comercialesModel.query.with_entities(Aliados_comercialesModel.id, Aliados_comercialesModel.aliado).all()
    list_vendedores = VendedoresModel.query.with_entities(VendedoresModel.id, VendedoresModel.nombres, VendedoresModel.apellidos).all()
    return render_template('views/prospectar.html', list_vendedores=list_vendedores, concesionarios=concesionarios)


