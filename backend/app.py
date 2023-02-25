###importamos nuestra aplicación
from main import create_app
### importamos os para manejar variables de entorno con el sistema de operativo desde script
import os
###importamos nuestra base de datos
from main import db


###se instancia nuestra aplicación
app = create_app()

###por medio del metodo app_context accedemos a nuestra aplicación y variables de configuración y por medio del metodo
###push activamos las variables relevantes del contexto para accederlas en el momento adecuado, ejemplo nuestra db.
app.app_context().push()

###determinamos que nuestro modulo se ejecute como programa principal y ejecute las siguientes sentecias.
### se cree db y corra nuestro servidor en el puerto indicado en nuestro entorno.
if __name__ == "__main__":
    ###creamos los modelos de la db
    db.create_all()
    ###corremos nuestra aplicación  en el puerto indicado.
    app.run(port= os.getenv("PORT"), debug=True)