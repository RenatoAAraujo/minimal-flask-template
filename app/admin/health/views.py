"""Health endpoints"""
from flask import current_app, request

from app.admin.health import bp
from app.services.exceptions.errors import InternalServerError, MethodNotAllowedError
from app.services.requests.helpers import default_return


@bp.route("/")
def _health(group_id):
    """Health route"""
    try:
        if request.method == "GET":
            return {"hash": current_app.config["APP_HASH"]}, 200
        else:
            raise MethodNotAllowedError()            
    except (InternalServerError, MethodNotAllowedError) as e:
        return default_return(e.status_code, e.message)
    except Exception as e:
        return default_return(500, str(e))
