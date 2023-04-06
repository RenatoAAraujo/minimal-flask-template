from flask_restx import Model, fields

login_request = Model(
    "login_request",
    {
        "username": fields.String(
            description="Username for authentication",
            required=True,
            example="usarioclient@email.com",
        ),
        "password": fields.String(
            description="'User's password'", required=True, example="123456"
        ),
    },
)
successful_login = Model(
    "successful_login",
    {
        "token_type": fields.String(
            description="Token type", required=True, example="Bearer"
        ),
        "expires_in": fields.Integer(
            description="Token expiration time (seconds)", required=True, example=3600
        ),
        "access_token": fields.String(
            description="Access token",
            required=True,
            example="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NTk4MDc3MywianRpIjoiYWQ4ZjA3NWItMThjYS00YjE1LWJlZmQtZmY4ZDUzYWNkMzhiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJoYXNoX2lkIjoiNmRjZjBiMTctMDQxZC00YmY1LThkNDUtNjY4NDFjNWNlOTZkIiwibmFtZSI6IlVzdVx1MDBlMXJpbyBBZG1pbiIsImdyb3VwX2lkIjoyLCJyb2xlcyI6WyJVU0VSX0MiLDIsM119LCJuYmYiOjE2NDU5ODA3NzMsImV4cCI6MTY0NjA2NzE3M30.PwdcST2l8gpoyuWIX9pb3lOPMYElzbhVhwSs2FEYrqU",
        ),
        "refresh_token": fields.Integer(
            description="Token for refresing authentication",
            required=True,
            example="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NTk4MDc3MywianRpIjoiOWEyNWU5MGItMWIxYS00NjJhLTlhNDEtYTM2OTRiMWI2NzM1IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOnsiaGFzaF9pZCI6IjZkY2YwYjE3LTA0MWQtNGJmNS04ZDQ1LTY2ODQxYzVjZTk2ZCIsIm5hbWUiOiJVc3VcdTAwZTFyaW8gQWRtaW4iLCJncm91cF9pZCI6Miwicm9sZXMiOlsiVVNFUl9DIiwyLDNdfSwibmJmIjoxNjQ1OTgwNzczLCJleHAiOjE2NDg1NzI3NzN9.qhpn0IDN-xbopdF1QXAMgjpqqBbzN8WyFwpFFVwpnII",
        ),
    },
)
successful_logout = Model(
    "successful_logout",
    {
        "id": fields.Integer(
            description="Table jwt_token_blockllist id", required=True, example=1
        ),
        "jti": fields.String(
            description="User's JTI",
            required=True,
            example="50a0b30b-2300-4445-ac82-b602e0fd353b",
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
