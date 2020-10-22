# IMPORTS
from flask import jsonify
import json
import os

# DATOS TEMPORALES
users = []

# CREAR USUARIO
class user:
    # CONSTRUCTOR
    def __init__(self):
        self.path = os.path.dirname(__file__)

    # RUTA RELATIVA
    def get_path(self, rel_path):
        return os.path.join(self.path, rel_path)

    # GUARDAR DATOS
    def set_data(self, user):
        # ESCRIBIR DATOS JSON
        users.append(user)
        return "Usuario agregado exitosamente."

    # LEER DATOS
    def get_data(self, username):
        # BUSCAR
        tmpUser = None
        for user in users:
            if(user['user_name'] == username):
                tmpUser = user
                
        # OUTPUT
        if(tmpUser):
            return jsonify(tmpUser)
        else:
            return "Usuario no encontrado."
