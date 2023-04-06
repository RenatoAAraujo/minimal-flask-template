"""User admin endpoints"""
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from app.admin.users import user_admin_api, user_model
from app.admin.users.services.crud import (
    create_user,
    delete_user,
    get_users,
    update_user,
)
from app.admin.users.swagger.models import create_user_model, update_user_model
from app.services.exceptions.errors import (
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)
from app.services.exceptions.swagger.models import error_model
from app.services.requests.helpers import default_return, request_default_filters
from app.services.requests.intercept import intercept_admin_user

parser = user_admin_api.parser()
parser.add_argument("Authorization", location="headers")


@user_admin_api.param("hash_id", "User hash")
@user_admin_api.route("/<string:hash_id>")
@user_admin_api.expect(parser)
class User(Resource):
    """Single user route"""
    @jwt_required()
    @intercept_admin_user
    @user_admin_api.response(200, "Success", user_model)
    @user_admin_api.response(400, "Bad Request", error_model)
    @user_admin_api.response(401, "Unouthorized", error_model)
    @user_admin_api.response(404, "Not Found", error_model)
    @user_admin_api.response(500, "Something went wrong", error_model)
    def get(self, hash_id):
        """Get user"""
        try:
            item, items_paginate = get_users(user_hash_id=hash_id)

            return default_return(200, item, items_paginate)
        except (
            BadRequestError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))

    @jwt_required()
    @intercept_admin_user
    @user_admin_api.doc(body=update_user_model)
    @user_admin_api.response(200, "Success", user_model)
    @user_admin_api.response(400, "Bad Request", error_model)
    @user_admin_api.response(401, "Unouthorized", error_model)
    @user_admin_api.response(404, "Not Found", error_model)
    @user_admin_api.response(500, "Something went wrong", error_model)
    def put(self, hash_id):
        """Update user"""
        try:
            user_payload = request.get_json()
            item = update_user(user_payload, user_hash_id=hash_id)

            return default_return(200, item)
        except (
            BadRequestError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))

    @jwt_required()
    @intercept_admin_user
    @user_admin_api.response(200, "Success", user_model)
    @user_admin_api.response(400, "Bad Request", error_model)
    @user_admin_api.response(401, "Unouthorized", error_model)
    @user_admin_api.response(404, "Not Found", error_model)
    @user_admin_api.response(500, "Something went wrong", error_model)
    def delete(self, hash_id):
        """Delete user"""
        try:
            item = delete_user(user_hash_id=hash_id)

            return default_return(200, item)
        except (BadRequestError, InternalServerError, UnauthorizedError) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))


@user_admin_api.route("")
@user_admin_api.expect(parser)
class Users(Resource):
    """Users route"""
    @jwt_required()
    @intercept_admin_user
    @user_admin_api.response(200, "Success", [user_model])
    @user_admin_api.response(400, "Bad Request", error_model)
    @user_admin_api.response(401, "Unouthorized", error_model)
    @user_admin_api.response(404, "Not Found", error_model)
    @user_admin_api.response(500, "Something went wrong", error_model)
    def get(self):
        """Get users"""
        try:
            filters = request_default_filters()
            items, items_paginate = get_users(filters=filters)

            return default_return(200, items, items_paginate)
        except (
            BadRequestError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))

    @jwt_required()
    @intercept_admin_user
    @user_admin_api.doc(body=create_user_model)
    @user_admin_api.response(201, "Created", user_model)
    @user_admin_api.response(400, "Bad Request", error_model)
    @user_admin_api.response(401, "Unouthorized", error_model)
    @user_admin_api.response(404, "Not Found", error_model)
    @user_admin_api.response(500, "Something went wrong", error_model)
    def post(self):
        """Create user"""
        try:
            user_payload = request.get_json()
            item = create_user(user_payload, True)

            return default_return(201, item)
        except (
            BadRequestError,
            ConflictError,
            ConflictError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))
