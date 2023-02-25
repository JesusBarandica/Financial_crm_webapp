###Importamos el modulo  resource para crear los recursos de nuestra aplicación de las rutas del objeto cliente
from flask_restful import Resource
###importamos de flask jsonify para serializar objetos a formato json y request para poder recibir las peticiones del cliente
from flask import jsonify, request 

###se crea la subclase Clientes heredada de la clase Resource para crear las rutas de las peticiones especifica de nuestro
###modelo clientes, se reuniran en esta clase las consultas masivas de este modelo, definiendo los roles.
class Clientes(Resource):
    pass

###se crea la subclase cliente heredada de la clase Resource para crear las rutas de las peticiones especifica de nuestro
###modelo clientes, se reuniran las operaciones que se ejecutaran a cada cliente en particular.
class Cliente(Resource):
    pass