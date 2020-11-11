# IMPORTS
from flask import jsonify
from services.errors import errors

apps_data = []


class apps:
    # BUSCAR APP
    def find_app(self, title):
        # BUSCAR
        index = -1
        for i in range(len(apps_data)):
            if apps_data[i]['title'] == title:
                index = i

        # REMPLAZAR
        if index >= 0:
            return [apps_data[index], index]
        else:
            return None

    # AGREGAR APPS
    def set_apps(self, apps_matrix):
        for app in apps_matrix:
            apps_data.append(app)
        return "Apps agregadas correctamente."

    # OBTENER APPS
    def get_apps(self):
        return jsonify({"apps": apps_data})

    # AGREGAR APP
    def set_app(self, app_data):
        apps_data.append(app_data)
        return "App agregada correctamente."

    # OBTENER APP
    def get_app(self, title):
        temp_app = self.find_app(title)

        # RETORNAR
        if temp_app:
            return jsonify(temp_app[0])
        else:
            return jsonify({"error": errors[3]})

    # ACTUALIZAR DATOS
    def put_app(self, title, app_data):
        # BUSCAR
        temp_app = self.find_app(title)

        # REMPLAZAR
        if temp_app:
            # BUSCAR
            local_app = self.find_app(app_data['title'])

            # REMPLAZAR
            if local_app == None or app_data['title'] == title:
                apps_data[temp_app[1]] = app_data
                return 'App actualizada exitosamente, recarga la pagina para ver los nuevos datos.'
            else:
                return errors[4]
        else:
            return errors[3]

    # BORRAR DATOS
    def delete_app(self, title):
        # BUSCAR
        temp_app = self.find_app(title)

        # REMPLAZAR
        if temp_app:
            del apps_data[temp_app[1]]
            return "Esta aplicación se ha eliminado permanentemente."
        else:
            return errors[3]