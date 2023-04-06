"""Flask app creatrion with flask-restx"""
import logging
import os

from flask import Flask, url_for
from flask_restx import Api
from waitress import serve

from app.services.extensions import cache, jwt, ma, migrate
from database.config_sqlalchemy import db, migrate


class CustomAPI(Api):
    @property
    def specs_url(self):
        return url_for(self.endpoint("specs"), _external=False)


def create_app(api):
    """create and configure the flask application"""
    # app
    _app = Flask(__name__)
    _app.config.from_object("config.Config")

    try:
        os.makedirs(_app.instance_path, exist_ok=True)
    except OSError as _e:
        print(f'Error in "app.instance_path"\nError: {str(_e)}')

    # extentions
    __resgister_extentions(_app)

    # logger
    logger_lv = (
        logging.WARN
        if os.environ.get("APP_ENV", "development") == "production"
        else logging.DEBUG
    )
    logging.basicConfig(
        level=logger_lv,
        format="%(asctime)s %(levelname)s %(name)s %(threadName)s: %(message)s",
    )

    """API V1"""
    api.init_app(_app)

    return _app


def __resgister_extentions(_app):
    """Register all flask app extensions"""
    # jwt
    jwt.init_app(_app)
    jwt.init_app(_app)

    # database
    db.init_app(_app)
    migrate.init_app(_app, db, compare_type=True)
    ma.init_app(_app)
    cache.init_app(_app)


def __register_namespaces():
    """Register all flask-restx namespace to the API"""
    # admin
    from app.admin.group.views import group_api

    _api.add_namespace(group_api, path="/api/v1/admin/groups")

    from app.admin.health.views import health_api

    _api.add_namespace(health_api, path="/api/v1/admin/health")

    from app.admin.users.views import user_admin_api

    _api.add_namespace(user_admin_api, path="/api/v1/admin/users")

    # auth
    from app.auth.views import auth_api

    _api.add_namespace(auth_api, path="/api/v1/auth")


def __register_models():
    """Register all swagger models"""
    from app.services.sqlalchemy.swagger.models import (
        null_pagination_info,
        pagination_info,
    )

    _api.models["null_pagination_info"] = null_pagination_info
    _api.models["pagination_info"] = pagination_info

    from app.services.exceptions.swagger.models import error_data_model, error_model

    _api.models["error_data"] = error_data_model
    _api.models["error"] = error_model


_api = Api(
    version="1.0",
    title="Barber API",
    description="A API that uses flask restx",
    doc="/doc",
)
__register_namespaces()
__register_models()


app = create_app(_api)
port = os.environ.get("PORT", "5000")


if os.environ.get("APP_ENV", "development") == "production":
    app.logger.info("Environment prod running. Port %s", port)
    serve(app, host="0.0.0.0", port=port)
else:
    try:
        app.run(host="0.0.0.0", port=port, debug=True)
    except Exception as e:
        print(f"Error:\n{str(e)}")
