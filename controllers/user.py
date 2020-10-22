# IMPORTS
from flask import request

# SERVICIOS
from services.user import user

# CONTROLADOR


class user_controller:
    # CONSTRUCTOR
    def __init__(self, app):
        self.user_service = user()
        self.set_routes(app)

    # RUTAS
    def set_routes(self, app):
        @app.route('/user', methods=['POST'])
        @app.validate('user', 'data')
        def set_user():
            # AGREGAR USUARIOS
            return self.user_service.set_data(request.json)

        @app.route('/user/<username>', methods=['GET'])
        def get_user(username):
            # LEER USUARIOS
            return self.user_service.get_data(username)

        @app.route('/user/<username>', methods=['PUT'])
        @app.validate('user', 'data')
        def put_user(username):
            # ACTUALIZAR USUARIOS
            return self.user_service.put_data(username, request.json)

        @app.route('/user/<username>', methods=['DELETE'])
        def delete_user(username):
            # BORRAR USUARIOS
            return self.user_service.delete_data(username)

        @app.route('/forgot/<username>', methods=['GET'])
        def get_user_password(username):
            # BORRAR USUARIOS
            return self.user_service.get_password(username)
