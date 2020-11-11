# IMPORTS
from flask import jsonify
import json
from services.errors import errors

# CREAR USUARIO
admin_user = {
    "user_name": "admin",
    "name": "Usuario",
    "last_name": "Maestro",
    "type": "admin",
    "password": "admin"
}

# DATOS TEMPORALES
users = [admin_user]


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
        temp_user = self.find_user(user['user_name'])

        # ESCRIBIR DATOS JSON
        if temp_user == None:
            users.append(user)
            return "Gracias por registrarte tu usuario ha sido agregado exitosamente, puedes continuar a la tienda."
        else:
            return errors[1]

    # LEER DATOS
    def get_data(self, username):
        # BUSCAR
        temp_user = self.find_user(username)

        # OUTPUT
        if temp_user:
            return jsonify(temp_user[0])
        else:
            return jsonify({'error': errors[0]})

    # ACTUALIZAR DATOS
    def put_data(self, username, user):
        # BUSCAR
        temp_user = self.find_user(username)

        # REMPLAZAR
        if temp_user:
            # BUSCAR
            local_user = self.find_user(user['user_name'])

            # REMPLAZAR
            if local_user == None or user['user_name'] == username:
                users[temp_user[1]] = user
                return 'Usuario actualizado exitosamente, recarga la pagina para ver los nuevos datos.'
            else:
                return errors[1]
        else:
            return errors[0]

    # BORRAR DATOS
    def delete_data(self, username):
        # BUSCAR
        temp_user = self.find_user(username)

        # REMPLAZAR
        if temp_user:
            del users[temp_user[1]]
            return "La cuenta de este usuario se ha eliminado permanentemente."
        else:
            return errors[0]

    def get_password(self, username):
        # BUSCAR
        temp_user = self.find_user(username)

        # REMPLAZAR
        if temp_user:
            return "Tu contraseña es: " + "\"" + temp_user[0][
                "password"] + "\"" + " no la olvides."
        else:
            return errors[0]
