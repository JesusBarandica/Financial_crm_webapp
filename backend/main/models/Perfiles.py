from .. import db

class Perfiles(db.Model):
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    nombre_perfil = db.Column(db.String(25), nullable=False, unique=True)

    def __repr__(self) :
        return Perfiles.__tablename__