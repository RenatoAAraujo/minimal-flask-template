"""User database models"""
import uuid

from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app import db
from database.base_model import BaseModel


class User(db.Model, BaseModel):  # pylint: disable=inconsistent-mro
    """
    User table

    Credential levels:
    1 - System
    2 - Admin
    3 - Employee
    4 - Client
    """

    __tablename__ = "user"

    hash_id = db.Column(db.String(36), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    email_verified = db.Column(db.Boolean, default=0)
    password = db.Column(db.String(256), nullable=False)
    token_update = db.Column(db.String(36))
    taxpayer_id = db.Column(db.String(16), nullable=False, unique=True)
    cell_phone = db.Column(db.String(32))
    birth_date = db.Column(db.String(16), nullable=False)
    genre = db.Column(db.String(256))
    image_key = db.Column(db.String(256))
    status = db.Column(db.Boolean, default=1)

    group_id = db.Column(db.ForeignKey("group.id"), nullable=False)

    group = db.relationship("Group", backref="user", lazy=True, uselist=False)

    # def _get_image(self):
    #     return get_aws_image_keys_private(self.image_key)
    #
    # image = property(_get_image)

    def set_password(self, password):
        """Set user password"""
        self.password = pbkdf2_sha256.hash(password)

    def check_password(self, candidate):
        """Check user password"""
        return pbkdf2_sha256.verify(candidate, self.password)

    def create_item(self, model_dict):
        """Create database registry"""
        self.hash_id = str(uuid.uuid4())
        self.name = model_dict["name"]
        self.email = model_dict["email"]
        self.email_verified = model_dict.get("email_verified", 0)
        self.set_password(model_dict["password"])
        self.token_update = str(uuid.uuid4())
        self.taxpayer_id = model_dict["taxpayer_id"]
        self.cell_phone = model_dict.get("cell_phone", None)
        self.birth_date = model_dict["birth_date"]
        self.genre = model_dict.get("genre", None)
        self.status = model_dict.get("status", 1)
        self.group_id = model_dict.get("group_id", 4)

        return self

    def update_item(self, model_dict):
        """Update database registry"""
        try:
            self.set_password(model_dict["password"])
        except KeyError:
            pass
        self.name = model_dict.get("name", self.name)
        self.genre = model_dict.get("genre", self.genre)
        self.cell_phone = model_dict.get("cell_phone", self.cell_phone)
        self.birth_date = model_dict.get("birth_date", self.birth_date)
        self.status = model_dict.get("status", self.status)
        self.group_id = model_dict.get("group_id", self.group_id)

        return self
