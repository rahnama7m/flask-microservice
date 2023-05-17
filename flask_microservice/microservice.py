# Import Python packages and modules


# Import Flask packages and modules
from flask import Flask

# Import project packages and modules
from .settings.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app
