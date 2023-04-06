from flask_restx import Model, fields

get_health = Model(
    "get_health",
    {
        "hash": fields.String(
            description="API hash",
            required=True,
            example="current",
        ),
    },
)
