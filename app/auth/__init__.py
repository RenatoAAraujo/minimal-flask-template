"""Auth blueprint"""
from flask_restx import Namespace

from app.auth.swagger.models import login_request, successful_login, successful_logout

auth_api = Namespace("auth", description="Auth Endpoints")

# models
auth_api.models["login_request"] = login_request
auth_api.models["successful_login"] = successful_login
auth_api.models["successful_logout"] = successful_logout
