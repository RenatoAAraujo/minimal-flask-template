"""Group blueprint"""
from flask_restx import Namespace

from app.admin.group.swagger.models import (
    create_group_model,
    group_model,
    update_group_model,
)

group_api = Namespace("admin_group", description="User groups")

# models
group_api.models["group"] = group_model
group_api.models["create_group"] = create_group_model
group_api.models["update_group"] = update_group_model
