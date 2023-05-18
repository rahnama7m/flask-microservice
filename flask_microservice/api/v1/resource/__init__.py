# Import Python packages and modules


# Import Flask packages and modules
from flask import Flask
from flask import Blueprint
from flask_restful import Api


# Import project packages and modules
from .task import *


api_v1_blp = Blueprint("api_v1_blp", __name__, url_prefix="/api/v1")
api_v1 = Api(api_v1_blp)

urls_path = [
    {"resource": TaskResourceList, "urls": "/tasks", "methods": ["GET", "POST"], "endpoint": "task_list"},
    {"resource": TaskResourceDetail, "urls": "/tasks/<task_id>", "methods": ["GET", "PATCH", "DELETE"], "endpoint": "task_detail"},
]

for url in urls_path:
    api_v1.add_resource(url["resource"], url["urls"], methods=url["methods"], endpoint=url["endpoint"])
