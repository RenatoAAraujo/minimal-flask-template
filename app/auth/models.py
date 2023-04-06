"""Auth database models"""
from app import db
from database.base_model import BaseModel


class JWTTokenBlocklist(db.Model, BaseModel):  # pylint: disable=inconsistent-mro
    """JWTTokenBlocklist is a table for blocked JWT tokens"""
    __tablename__ = "jwt_token_blocklist"

    jti = db.Column(db.String(36), nullable=False)

    def create_item(self, model_dict):
        self.jti = model_dict["jti"]

        return self
