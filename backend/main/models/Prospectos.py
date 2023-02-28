from .. import db
import datetime as dt

class Prospectos(db.Model):
    
    fecha_prospeccion = db.Column(db.DateTime,default=dt.datetime.now(), nullable=False)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    Concesionario_aliado = db.Column(db.Integer,db.ForeignKey("aliados_comerciales.id"),nullable=False)
    ejecutivo = db.Column(db.Integer,db.ForeignKey("usuario.id"),nullable=False)
    tipo_identi = db.Column(db.SmallInteger, db.ForeignKey("tipo_documento.id"),nullable=False)
    identificacion = db.Column(db.Integer,nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    segundo_nombre = db.Column(db.String(50), nullable=False)
    primer_apellido = db.Column(db.String(50), nullable=False)
    segundo_apellido = db.Column(db.String(50), nullable=False)
    celular = db.Column(db.String(15),nullable=False)
    email = db.Column(db.String(150), nullable=False)
    perfil = db.Column(db.String(25), db.ForeignKey("perfiles.id"), nullable=False)
    vendedor = db.Column(db.Integer, db.ForeignKey("vendedores.id"), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()