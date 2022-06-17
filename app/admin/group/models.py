"""Group database models"""
from app import db
from database.base_model import BaseModel


class Group(db.Model, BaseModel):  # pylint: disable=inconsistent-mro
    """Group is table for grouping up user access and functions"""

    __tablename__ = "group"

    name = db.Column(db.String(256))
    status = db.Column(db.Boolean, default=1)

    def create_item(self, model_dict):
        """Create databse registry"""
        self.name = model_dict["name"]

        return self

    def update_item(self, model_dict):
        """Update databse registry"""
        self.name = model_dict.get("name", self.name)
        self.status = model_dict.get("status", self.status)

        return self
