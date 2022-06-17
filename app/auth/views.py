"""Auth endpoints"""
from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required

from app import jwt
from app.auth import auth_bp
from app.auth.models import JWTTokenBlocklist
from app.auth.schemas import JWTTokenBlocklistSchema
from app.auth.services.token import generate_user_jwt
from app.auth.services.users import select_user_by_jwt
from app.auth.services.validations import validate_token
from app.services.exceptions.errors import (
    BadRequestError,
    InternalServerError,
    MethodNotAllowedError,
    NotFoundError,
    UnauthorizedError,
)
from app.services.requests.helpers import default_return


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):  # pylint: disable=unused-argument
    """Check if token in the blocklist"""
    jti = jwt_payload["jti"]
    token = JWTTokenBlocklist.query.filter(
        JWTTokenBlocklist.deleted_at == None, JWTTokenBlocklist.jti == jti
    ).first()

    return token


@auth_bp.route("/login")
def _login():
    """Login user"""
    try:
        if request.method == "POST":

            dict_body = request.get_json()

            user, password = validate_token(dict_body)

            if user and user.check_password(password):
                token_dict = generate_user_jwt(user)

                return make_response(make_response(jsonify(token_dict), 201))

            raise UnauthorizedError("Incorrect username or password")

        raise MethodNotAllowedError()
    except (
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        UnauthorizedError,
    ) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))


@auth_bp.route("/refresh")
@jwt_required(refresh=True)
def _refresh():
    """Refresh token"""
    try:
        if request.method == "POST":
            user_jwt = get_jwt_identity()

            user = select_user_by_jwt(user_jwt)

            if user:
                token = generate_user_jwt(user)

                return make_response(jsonify(token), 200)

            raise UnauthorizedError("User Unauthorized!")

        raise MethodNotAllowedError()
    except (
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        UnauthorizedError,
    ) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))


@auth_bp.route("/logout")
@jwt_required()
def _logout():
    """Logout user"""
    try:
        if request.method == "DELETE":
            jti = get_jwt()["jti"]

            token = JWTTokenBlocklist().create_item({"jti": jti}).save()

            return make_response(jsonify(JWTTokenBlocklistSchema().dump(token)), 200)

        raise MethodNotAllowedError()
    except (
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        UnauthorizedError,
    ) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))


@auth_bp.route("/protected")
@jwt_required()
def _protected():
    """Check JWT"""
    try:
        if request.method == "POST":
            return make_response(jsonify(hello="world"), 200)

        raise MethodNotAllowedError()
    except (
        BadRequestError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        UnauthorizedError,
    ) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))
