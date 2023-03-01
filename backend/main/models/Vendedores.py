from .. import db

class Vendedores(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    concesionario = db.Column(db.Integer, db.ForeignKey("aliados_comerciales.id"), nullable=False)
    cedula = db.Column(db.String(15), nullable=False, unique=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    
    def __repr__(self) -> str:
        return super().__repr__()