from .. import db

class Estado(db.Model):

    id = db.Column(db.Integer, primary_key= True, autoincrement=True, nullable=False, unique=True )
    nombre_estado = db.Column(db.String(10),unique=False)

    _static_cache_key = "Estado"

    def __repr__(self) :
        return Estado.__repr__()