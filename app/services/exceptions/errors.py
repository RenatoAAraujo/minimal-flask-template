"""Custom error classes"""
import logging
from http import HTTPStatus

import sqlalchemy
import werkzeug
from flask import jsonify
from werkzeug.exceptions import MethodNotAllowed

from app import jwt
from app.services.exceptions import exception_handler_bp

logger = logging.getLogger(__name__)


class BadRequestError(Exception):
    """Exception raised for status 400 (Bad Request)."""

    def __init__(self, message="Bad Request"):
        self.status_code = HTTPStatus.BAD_REQUEST
        self.message = message
        super().__init__(self.message)


class UnauthorizedError(Exception):
    """Exception raised for status 401 (Unauthorized)."""

    def __init__(self, message="Unauthorized"):
        self.status_code = HTTPStatus.UNAUTHORIZED
        self.message = message
        super().__init__(self.message)


class ForbiddenError(Exception):
    """Exception raised for status 403 (Forbidden)."""

    def __init__(self, message="Forbidden"):
        self.status_code = HTTPStatus.FORBIDDEN
        self.message = message
        super().__init__(self.message)


class NotFoundError(Exception):
    """Exception raised for status 404 (Not Found)."""

    def __init__(self, message="Not Found"):
        self.status_code = HTTPStatus.NOT_FOUND
        self.message = message
        super().__init__(self.message)


class ConflictError(Exception):
    """Exception raised for status 409 (Conflict)."""

    def __init__(self, message="Conflict"):
        self.status_code = HTTPStatus.CONFLICT
        self.message = message
        super().__init__(self.message)


class InternalServerError(Exception):
    """Exception raised for status 500 (Internal Server Error)."""

    def __init__(self, message="Something went wrong"):
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        self.message = message
        super().__init__(self.message)


class GenerateError(Exception):
    def __init__(self, error, status_code):
        self.message = error
        self.status_code_code = status_code
        super().__init__(self)


@exception_handler_bp.app_errorhandler(GenerateError)
def generate_exception(e):
    logger.exception(e)
    response = jsonify({"status": e.status_code, "msg": e.error})
    response.status_code = e.status_code

    return response


@exception_handler_bp.app_errorhandler(MethodNotAllowed)
def method_exception(e):
    logger.exception(e)
    response = jsonify(
        {"status": HTTPStatus.METHOD_NOT_ALLOWED, "msg": "Method not Allowed"}
    )
    response.status_code = HTTPStatus.METHOD_NOT_ALLOWED

    return response


@exception_handler_bp.app_errorhandler(sqlalchemy.exc.InternalError)
def sql_error(e):
    logger.exception(e)
    response = jsonify(
        {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "msg": "SQL Error: {}".format(e.orig.args[1]),
        }
    )
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    return response


# @exception_handler_bp.app_errorhandler(Exception)
# def _exception(e):
#     logger.exception(e)
#     response = jsonify(
#         {
#             "status": HTTPStatus.INTERNAL_SERVER_ERROR,
#             "msg": "Unexpected error"
#         })
#     response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
#     return response


@exception_handler_bp.app_errorhandler(KeyError)
def _key_error(e):
    logger.exception(e)
    response = jsonify(
        {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "msg": "Internal error! Field not found: {}".format(e),
        }
    )
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return response


@exception_handler_bp.app_errorhandler(NameError)
def _name_error(e):
    logger.exception(e)
    response = jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "msg": e.args[0]})
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return response


@exception_handler_bp.app_errorhandler(werkzeug.exceptions.BadRequest)
def bad_request(e):
    logger.exception(e)
    response = jsonify({"status": HTTPStatus.BAD_REQUEST, "msg": "Bad request"})
    response.status_code = HTTPStatus.BAD_REQUEST
    return response


@exception_handler_bp.app_errorhandler(werkzeug.exceptions.NotFound)
def bad_request(e):
    logger.exception(e)
    response = jsonify({"status": HTTPStatus.NOT_FOUND, "msg": "Bad request"})
    response.status_code = HTTPStatus.NOT_FOUND
    return response


@jwt.invalid_token_loader
def _expired_token_callbacks(c):
    return jsonify({"status": 422, "msg": f"Unidentified Token"}), 422


@jwt.unauthorized_loader
def _expired_token_callback(c):
    return jsonify({"status": 401, "msg": f"Token not sent"}), 401
