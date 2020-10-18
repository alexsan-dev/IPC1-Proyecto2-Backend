# IMPORTS
import json
import os

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
        print(user)
        
        # OUTPUT
        return "Usuario agregado exitosamente"
