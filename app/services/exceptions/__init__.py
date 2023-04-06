from flask import Blueprint

exception_handler_bp = Blueprint("exception_handler_bp", __name__)
from . import errors
