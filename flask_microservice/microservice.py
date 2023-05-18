# Import Python packages and modules


# Import Flask packages and modules
from flask import Flask

# Import project packages and modules
from .settings import config
from .api.v1 import resource as api_v1_resource


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    app.register_blueprint(api_v1_resource.api_v1_blp)
    return app
