"""User admin endpoints"""
from flask import request
from flask_jwt_extended import jwt_required

from app.admin.users import user_admin_bp
from app.admin.users.services.crud import (
    create_user,
    delete_user,
    get_users,
    update_user,
)
from app.services.exceptions.errors import (
    BadRequestError,
    ConflictError,
    InternalServerError,
    MethodNotAllowedError,
    NotFoundError,
    UnauthorizedError,
)
from app.services.requests.helpers import default_return, request_default_filters
from app.services.requests.intercept import intercept_admin_user


@user_admin_bp.route("/<int:hash_id>")
@jwt_required()
@intercept_admin_user
def _user(hash_id):
    """Single user route"""
    try:
        if request.method == "GET":
            item, items_paginate = get_users(user_hash_id=hash_id)

            return default_return(200, item, items_paginate)
        if request.method == "PUT":
            user_payload = request.get_json()
            item = update_user(user_payload, user_hash_id=hash_id)

            return default_return(200, item)
        if request.method == "DELETE":
            item = delete_user(user_hash_id=hash_id)

            return default_return(200, item)

        raise MethodNotAllowedError()
    except (
        BadRequestError,
        ConflictError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        UnauthorizedError,
    ) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))


@user_admin_bp.route("/")
@jwt_required()
@intercept_admin_user
def _users():
    """Users route"""
    try:
        if request.method == "GET":
            filters = request_default_filters()
            items, items_paginate = get_users(filters=filters)

            return default_return(200, items, items_paginate)
        if request.method == "POST":
            user_payload = request.get_json()
            item = create_user(user_payload, True)

            return default_return(201, item)

        raise MethodNotAllowedError()
    except (
        BadRequestError,
        ConflictError,
        InternalServerError,
        MethodNotAllowedError,
        NotFoundError,
        UnauthorizedError,
    ) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))
