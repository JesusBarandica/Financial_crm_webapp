from .. import db

class Vendedores(db.Model):

    id = db.column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    concesionario = db.column(db.Integer, db.ForeignKey("aliados_comerciales.id"), nullable=False)
    cedula = db.column(db.String(15), nullable=False, unique=True)
    nombres = db.column(db.String(50), nullable=False)
    apellidos = db.column(db.String(50), nullable=False)
    