from .. import db

class Aliados_comerciales(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    nit = db.Column(db.Integer,unique=True,nullable=False)
    aliado = db.Column(db.String(150), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    celular = db.Column(db.String(15), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()