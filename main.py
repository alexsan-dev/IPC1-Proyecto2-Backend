# FLASK
from flask import Flask, request
from flask_jsonschema_validator import JSONSchemaValidator
from flask_cors import CORS, cross_origin

# CONTROLADORES
from controllers.user import user_controller
from controllers.login import login_controller

# APP
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})

# JSON VALIDATION
JSONSchemaValidator(app=app, root="models")

# CONTROLADORES
user_controller(app)
login_controller(app)

if __name__ == '__main__':
    app.run()
