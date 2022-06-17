import pytest

from app import api, create_app, db


@pytest.fixture
def app():
    """return the web application"""
    # change env
    _app = create_app(api, testing=True)
    app_context = _app.app_context()
    app_context.push()
    db.drop_all()
    db.create_all()
    yield _app
    db.drop_all()
    db.session.rollback()
    app_context.pop()


@pytest.fixture()
def client(app):
    yield app.test_client()


@pytest.fixture
def base64_img():
    return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z/C/HgAGgwJ/lK3Q6wAAAABJRU5ErkJggg=="
