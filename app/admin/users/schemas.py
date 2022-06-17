"""User Schemas"""
from marshmallow import fields

from app import ma
from app.admin.group.schemas import GroupSchema


class UserSchema(ma.Schema):
    """User Schema"""

    id = fields.Int()
    hash_id = fields.String()
    name = fields.String()
    email = fields.String()
    email_verified = fields.Boolean()
    token_update = fields.String()
    taxpayer_id = fields.String()
    cell_phone = fields.String()
    genre = fields.String()
    image_key = fields.String()
    status = fields.Boolean()
    group_id = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()

    group = fields.Nested(GroupSchema)

    class Meta:
        """Schema meta class"""

        ordered = True
