from datetime import datetime

from flask_sqlalchemy import Model
from sqlalchemy import Column, DateTime, Integer


class BaseModel(Model):
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(DateTime)

    @classmethod
    def get_by_id(cls, record_id):
        return cls.query.get(int(record_id))
