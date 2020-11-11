# IMPORTS
from flask import request
from flask_cors import cross_origin

# SERVICIOS
from services.login import login

# CONTROLADOR


class login_controller:
    # CONSTRUCTOR
    def __init__(self, app):
        self.login_service = login()
        self.set_routes(app)

    # RUTAS
    def set_routes(self, app):
        @app.route('/login', methods=['POST'])
        @app.validate('user', 'login')
        @cross_origin()
        def login_user():
            # AGREGAR USUARIOS
            login_data = request.json
            return self.login_service.login_user(login_data['user_name'],
                                                 login_data['password'])
