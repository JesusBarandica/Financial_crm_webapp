###importamos os para manipular sistema operativo desde entorno de desarrollo con lineas de codigo en python
import os
###importamos flask para levantar nuestro servidor y poder recibir peticiones del usuario
from flask import Flask
###importamos dotenv para manipular nuestras variables de entorno, especificamente en este caso las cargaremos.
from dotenv import load_dotenv
###se importa SQLalchemy para crear base de dato desde entorno de desarrollo
from flask_sqlalchemy import SQLAlchemy
###se importa flask-restful para crear la api para las rutas de nuestros modelos
from flask_restful import Api
### se importa flask-jwtextends para crear los tokens y sesiones de usuario
from flask_jwt_extended import JWTManager
### para configurar el tiempo que dura la sesión
import datetime
### Se importa flask-login para administrar las autenticaciones a nuestra aplicación
from flask_login import LoginManager
### importamos modelo usuario para crear load_user


# instanciamos SQLAlchSQLAlchemyemy  para crear base datos.
db = SQLAlchemy()

#instanciamos nuestra api para crear rutas
api = Api()

#instanciamos el jwtmanager para agregarla a la app
jwt = JWTManager()

#instaciamos login-manager para manejar la autenticación de usuarios
login_manager = LoginManager()




def create_app():

    ###instanciamos Flask y le colocamos el __name__ para que reconozca nuestra aplicación y sus modulos
    app = Flask(__name__,
                template_folder="D:/CRM_FINANCIERO/frontend", 
                static_folder="D:/CRM_FINANCIERO/frontend/static")


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

    #import main.resources.Prospectos as ResourcesProspectos  
    import main.resources.Usuarios as ResourcesUsuarios

    #api.add_resource(ResourcesProspectos.Prospectos,"/prospectos")
    #api.add_resource(ResourcesProspectos.Prospecto,"/addprospecto")
    api.add_resource(ResourcesUsuarios.Usuario,"/usuario")

    api.init_app(app)

    #registro de blueprint  para recursos para modelo de prospectos
    from main.resources import Prospectos

    app.register_blueprint(Prospectos.Resource_prospectos)

    #registro de rutas de autenticación login y register
    from main.auth import routes

    #registro de blueprint auth que contiene las rutas de funciones login y register
    app.register_blueprint(routes.auth)


    #importamos el paquete que contiene los modulos para renderizar plantillas
    from main.route_templates import templates_html

    app.register_blueprint(templates_html.menu)

    
    
    app.config["SECRET_KEY"] = os.getenv("JWT_SECRET_KEY") 
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(seconds= int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))

    jwt.init_app(app)

    #inicializamos nuestro loginmanager para que nuestra app la reconosca.
    from main.models import UsuariosModel
    @login_manager.user_loader
    def load_user(user_id):
        return UsuariosModel.query.get(int(user_id))
    
    login_manager.login_view = "menu.login_init"
    login_manager.init_app(app)
    
    return app








