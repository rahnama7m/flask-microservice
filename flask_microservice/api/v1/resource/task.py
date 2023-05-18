# Import Python packages and modules


# Import Flask packages and modules
from flask_restful import Resource


# Import project packages and modules
from flask_microservice.api.v1.controller.task import TaskController


class TaskResourceList(Resource):
    def get(self):
        """
        GET /api/v1/tasks --> List of tasks.
        """
        return TaskController.get_tasks()

    def post(self):
        """
        POST /api/v1/tasks --> Create a new task.
        """
        return TaskController.create_task()


class TaskResourceDetail(Resource):
    def get(self, task_id):
        """
        GET /api/v1/tasks/<task_id> --> Get task info.
        """
        if task_id is None:
            return TaskController.get_tasks()
        else:
            return TaskController.get_task(task_id)

    def patch(self, task_id):
        """
        PATCH /api/v1/tasks/<task_id> --> Update task.
        """
        return TaskController.update_task(task_id)

    def delete(self, task_id):
        """
        DELETE /api/v1/tasks/<task_id> --> Delete task.
        """
        return TaskController.delete_task(task_id)
