"""Health blueprint"""
from flask_restx import Namespace

from app.admin.health.swagger.models import get_health

health_api = Namespace("admin_health", description="API health status")

# models
health_api.models["get_health"] = get_health
