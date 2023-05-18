"""
# Flask Microservice Project-  API Version 1
## Architecture
In this project we use MVC architecture. Components of each section are:
    1. Model: In root of application represented by models/app_models.py
    2. View: In each version of project (Exp: api/v1),  represented by resource.py
    3. Controller: In each version of project (Exp: api/v1), represented by controller.py

"""
from .microservice import create_app
