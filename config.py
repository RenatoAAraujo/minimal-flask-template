import os
from datetime import timedelta


class Config:
    # api
    SITE_API_HTTPS = os.environ.get("SITE_HTTPS", "http://localhost:") + str(
        os.environ.get("API_PORT", 5000)
    )
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JSON_SORT_KEYS = False

    # static
    APP_VERSION = os.environ.get("APP_VERSION", "latest")
    APP_HASH = os.environ.get("APP_HASH", "latest")
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    STATIC_DIR = os.path.abspath(os.path.join(APP_DIR, "static"))

    # database
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.environ.get('DB_USER')}:"
        f"{os.environ.get('DB_PASSWORD')}@"
        f"{os.environ.get('DB_HOST')}/"
        f"{os.environ.get('DB_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 0

    # cache
    CACHE_TYPE = os.environ.get("CACHE_TYPE", "simple")
    if CACHE_TYPE == "redis":
        CACHE_REDIS_HOST = os.environ.get("CACHE_REDIS_HOST")
        CACHE_REDIS_PORT = os.environ.get("CACHE_REDIS_PORT")
        CACHE_KEY_PREFIX = SITE_API_HTTPS

    # jwt
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRES = 3600
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    BASIC_CLIENT = os.environ.get("BASIC_CLIENT")
    BASIC_ADMIN = os.environ.get("BASIC_ADMIN")

    # aws
    AWS_ACCESS_KEY_ID = None
    AWS_SECRET_ACCESS_KEY = None
    AWS_LOCATION = None
    AWS_BUCKET = None
    AWS_BUCKET_LOCATION = AWS_LOCATION
    AWS_BUCKET_CLOUDFRONT = None

    if os.environ.get("APP_ENV") == "development":
        DEBUG = True
    else:
        DEBUG = False
