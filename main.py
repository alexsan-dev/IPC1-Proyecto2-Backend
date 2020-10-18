# FLASK
from flask import Flask
from flask_jsonschema_validator import JSONSchemaValidator

# CONTROLADORES
from controllers.user import user_controller

# APP
app = Flask(__name__)

# JSON VALIDATION
JSONSchemaValidator(app=app, root="models")

# CONTROLADORES
user_controller(app)

if __name__ == '__main__':
    app.run()
