"""Group Scheemas"""
from marshmallow import fields

from app import ma


class GroupSchema(ma.Schema):
    """Group schema"""

    id = fields.Int()
    name = fields.String()
    status = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()

    class Meta:
        """Schema meta class"""

        ordered = True
