"""Auth Schemas"""
from marshmallow import fields

from app import ma


class JWTTokenBlocklistSchema(ma.Schema):
    """JWTTokenBLockList schema"""
    id = fields.Int()
    jti = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()

    class Meta:
        """Schema meta class"""
        ordered = True
