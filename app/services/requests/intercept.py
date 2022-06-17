"""JWT interception annotations"""
from functools import wraps

from flask_jwt_extended import get_jwt_identity

from app.services.exceptions.errors import UnauthorizedError


def intercept_admin_user(f):
    """Bar client credentials"""

    @wraps(f)
    def wrap(*args, **kwargs):
        jwt_group_id = get_jwt_identity()["group_id"]

        if jwt_group_id == 5:
            raise UnauthorizedError("User Unauthorized!")

        return f(*args, **kwargs)

    return wrap


def intercept_system_user(f):
    """Allow only system credentials"""

    @wraps(f)
    def wrap(*args, **kwargs):
        jwt_group_id = get_jwt_identity()["group_id"]

        if jwt_group_id != 1:
            raise UnauthorizedError("User Unauthorized!")

        return f(*args, **kwargs)

    return wrap
