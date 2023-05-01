from .. import db

class Perfiles(db.Model):
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    nombre_perfil = db.Column(db.String(25), nullable=False, unique=True)

    _static_cache_key = "Perfiles"

    def __repr__(self) :
        return Perfiles.__repr__()