from .. import db

class Tipo_documento(db.Model):
    
    id = db.Column(db.SmallInteger,primary_key=True,autoincrement=True,nullable=False,unique=True)
    abreviatura = db.Column(db.String(2),nullable=False,unique=True)
    tipo_documen = db.Column(db.String(50),nullable=False,unique=True)

    _static_cache_key = "Tipo_documento"

    def __repr__(self) -> str:
        return super().__repr__()