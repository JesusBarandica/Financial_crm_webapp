from .. import db
import datetime as dt

class Usuarios(db.Model):
    
    fecha_registro = db.Column(db.DateTime,default=dt.datetime.now(),nullable=False) 
    id = db.Column(db.Integer,primary_key=True,autoincrement=True, nullable=False, unique=True)
    nombre = db.Column(db.String(50),nullable=False)
    apellido = db.Column(db.String(30),nullable=False)
    seg_apellido = db.Column(db.String(30),nullable=False)
    celular = db.Column(db.String(15),nullable=False)
    email = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f"Usuarios {Usuarios.nombre}"