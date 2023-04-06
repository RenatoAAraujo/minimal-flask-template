"""Flask app extentions"""
import os

import boto3
from flask_caching import Cache
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from config import Config

cors = CORS()
cache = Cache()
jwt = JWTManager()
migrate = Migrate()
ma = Marshmallow()

s3 = boto3.client(
    "s3",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
)

# aws simple notification service
sns = boto3.client(
    "sns",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name="us-east-1",
)

# aws simple email service
ses = boto3.client(
    "ses",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name="us-east-1",
)
