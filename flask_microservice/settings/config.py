import os


# Class for import .env variables and use it for configuration of flask apps
class Config:
    TESTING = DEBUG = bool(int(os.environ.get("DEBUG", "0")))
    ENV = os.environ.get("ENVIRONMENT", "production")
