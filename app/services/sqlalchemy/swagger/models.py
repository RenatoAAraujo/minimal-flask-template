from flask_restx import Model, fields

null_pagination_info = Model(
    "null_pagination_info",
    {},
)
pagination_info = Model(
    "pagination_info",
    {
        "has_next": fields.Boolean(
            description="Has a next page", required=True, example="null|true|false"
        ),
        "has_prev": fields.Boolean(
            description="Has a previous page", required=True, example="null|true|false"
        ),
        "next_num": fields.Integer(
            description="Next page number", required=True, example="null|2"
        ),
        "prev_num": fields.Integer(
            description="Previous page number", required=True, example="null|1"
        ),
        "page": fields.Integer(
            description="Current page number", required=True, example="1"
        ),
        "pages": fields.Integer(
            description="Total number pages", required=True, example="null|100"
        ),
        "per_page": fields.Integer(
            description="Items per page", required=True, example="10"
        ),
        "total": fields.Integer(
            description="Total number of items", required=True, example="null|1023"
        ),
    },
)
