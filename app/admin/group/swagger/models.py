from flask_restx import Model, fields

group_model = Model(
    "group",
    {
        "id": fields.Integer(description="Table group id", required=True, example=1),
        "name": fields.String(
            description="Group name",
            required=True,
            example="Admin",
        ),
        "status": fields.Boolean(
            description="Active group",
            required=True,
            example="True|False",
        ),
        "created_at": fields.DateTime(
            description="Creation date time",
            required=True,
            example="2022-02-27 15:12:50",
        ),
        "updated_at": fields.DateTime(
            description="Update date time", required=True, example="2022-02-27 15:12:50"
        ),
        "deleted_at": fields.DateTime(
            description="Delete date time", required=True, example="2022-02-27 15:12:50"
        ),
    },
)

create_group_model = Model(
    "create_group",
    {
        "name": fields.String(
            description="Group name",
            required=True,
            example="Admin",
        ),
    },
)

update_group_model = Model(
    "update_group",
    {
        "name": fields.String(
            description="Group name",
            required=True,
            example="Admin",
        ),
        "status": fields.Boolean(
            description="Active group",
            required=True,
            example="True|False",
        ),
    },
)
