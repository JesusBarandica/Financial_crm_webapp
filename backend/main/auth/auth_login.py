from .. import login_manager
from main.models import UsuariosModel


@login_manager.user_loader
def load_user(user_id):

    return UsuariosModel.query.get(int(user_id))

