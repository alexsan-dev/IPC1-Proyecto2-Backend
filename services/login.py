# IMPORTS
from services.user import users
from services.errors import errors

# CREAR USUARIO


class login:
    # BUSCADOR
    def find_user(self, username, password):
        # BUSCAR
        index = -1
        for i in range(len(users)):
            if users[i]['user_name'] == username and users[i][
                    'password'] == password:
                index = i

        # REMPLAZAR
        if index >= 0:
            return [users[index], index]
        else:
            return None

    # RUTA RELATIVA
    def login_user(self, username, password):
        # BUSCAR
        temp_user = self.find_user(username, password)

        # VALIDAR
        return errors[
            2] if temp_user == None else "Bienvenido de nuevo " + temp_user[0][
                'name'] + ' es un gusto verte de nuevo.'
