from .. import db
import datetime as dt
from flask import session

class Prospectos(db.Model):
    
    fecha_prospeccion = db.Column(db.DateTime, default= dt.datetime.now(), nullable=False)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    Concesionario_aliado = db.Column(db.Integer,db.ForeignKey("aliados_comerciales.id"),nullable=False)
    ejecutivo = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    tipo_identi = db.Column(db.SmallInteger, db.ForeignKey("tipo_documento.id"),nullable=False)
    identificacion = db.Column(db.Integer,nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    segundo_nombre = db.Column(db.String(50), nullable=False)
    primer_apellido = db.Column(db.String(50), nullable=False)
    segundo_apellido = db.Column(db.String(50), nullable=False)
    celular = db.Column(db.String(15),nullable=False)
    email = db.Column(db.String(150), nullable=False)
    perfil = db.Column(db.Integer, db.ForeignKey("perfiles.id"), nullable=False)
    vendedor = db.Column(db.Integer, db.ForeignKey("vendedores.id"), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()
    


    def to_json(self):
        prospecto = {
            "fecha_prospeccion" : str(self.fecha_prospeccion),
            "Concesionario_aliado": self.Concesionario_aliado,
            "ejecutivo": self.ejecutivo,
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "segundo_nombre": self.segundo_nombre,
            "primer_apellido": self.primer_apellido,
            "segundo_apellido": self.segundo_apellido,
            "celular": self.celular,
            "email": self.email,
            "perfil": self.perfil,
            "vendedor": self.vendedor
        }
        return prospecto

    @staticmethod
    def from_json(prospecto_json):

        fecha_prospeccion = str(prospecto_json.get("fecha_prospeccion"))
        id = int(prospecto_json.get("id"))
        Concesionario_aliado = int(prospecto_json.get("concesionario_aliado"))
        ejecutivo = int(session.get("data"))
        tipo_identi = int(prospecto_json.get("tipo_identi"))
        identificacion = str(prospecto_json.get("identificacion"))
        nombre = str(prospecto_json.get("nombre"))
        segundo_nombre = str(prospecto_json.get("segundo_nombre"))
        primer_apellido = str(prospecto_json.get("primer_apellido"))
        segundo_apellido = str(prospecto_json.get("segundo_apellido"))
        celular = str(prospecto_json.get("celular"))
        email = str(prospecto_json.get("email"))
        perfil = int(prospecto_json.get("perfil"))
        vendedor = int(prospecto_json.get("vendedor"))

        return Prospectos(
            fecha_prospeccion = fecha_prospeccion,
            id = id,
            Concesionario_aliado = Concesionario_aliado,
            ejecutivo = ejecutivo,
            tipo_identi = tipo_identi,
            identificacion = identificacion,
            nombre = nombre,
            segundo_nombre = segundo_nombre,
            primer_apellido = primer_apellido,
            segundo_apellido = segundo_apellido,
            celular = celular,
            email = email,
            perfil = perfil,
            vendedor = vendedor
        )



