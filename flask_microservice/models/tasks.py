from .base import BaseModel
from sqlalchemy import Column, Integer, DateTime, String, Text, null


class Task(BaseModel):
    __tablename__ = 'Task'

    # uid
    title = Column(String(1024), index=True, nullable=False)
    code = Column(Text, nullable=False)

    name_space = Column(String(1024), index=True, nullable=False)
    runtime = Column(String(128), nullable=True)
    image = Column(String(1024), nullable=True)

    result_text = Column(Text, nullable=True)
    status = Column(String(128), nullable=False)

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, code={self.code})"
