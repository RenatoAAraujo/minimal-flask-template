"""Health endpoints"""
from flask import current_app, request

from app.admin.health import health_bp
from app.services.exceptions.errors import InternalServerError, MethodNotAllowedError
from app.services.requests.helpers import default_return


@health_bp.route("/")
def _health():
    """Health route"""
    try:
        if request.method == "GET":
            return {"hash": current_app.config["APP_HASH"]}, 200

        raise MethodNotAllowedError()
    except (InternalServerError, MethodNotAllowedError) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))
