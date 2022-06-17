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


def get_request_status_code(
    status,
):  # pylint: disable=too-many-branches, too-many-statements
    """
    Get status code

    :param status: status code or message
    """
    if isinstance(status, str):
        status = status.upper()

    if status in [100, "CONTINUE"]:
        status = 100
    elif status in [101, "SWITCHING PROTOCOLS"]:
        status = 101
    elif status in [102, "PROCESSING"]:
        status = 102
    elif status in [103, "EARLY HINTS"]:
        status = 103
    elif status in [200, "OK", "SUCCESS"]:
        status = 200
    elif status in [201, "CREATED"]:
        status = 201
    elif status in [202, "ACCEPTED"]:
        status = 202
    elif status in [203, "NON-AUTHORITATIVE INFORMATION"]:
        status = 203
    elif status in [204, "NO CONTENT"]:
        status = 204
    elif status in [205, "RESET CONTENT"]:
        status = 205
    elif status in [206, "PARTIAL CONTENT"]:
        status = 206
    elif status in [207, "MULTI-STATUS"]:
        status = 207
    elif status in [208, "ALREADY REPORTED"]:
        status = 208
    elif status in [226, "IM USED"]:
        status = 226
    elif status in [300, "MULTIPLE CHOICES"]:
        status = 300
    elif status in [301, "MOVED PERMANENTLY"]:
        status = 301
    elif status in [302, "FOUND"]:
        status = 302
    elif status in [303, "SEE OTHER"]:
        status = 303
    elif status in [304, "NOT MODIFIED"]:
        status = 304
    elif status in [307, "TEMPORARY REDIRECT"]:
        status = 307
    elif status in [308, "PERMANENT REDIRECT"]:
        status = 308
    elif status in [400, "BAD REQUEST"]:
        status = 400
    elif status in [401, "UNAUTHORIZED"]:
        status = 401
    elif status in [402, "PAYMENT REQUIRED"]:
        status = 402
    elif status in [403, "FORBIDDEN"]:
        status = 403
    elif status in [404, "NOT FOUND"]:
        status = 404
    elif status in [405, "METHOD NOT ALLOWED"]:
        status = 405
    elif status in [406, "NOT ACCEPTED"]:
        status = 406
    elif status in [407, "PROXY AUTHENTICATION REQUIRED"]:
        status = 407
    elif status in [408, "REQUEST TIMEOUT"]:
        status = 408
    elif status in [409, "CONFLICT"]:
        status = 409
    elif status in [410, "GONE"]:
        status = 410
    elif status in [411, "LENGTH REQUIRED"]:
        status = 411
    elif status in [412, "PRECONDITION FAILED"]:
        status = 412
    elif status in [413, "REQUEST ENTITY TOO LARGE"]:
        status = 413
    elif status in [414, "REQUEST ENTITY TOO LOONG"]:
        status = 414
    elif status in [415, "UNSUPPORTED MEDIA TYPE"]:
        status = 415
    elif status in [416, "REQUEST RANGE NOT SATISFIABLE"]:
        status = 416
    elif status in [417, "EXPECTATION FAILED"]:
        status = 417
    elif status in [418, "I'M A TEAPOT"]:
        status = 418
    elif status in [421, "MISDIRECTED REQUEST"]:
        status = 421
    elif status in [422, "UNPROCESSABLE ENTITY"]:
        status = 422
    elif status in [423, "LOCKED"]:
        status = 423
    elif status in [424, "FAILED DEPENDENCY"]:
        status = 424
    elif status in [425, "TOO EARLY"]:
        status = 425
    elif status in [426, "UPGRADE REQUIRED"]:
        status = 426
    elif status in [428, "PRECONDITION REQUIRED"]:
        status = 428
    elif status in [429, "TOO MANY REQUESTS"]:
        status = 429
    elif status in [431, "REQUEST HEADER FIELDS TOO LARGE"]:
        status = 431
    elif status in [451, "UNAVAILABLE FOR LEGAL REASONS"]:
        status = 451
    elif status in [500, "INTERNAL SERVER ERROR"]:
        status = 500
    elif status in [501, "NOT IMPLEMENTED"]:
        status = 501
    elif status in [502, "BAD GATEWAY"]:
        status = 502
    elif status in [503, "SERVICE UNAVAILABLE"]:
        status = 503
    elif status in [504, "GATEWAY TIMEOUT"]:
        status = 504
    elif status in [505, "HTTP VERSION NOT SUPPORTED"]:
        status = 505
    elif status in [506, "VARIANT ALSO NEGOTIATES"]:
        status = 506
    elif status in [507, "INSUFFICIENT STORAGE"]:
        status = 507
    elif status in [508, "LOOP DETECTED"]:
        status = 508
    elif status in [510, "NOT EXTENDED"]:
        status = 510
    elif status in [511, "NETWORK AUTHENTICATION REQUIRED"]:
        status = 511
    else:
        raise InternalServerError("HTTP status not supported")

    return status


def request_default_filters():
    """Default/Most used request filters"""
    return {
        "page": request.args.get("page", default=1, type=int),
        "per_page": request.args.get("page", default=10, type=int),
        "search": request.args.get("search", default=None, type=str),
    }
