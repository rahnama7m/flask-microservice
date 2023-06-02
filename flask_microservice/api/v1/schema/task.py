# Import Python packages and modules


# Import Flask packages and modules
from flask_marshmallow import Marshmallow

# Import project packages and modules
from flask_microservice.models import Task


ma = Marshmallow()


class TaskSchema(ma.SQLAlchemyAutoSchema):
    id = ma.auto_field(dump_only=True)
    created_date = ma.auto_field(dump_only=True)
    updated_date = ma.auto_field(dump_only=True)
    result_text = ma.auto_field(dump_only=True)
    status = ma.auto_field(dump_only=True)

    class Meta:
        model = Task
