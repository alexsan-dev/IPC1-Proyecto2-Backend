# IMPORTS
from flask import jsonify
import json

# DATOS TEMPORALES
users = []

# CREAR USUARIO


class user:
    # BUSCADOR
    def find_user(self, username):
        # BUSCAR
        index = -1
        for i in range(len(users)):
            if users[i]['user_name'] == username:
                index = i

        # REMPLAZAR
        if index >= 0:
            return [users[index], index]
        else:
            return None

    # GUARDAR DATOS
    def set_data(self, user):
        # BUSCAR
        tmpUser = self.find_user(user['user_name'])

        # ESCRIBIR DATOS JSON
        if tmpUser == None:
            users.append(user)
            return "Usuario agregado exitosamente."
        else:
            return "Este username ya esta registrado."

    # LEER DATOS
    def get_data(self, username):
        # BUSCAR
        tmpUser = self.find_user(username)

        # OUTPUT
        if tmpUser:
            return jsonify(tmpUser[0])
        else:
            return "Usuario no encontrado."

    # ACTUALIZAR DATOS
    def put_data(self, username, user):
        # BUSCAR
        tmpUser = self.find_user(username)

        # REMPLAZAR
        if tmpUser:
            # BUSCAR
            localUser = self.find_user(user['user_name'])

            # REMPLAZAR
            if localUser == None and user['user_name'] != username:
                users[tmpUser[1]] = user
                return user
            else:
                return "Usuario no actualizado."
        else:
            return "Usuario no encontrado."

     # BORRAR DATOS
    def delete_data(self, username):
        # BUSCAR
        tmpUser = self.find_user(username)

        # REMPLAZAR
        if tmpUser:
            del users[tmpUser[1]]
            return "Usuario eliminado."
        else:
            return "Usuario no encontrado."
