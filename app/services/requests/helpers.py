"""Requests helper methods"""
from flask import jsonify, make_response, request

from app.services.exceptions.errors import InternalServerError


def default_return(status: int, data: (dict, str) = None, pagination_info: dict = None):
    """
    Default request reponse method

    :param status:  status code (int)
    :param data: reponse data (dict, str)
    :param pagination_info: query pagination info (dict)
    """
    if data:
        assert isinstance(
            data, (dict, str, list)
        ), '"data" must be a dict, list or a string'
    if pagination_info:
        assert isinstance(pagination_info, dict), '"pagination_info" must be a dict'

    return make_response(
        jsonify({"pagination_info": pagination_info, "data": data}),
        get_request_status_code(status),
    )


def get_request_status_code(status):  # pylint: disable=too-many-branches, too-many-statements
    """
    Get status code

    :param status: status code or message
    """
    if isinstance(status, str):
        status = status.upper()
    if isinstance(status, int):
        status = str(status)

    status_to_status_code = {
        "100": 100,
        "CONTINUE": 100,
        "102": 102,
        "PROCESSING": 102,
        "200": 200,
        "OK": 200,
        "SUCCESS": 200,
        "201": 201,
        "CREATED": 201,
        "202": 202,
        "ACCEPTED": 202,
        "400": 400,
        "BAD REQUEST": 400,
        "401": 401,
        "UNAUTHORIZED": 401,
        "402": 402,
        "PAYMENT REQUIRED": 402,
        "403": 403,
        "FORBIDDEN": 403,
        "404": 404,
        "NOT FOUND": 404,
        "405": 405,
        "METHOD NOT ALLOWED": 405,
        "406": 406,
        "NOT ACCEPTED": 406,
        "408": 408,
        "REQUEST TIMEOUT": 408,
        "409": 409,
        "CONFLICT": 409,
        "422": 422,
        "UNPROCESSABLE ENTITY": 422,
        "423": 423,
        "LOCKED": 423,
        "429": 429,
        "TOO MANY REQUESTS": 429,
        "451": 451,
        "UNAVAILABLE FOR LEGAL REASONS": 451,
        "500": 500,
        "INTERNAL SERVER ERROR": 500,
        "501": 501,
        "NOT IMPLEMENTED": 501,
        "502": 502,
        "BAD GATEWAY": 502,
        "503": 503,
        "SERVICE UNAVAILABLE": 503,
        "504": 504,
        "GATEWAY TIMEOUT": 504,
        "505": 505,
        "HTTP VERSION NOT SUPPORTED": 505,
        "506": 506,
        "VARIANT ALSO NEGOTIATES": 506,
        "507": 507,
        "INSUFFICIENT STORAGE": 507,
        "508": 508,
        "LOOP DETECTED": 508,
        "510": 510,
        "NOT EXTENDED": 510,
        "511": 511,
        "NETWORK AUTHENTICATION REQUIRED": 511,
    }

    _status_code = status_to_status_code.get(status, None)
    if not _status_code:
        raise InternalServerError("HTTP status not supported")
    return _status_code


def request_default_filters():
    """Default/Most used request filters"""
    return {
        "page": request.args.get("page", default=1, type=int),
        "per_page": request.args.get("page", default=10, type=int),
        "search": request.args.get("search", default=None, type=str),
    }
