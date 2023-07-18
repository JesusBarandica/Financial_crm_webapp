from .. import db

class Etapa(db.Model):

    id = db.Column(db.Integer, primary_key= True, autoincrement=True, nullable=False, unique=True )
    nombre_etapa = db.Column(db.String(10),unique=False)

    _static_cache_key = "Etapa"

    def __repr__(self) :
        return Etapa.__repr__()