from flask import Flask
from flask_restx import Api

from app import resgister_extentions, register_models, register_namespaces, api, app, create_app, port


def test_api_instance():
    assert isinstance(api, Api)


def test_app_instance():
    assert isinstance(app, Flask)


def test_port_values():
    assert port is not None


def test_app_creation():
    _app = create_app(api)

    assert isinstance(_app, Flask)


def test_namespace_register():
    register_namespaces()

    assert isinstance(api, Api)


def test_model_register():
    register_models()

    assert isinstance(api, Api)


def test_extension_register():
    resgister_extentions(app)

    assert isinstance(app, Flask)


def test_full_creation():
    _app = create_app(api)
    register_namespaces()
    register_models()

    assert isinstance(_app, Flask)
    assert isinstance(api, Api)
