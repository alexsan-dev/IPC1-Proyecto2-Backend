# IMPORTS
from flask import request
from flask_cors import cross_origin

# SERVICIOS
from services.apps import apps

# CONTROLADOR


class apps_controller:
    # CONSTRUCTOR
    def __init__(self, app):
        self.apps_service = apps()
        self.set_routes(app)

    # RUTAS
    def set_routes(self, app):
        # SUBIR APPS
        @app.route('/apps', methods=['POST'])
        @cross_origin()
        def upload_apps():
            # AGREGAR USUARIOS
            apps_data = request.json
            return self.apps_service.set_apps(apps_data['data'])

        # LEER APPS
        @app.route('/apps', methods=['GET'])
        @cross_origin()
        def get_apps():
            return self.apps_service.get_apps()

        # LEER APP
        @app.route('/apps/<app_title>', methods=['GET'])
        @cross_origin()
        def get_app(app_title):
            return self.apps_service.get_app(app_title)

        # AGREGAR APP
        @app.route('/apps', methods=['POST'])
        @app.validate('app', 'data')
        @cross_origin()
        def set_app():
            return self.apps_service.set_app(request.json)

        # ACTUALIZAR APP
        @app.route('/apps/<app_title>', methods=['PUT'])
        @cross_origin()
        def put_app(app_title):
            return self.apps_service.put_app(app_title, request.json)

        # BORRAR APP
        @app.route('/apps/<app_title>', methods=['DELETE'])
        @cross_origin()
        def delete_app(app_title):
            return self.apps_service.delete_app(app_title)