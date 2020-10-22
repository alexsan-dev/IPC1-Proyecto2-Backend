# IMPORTS
from services.user import users

# CREAR USUARIO


class login:
    # BUSCADOR
    def find_user(self, username, password):
        # BUSCAR
        index = -1
        for i in range(len(users)):
            if users[i]['user_name'] == username and users[i]['password'] == password:
                index = i

        # REMPLAZAR
        if index >= 0:
            return [users[index], index]
        else:
            return None

    # RUTA RELATIVA
    def login_user(self, username, password):
        # BUSCAR
        tmpUser = self.find_user(username, password)

        # VALIDAR
        return "Error" if tmpUser == None else "Ok"
