from flask_restx import Model, fields

from app.services.sqlalchemy.swagger.models import null_pagination_info

error_data_model = Model(
    "error_data", {"message": fields.String(description="Error messge", required=True)}
)

error_model = Model(
    "error",
    {
        "pagination_info": fields.Nested(null_pagination_info),
        "data": fields.Nested(error_data_model),
    },
)
