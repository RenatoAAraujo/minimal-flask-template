"""Flask app creatrion with flask-restx"""
import logging
import os

from flask import Flask
from waitress import serve

from app.services.extensions import cache, jwt, ma
from database.config_sqlalchemy import db, migrate


def create_app(deploy_env="Testing"):
    """create and configure the flask application"""
    # app
    _app = Flask(__name__)
    if not deploy_env:
        raise ValueError("Invalid APP_ENV!")
    _app.config.from_object(f"config.{os.environ.get('APP_ENV')}Config")

    try:
        os.makedirs(_app.instance_path, exist_ok=True)
    except OSError as _e:
        print(f'Error in "app.instance_path"\nError: {str(_e)}')

    # extentions
    resgister_extentions(_app)

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

    return _app


def resgister_extentions(_app):
    # jwt
    jwt.init_app(_app)
    jwt.init_app(_app)

    # database
    db.init_app(_app)
    migrate.init_app(_app, db, compare_type=True)
    ma.init_app(_app)
    cache.init_app(_app)


def register_blueprints(app):
    """Register all flask-restx namespace to the API"""
    # admin
    from app.admin.group.views import bp as group_bp

    app.register_blueprint(group_bp, url_prefix="/api/v1/admin/groups")

    from app.admin.health.views import bp as health_bp

    app.register_blueprint(health_bp, url_prefix="/api/v1/admin/health")

    from app.admin.users.views import bp as user_admin_bp

    app.register_blueprint(user_admin_bp, url_prefix="/api/v1/admin/users")

    # auth
    from app.auth.views import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")



app = create_app(deploy_env=os.environ.get("APP_ENV"))
port = os.environ.get("PORT", "5000")


register_blueprints(app)


if os.environ.get("APP_ENV", "development") == "production":
    app.logger.info(
        "Environment prod running. Port %s", port
    )  # pylint: disable=no-member
    serve(app, host="0.0.0.0", port=port)
else:
    try:
        app.run(host="0.0.0.0", port=port, debug=True)
    except (Exception,) as e:
        print(f"Error:\n{str(e)}")
