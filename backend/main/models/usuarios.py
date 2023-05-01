from .. import db
import datetime as dt
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class Usuarios(UserMixin, db.Model):
    
    fecha_registro = db.Column(db.DateTime,default=dt.datetime.now(),nullable=False) 
    id = db.Column(db.Integer,primary_key=True,autoincrement=True, nullable=False, unique=True)
    nombre = db.Column(db.String(50),nullable=False)
    apellido = db.Column(db.String(30),nullable=False)
    seg_apellido = db.Column(db.String(30),nullable=False)
    celular = db.Column(db.String(15),nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    role = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(100),nullable=False)

    _static_cache_key = "Usuarios"

    def __repr__(self):
        return Usuarios.__repr__()
    
    @property
    def plain_password(self):
        raise AttributeError("the password dont be read")
    
    @plain_password.setter
    def plain_password(self,password):
        self.password = generate_password_hash(password)
    
    def validate_pass(self,password):
        return check_password_hash(self.password,password)

    def get_id(self):
        return str(self.id)


    def to_json(self):
        usuario = {
            "fecha_registro" : str(self.fecha_registro),
            "nombre": self.nombre,
            "apellido": self.apellido,
            "seg_apellido": self.seg_apellido,
            "celular": self.celular,
            "email": self.email,
            "role": self.role,
        }
        return usuario

    @staticmethod
    def from_json(usuario_json):

        fecha_registro = usuario_json.get("fecha_registro")
        id = usuario_json.get("id")
        nombre = usuario_json.get("nombre")
        apellido = usuario_json.get("apellido")
        seg_apellido = usuario_json.get("seg_apellido")
        celular = usuario_json.get("celular")
        email = usuario_json.get("email")
        role = usuario_json.get("role")
        password = usuario_json.get("password")

        return Usuarios(
            fecha_registro = fecha_registro,
            id = id,
            nombre = nombre,
            apellido = apellido,
            seg_apellido = seg_apellido,
            celular = celular,
            email = email,
            role = role,
            plain_password = password
        )