# IMPORTS
from flask import request
from flask_cors import cross_origin

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
        @cross_origin()
        @app.validate('user', 'data')
        def set_user():
            # AGREGAR USUARIOS
            return self.user_service.set_data(request.json)

        @app.route('/user/<username>', methods=['GET'])
        @cross_origin()
        def get_user(username):
            # LEER USUARIOS
            return self.user_service.get_data(username)

        @app.route('/user/<username>', methods=['PUT'])
        @cross_origin()
        @app.validate('user', 'data')
        def put_user(username):
            # ACTUALIZAR USUARIOS
            return self.user_service.put_data(username, request.json)

        @app.route('/user/<username>', methods=['DELETE'])
        @cross_origin()
        def delete_user(username):
            # BORRAR USUARIOS
            return self.user_service.delete_data(username)

        @app.route('/forgot/<username>', methods=['GET'])
        @cross_origin()
        def get_user_password(username):
            # RECUPERAR USUARIO
            return self.user_service.get_password(username)
