# Import Python packages and modules


# Import Flask packages and modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime

# Import project packages and modules


db = SQLAlchemy()
mg = Migrate()


class BaseModel(db.Model):
    """description of class"""
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime(timezone=True), default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())
