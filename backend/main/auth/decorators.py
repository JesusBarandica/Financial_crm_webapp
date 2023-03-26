from .. import jwt
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def required_role(roles):
    def decorator(function):
        def wrapper(*args, **kwargs):
            ###verificar jwt sea correcto
            verify_jwt_in_request()

            #obtenemos peticiones dentro del jwt
            claims = get_jwt()

            if claims["role"] in roles:
                return function(*args, **kwargs)
            else:
                return "roll not allowed", 403
            
        return wrapper
    return decorator


@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return {
        "usuarioId": usuario.id,
        "role": usuario.role
    }

@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        "id" : usuario.id,
        "role": usuario.role,
        "nombre": usuario.nombre,
    }

