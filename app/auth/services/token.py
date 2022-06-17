"""JWT token generation methods"""
from flask import current_app
from flask_jwt_extended import create_access_token, create_refresh_token


def generate_user_jwt(user):
    """
    Manage user's JWT token creation

    :param user: User ententy
    """
    user_jwt = {
        "hash_id": user.hash_id,
        "name": user.name,
        "group_id": user.group_id,
        "roles": ["USER_C", 2, 3],
    }

    access_token = create_access_token(identity=user_jwt)
    refresh_token = create_refresh_token(identity=user_jwt)

    data = {
        "token_type": "Bearer",
        "expires_in": current_app.config["JWT_EXPIRES"],
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

    return data
