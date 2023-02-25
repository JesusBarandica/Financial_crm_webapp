###importamos os para manipular sistema operativo desde entorno de desarrollo con lineas de codigo en python
import os
###importamos flask para levantar nuestro servidor y poder recibir peticiones del usuario
from flask import Flask
###importamos dotenv para manipular nuestras variables de entorno, especificamente en este caso las cargaremos.
from dotenv import load_dotenv
###se importa SQLalchemy para crear base de dato desde entorno de desarrollo
from flask_sqlalchemy import SQLAlchemy

# instanciamos SQLAlchSQLAlchemyemy  para crear base datos.
db = SQLAlchemy()

def create_app():

    ###instanciamos Flask y le colocamos el __name__ para que reconozca nuestra aplicación y sus modulos
    app = Flask(__name__)

    ###cargamos variables de entorno para configurar nuestra app
    load_dotenv()


    return app








