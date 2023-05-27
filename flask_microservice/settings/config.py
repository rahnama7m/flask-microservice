import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# Class for import .env variables and use it for configuration of flask apps
class Config:
    TESTING = DEBUG = bool(int(os.environ.get("DEBUG", "0")))
    ENV = os.environ.get("ENVIRONMENT", "production")

    DATABASE_ENGINE = os.environ.get("DATABASE_ENGINE", None)
    DATABASE_NAME = os.environ.get("DATABASE_NAME", None)
    DATABASE_USER = os.environ.get("DATABASE_USER", None)
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", None)
    DATABASE_HOST = os.environ.get("DATABASE_HOST", None)
    DATABASE_PORT = os.environ.get("DATABASE_PORT", None)

    SQLALCHEMY_DATABASE_URI = f"{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
