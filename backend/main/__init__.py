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


    #configuración base de datos

    ###traemos variables de entorno y las instanciamos
    PATH = os.getenv("PATH_DATABASE")
    NAME_DB = os.getenv("NAME_DATABASE")
    ### creamos un condicional para verificar si la base de datos existen en esta ruta.
    ### utilizamos os.path.exits para verificar si ruta existe
    if not os.path.exists(f"{PATH}{NAME_DB}"):
    ### si la ruta no existe nos dirigimos a la ruta
        os.chdir(f"{PATH}")
    ### creamos base de datos con el sistema operativo
        file = os.open(f"{NAME_DB}", os.O_CREAT )

    ###ya con nuestra base de datos creada, configuramos nuestra aplicación
    ###desahabilitamos los commit automaticos para nuestra aplicación
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    ###habilitamos para que nuestra aplicación se conecte a nuestra db en la ruta especificada.
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{PATH}{NAME_DB}"
    ### inicializamos las configuración que hicimos a nuestra base de datos y las aplicamos
    db.init_app(app)

    
    return app








