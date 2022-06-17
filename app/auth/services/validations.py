"""Authenticcation validations"""
from app.admin.users.models import User
from app.services.exceptions.errors import BadRequestError


def _validate_data(data: dict):
    assert isinstance(data, dict), '"data" must be a dict'

    if not data.get("username"):
        raise BadRequestError("Missing username parameter")
    if not data.get("password"):
        raise BadRequestError("Missing password parameter")


def validate_token(params: dict):
    """Validate user token"""
    assert isinstance(params, dict), '"data" must be a dict'

    _validate_data(params)

    user = User.query.filter(User.deleted_at == None, User.status == 1)

    if "@" in params["username"]:
        user = user.filter(User.email == params["username"])
    else:
        user = user.filter(User.cpf == params["username"])

    user = user.first()

    return user, params["password"]
