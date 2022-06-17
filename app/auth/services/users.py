"""Authtication user helpers"""
from app.admin.users.models import User


def select_user_by_jwt(user_jwt):
    """
    Get uer by JWT

    :param user_jwt: User's JWT dict
    """
    return User.query.filter(
        User.hash_id == user_jwt["hash_id"], User.status == 1, User.deleted_at == None
    ).first()
