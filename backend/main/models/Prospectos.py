from .. import db
import datetime as dt
from flask import session, request

class Prospectos(db.Model):
    
    fecha_prospeccion = db.Column(db.DateTime, default= dt.datetime.now(), nullable=False)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False,unique=True)
    Concesionario_aliado = db.Column(db.Integer,db.ForeignKey("aliados_comerciales.id"),nullable=False)
    ejecutivo = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    tipo_identi = db.Column(db.SmallInteger, db.ForeignKey("tipo_documento.id"),nullable=False)
    identificacion = db.Column(db.Integer,nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    segundo_nombre = db.Column(db.String(50))
    primer_apellido = db.Column(db.String(50), nullable=False)
    segundo_apellido = db.Column(db.String(50))
    celular = db.Column(db.String(15),nullable=False)
    email = db.Column(db.String(150), nullable=False)
    perfil = db.Column(db.Integer, db.ForeignKey("perfiles.id"), nullable=False)
    vendedor = db.Column(db.Integer, db.ForeignKey("vendedores.id"), nullable=False)

    _static_cache_key = "Prospectos"

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
    def from_json(request):


        fecha_prospeccion = request.form.get("fecha_prospeccion")
        id = int(request.form.get("id"))
        Concesionario_aliado = int(request.form.get("concesionario_aliado"))
        ejecutivo = int(session.get("data"))
        tipo_identi = int(request.form.get("tipo_identi"))
        identificacion = int(request.form.get("identificacion"))
        nombre = str(request.form.get("nombre"))
        segundo_nombre = str(request.form.get("segundo_nombre"))
        primer_apellido = str(request.form.get("primer_apellido"))
        segundo_apellido = str(request.form.get("segundo_apellido"))
        celular = str(request.form.get("celular"))
        email = str(request.form.get("email"))
        perfil = int(request.form.get("perfil"))
        vendedor = int(request.form.get("vendedor"))

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



