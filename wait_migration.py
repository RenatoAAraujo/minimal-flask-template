import os

if os.environ.get("DB_MIGRATE"):
    if not os.environ.get("DB_MIGRATE") == "Testing":
        os.system(
            f"dockerize -wait tcp://{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')} -timeout {os.environ.get('DB_WAIT')}"
        )
    else:
        os.system(
            f"dockerize -wait tcp://{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT_TEST')} -timeout {os.environ.get('DB_WAIT')}"
        )
    os.system("flask db upgrade")
