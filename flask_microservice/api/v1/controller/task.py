# Import Python packages and modules


# Import Flask packages and modules

# Import project packages and modules
from flask_microservice.utils import json_response_parser
from flask_microservice.models.tasks import Task


class TaskController:

    @staticmethod
    def get_tasks():
        return json_response_parser(status=503, internal_code=501)

    @staticmethod
    def get_task(task_id):
        return json_response_parser(status=501, internal_code=501)

    @staticmethod
    def create_task():
        return json_response_parser(status=501, internal_code=501)

    @staticmethod
    def update_task(task_id):
        return json_response_parser(status=501, internal_code=501)

    @staticmethod
    def delete_task(task_id):
        return json_response_parser(status=501, internal_code=501)
