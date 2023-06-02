# Import Python packages and modules


# Import Flask packages and modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import project packages and modules
from .settings import config
from .api.v1 import resource as api_v1_resource
from .models.base import db
from .models.base import mg
from .api.v1 import schema as api_v1_schema


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    db.init_app(app)
    mg.init_app(app, db)
    api_v1_schema.ma.init_app(app)
    app.register_blueprint(api_v1_resource.api_v1_blp)
    return app
