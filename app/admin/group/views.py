"""Group endpoints"""
from flask import request
from flask_jwt_extended import jwt_required


from app.admin.group import bp
from app.admin.group.services.crud import (
    create_group,
    delete_group,
    get_group,
    get_groups,
    update_group,
)
from app.services.exceptions.errors import (
    BadRequestError,
    ConflictError,
    InternalServerError,
    MethodNotAllowedError,
    NotFoundError,
    UnauthorizedError,
)
from app.services.requests.helpers import default_return
from app.services.requests.intercept import intercept_admin_user


@bp.route("/<int:group_id>")
@jwt_required()
@intercept_admin_user
def _group(group_id):
    """Single group route"""
    try:
        if request.method == "GET":
            item = get_group(group_id, True)

            return default_return(200, item)
        elif request.method == "PUT":
            item = update_group(group_id, True)

            return default_return(200, item)
        elif request.method == "DELETE":
            item = delete_group(group_id)

            return default_return(200, item)
        else:
            raise MethodNotAllowedError()            
    except (BadRequestError, ConflictError, InternalServerError, MethodNotAllowedError, NotFoundError, UnauthorizedError) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))


@bp.route("/")
@jwt_required()
@intercept_admin_user
def _groups(group_id):
    """Groups route"""
    try:
        if request.method == "GET":
            items, items_paginate = get_groups(True)

            return default_return(200, items, items_paginate)
        elif request.method == "POST":
            item = create_group(schema=True)

            return default_return(201, item)
        else:
            raise MethodNotAllowedError()            
    except (BadRequestError, ConflictError, InternalServerError, MethodNotAllowedError, NotFoundError, UnauthorizedError) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))
