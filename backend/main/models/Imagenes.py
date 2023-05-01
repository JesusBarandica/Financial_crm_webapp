from .. import db

class Imagenes(db.Model):

    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    id_prospecto = db.Column(db.Integer,db.ForeignKey("prospectos.id"),nullable=False, unique=True)
    name_cedula = db.Column(db.String(255),nullable=False)
    imagen_cedula = db.Column(db.LargeBinary,nullable=False)
    name_consulta = db.Column(db.String(255),nullable=False)
    imagen_consulta = db.Column(db.LargeBinary,nullable=False)

    _static_cache_key = "Imagenes"

    def __repr__(self) :
        return Imagenes.__repr__()
    
    
