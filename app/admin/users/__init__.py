"""Users admin blueprint"""
from flask_restx import Namespace

from app.admin.users.swagger.models import (
    create_user_model,
    update_user_model,
    user_model,
)

user_admin_api = Namespace("admin_users", description="User Admin Endpoints")

# models
user_admin_api.models["user"] = user_model
user_admin_api.models["create_user"] = create_user_model
user_admin_api.models["update_user"] = update_user_model
