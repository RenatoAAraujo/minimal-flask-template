"""Group endpoints"""
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from app.admin.group import group_api
from app.admin.group.services.crud import (
    create_group,
    delete_group,
    get_group,
    get_groups,
    update_group,
)
from app.admin.group.swagger.models import (
    create_group_model,
    group_model,
    update_group_model,
)
from app.services.exceptions.errors import (
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)
from app.services.exceptions.swagger.models import error_model
from app.services.requests.helpers import default_return
from app.services.requests.intercept import intercept_admin_user

parser = group_api.parser()
parser.add_argument("Authorization", location="headers")


@group_api.param("group_id", "Group ID")
@group_api.route("/<int:group_id>")
@group_api.expect(parser)
class Group(Resource):
    """Single group route"""
    @jwt_required()
    @intercept_admin_user
    @group_api.response(200, "Success", group_model)
    @group_api.response(400, "Bad Request", error_model)
    @group_api.response(401, "Unouthorized", error_model)
    @group_api.response(404, "Not Found", error_model)
    @group_api.response(500, "Something went wrong", error_model)
    def get(self, group_id):
        """Get group"""
        try:
            item = get_group(group_id, True)

            return default_return(200, item)
        except (
            BadRequestError,
            ConflictError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))

    @jwt_required()
    @intercept_admin_user
    @group_api.doc(body=update_group_model)
    @group_api.response(200, "Success", group_model)
    @group_api.response(400, "Bad Request", error_model)
    @group_api.response(401, "Unouthorized", error_model)
    @group_api.response(404, "Not Found", error_model)
    @group_api.response(500, "Something went wrong", error_model)
    def put(self, group_id):
        """Update group"""
        try:
            item = update_group(group_id, True)

            return default_return(200, item)
        except (
            BadRequestError,
            ConflictError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))

    @jwt_required()
    @intercept_admin_user
    @group_api.response(200, "Success", group_model)
    @group_api.response(400, "Bad Request", error_model)
    @group_api.response(401, "Unouthorized", error_model)
    @group_api.response(404, "Not Found", error_model)
    @group_api.response(500, "Something went wrong", error_model)
    def delete(self, group_id):
        """Delete group"""
        try:
            item = delete_group(group_id)

            return default_return(200, item)
        except (
            BadRequestError,
            ConflictError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))


@group_api.route("")
@group_api.expect(parser)
class Groups(Resource):
    """Groups route"""
    @jwt_required()
    @intercept_admin_user
    @group_api.response(200, "Success", [group_model])
    @group_api.response(400, "Bad Request", error_model)
    @group_api.response(401, "Unouthorized", error_model)
    @group_api.response(404, "Not Found", error_model)
    @group_api.response(500, "Something went wrong", error_model)
    def get(self):
        """Get groups"""
        try:
            items, items_paginate = get_groups(True)

            return default_return(200, items, items_paginate)
        except (
            BadRequestError,
            ConflictError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))

    @jwt_required()
    @intercept_admin_user
    @group_api.doc(body=create_group_model)
    @group_api.response(201, "Created", create_group_model)
    @group_api.response(400, "Bad Request", error_model)
    @group_api.response(401, "Unouthorized", error_model)
    @group_api.response(404, "Not Found", error_model)
    @group_api.response(500, "Something went wrong", error_model)
    def post(self):
        """Create group"""
        try:
            item = create_group(schema=True)

            return default_return(201, item)
        except (
            BadRequestError,
            ConflictError,
            InternalServerError,
            NotFoundError,
            UnauthorizedError,
        ) as e:
            return default_return(e.status_code, e.message)
        except Exception as e:
            return default_return(500, str(e))
