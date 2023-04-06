"""Auth endpoints"""
from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from flask_restx import Resource

from app import jwt
from app.auth import auth_api
from app.auth.models import JWTTokenBlocklist
from app.auth.schemas import JWTTokenBlocklistSchema
from app.auth.services.token import generate_user_jwt
from app.auth.services.users import select_user_by_jwt
from app.auth.services.validations import validate_token
from app.auth.swagger.models import login_request, successful_login, successful_logout
from app.services.exceptions.errors import (
    BadRequestError,
    InternalServerError,
    UnauthorizedError,
)
from app.services.exceptions.swagger.models import error_model
from app.services.requests.helpers import default_return

parser = auth_api.parser()
parser.add_argument("Authorization", location="headers")


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    """Check if token in the blocklist"""
    jti = jwt_payload["jti"]
    token = JWTTokenBlocklist.query.filter(
        JWTTokenBlocklist.deleted_at == None, JWTTokenBlocklist.jti == jti
    ).first()

    return token


@auth_api.route("/login")
class Login(Resource):
    """Login user"""
    @auth_api.doc(body=login_request)
    @auth_api.response(201, "Created", successful_login)
    @auth_api.response(400, "Bad Request", error_model)
    @auth_api.response(401, "Unouthorized", error_model)
    @auth_api.response(500, "Something went wrong", error_model)
    def post(self):
        """Try to login"""
        try:
            dict_body = request.get_json()

            user, password = validate_token(dict_body)

            if user and user.check_password(password):
                token_dict = generate_user_jwt(user)

                return make_response(make_response(jsonify(token_dict), 201))
            else:
                raise UnauthorizedError("Incorrect username or password")
        except (BadRequestError, InternalServerError, UnauthorizedError) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))


@auth_api.route("/refresh")
@auth_api.expect(parser)
class Refresh(Resource):
    """Refresh token"""
    @jwt_required(refresh=True)
    @auth_api.response(200, "Successs", successful_login)
    @auth_api.response(400, "Bad Request", error_model)
    @auth_api.response(401, "Unouthorized", error_model)
    @auth_api.response(500, "Something went wrong", error_model)
    def post(self):
        """Try to refresh user token"""
        try:
            user_jwt = get_jwt_identity()

            user = select_user_by_jwt(user_jwt)

            if user:
                token = generate_user_jwt(user)

                return make_response(jsonify(token), 200)
            else:
                raise UnauthorizedError("User Unauthorized!")
        except (BadRequestError, InternalServerError, UnauthorizedError) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))


@auth_api.route("/logout")
@auth_api.expect(parser)
class Logout(Resource):
    """Logout user"""
    @jwt_required()
    @auth_api.response(200, "Sucess", successful_logout)
    @auth_api.response(400, "Bad Request", error_model)
    @auth_api.response(401, "Unouthorized", error_model)
    @auth_api.response(500, "Something went wrong", error_model)
    def delete(self):
        """Try ti logout user"""
        try:
            jti = get_jwt()["jti"]

            token = JWTTokenBlocklist().create_item({"jti": jti}).save()

            return make_response(jsonify(JWTTokenBlocklistSchema().dump(token)), 200)
        except (BadRequestError, InternalServerError, UnauthorizedError) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))


@auth_api.route("/protected")
@auth_api.expect(parser)
class Protected(Resource):
    """Check JWT"""
    @jwt_required()
    @auth_api.response(200, "Sucess", successful_login)
    @auth_api.response(400, "Bad Request", error_model)
    @auth_api.response(401, "Unouthorized", error_model)
    @auth_api.response(500, "Something went wrong", error_model)
    def get(self):
        """JWT test"""
        try:
            return make_response(jsonify(hello="world"), 200)
        except (BadRequestError, InternalServerError, UnauthorizedError) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))
