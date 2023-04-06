from flask_restx import Model, fields

from app.admin.group import group_model

user_model = Model(
    "user",
    {
        "id": fields.Integer(description="Table user id", required=True, example=1),
        "hash_id": fields.String(
            description="Table user hash id, for outside calls",
            required=True,
            example="eeb09670-99f4-4357-b421-0767b30a1a17",
        ),
        "name": fields.String(
            description="User's name",
            required=True,
            example="Client Name",
        ),
        "email": fields.String(
            description="User's email",
            required=True,
            example="usarioclient@email.com",
        ),
        "email_verified": fields.Boolean(
            description="User's email verified",
            required=True,
            example="true|false",
        ),
        "token_update": fields.String(
            description="User's update token",
            required=False,
            example="6b8ab13b-cb69-46f3-af50-3b7b32eb5e45",
        ),
        "taxpayer_id": fields.String(
            description="User's taxpayer id",
            required=True,
            example="027.053.450-43",
        ),
        "cellphone": fields.String(
            description="User's cellphone",
            required=False,
            example="62999999999",
        ),
        "birth_date": fields.String(
            description="User's birth date",
            required=True,
            example="05/11/1997",
        ),
        "genre": fields.String(
            description="User's Genre",
            required=False,
            example="null|M|F",
        ),
        "image_key": fields.String(
            description="User's image key",
            required=False,
            example="null|kbalkjgdskgbfjklshgru",
        ),
        "status": fields.Boolean(
            description="Active user",
            required=True,
            example="True|False",
        ),
        "group_id": fields.Boolean(
            description="User's group id",
            required=True,
            example=5,
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
        "group": fields.Nested(group_model),
    },
)

create_user_model = Model(
    "create_user",
    {
        "name": fields.String(
            description="User's name",
            required=True,
            example="Client Name",
        ),
        "email": fields.String(
            description="User's email",
            required=True,
            example="usarioclient@email.com",
        ),
        "password": fields.String(
            description="User's password", required=True, example="123456"
        ),
        "taxpayer_id": fields.String(
            description="User's taxpayer id",
            required=True,
            example="027.053.450-43",
        ),
        "cellphone": fields.String(
            description="User's cellphone",
            required=False,
            example="62999999999",
        ),
        "birth_date": fields.String(
            description="User's birth date",
            required=True,
            example="05/11/1997",
        ),
        "genre": fields.String(
            description="User's Genre",
            required=False,
            example="null|M|F",
        ),
        "group_id": fields.Boolean(
            description="User's group id",
            required=True,
            example=5,
        ),
    },
)

update_user_model = Model(
    "update_user",
    {
        "password": fields.String(
            description="User's password", required=False, example="123456"
        ),
        "name": fields.String(
            description="User's name",
            required=False,
            example="Client Name",
        ),
        "genre": fields.String(
            description="User's Genre",
            required=False,
            example="null|M|F",
        ),
        "cellphone": fields.String(
            description="User's cellphone",
            required=False,
            example="62999999999",
        ),
        "birth_date": fields.String(
            description="User's birth date",
            required=False,
            example="05/11/1997",
        ),
        "status": fields.Boolean(
            description="Active user",
            required=False,
            example="True|False",
        ),
        "group_id": fields.Boolean(
            description="User's group id",
            required=False,
            example=5,
        ),
    },
)
