# Import Python packages and modules


# Import Flask packages and modules


# Import project packages and modules
from flask_microservice.settings import config
from flask_microservice.settings import messages


def json_response_parser(state=None, metadata=None, status=200, internal_code=501, headers=None):
    if headers is None:
        headers = {}
    if metadata is None:
        metadata = {}
    if state is None:
        state = {}
    resource = {
        "result": state,
        "metadata": metadata,
        "status": {
            "code": internal_code,
            "message": messages.STATUS_MESSAGES.get(internal_code) if config.Config.DEBUG else None,
        }
    }
    return resource, status, headers
