import pytest
import werkzeug

from app.services.exceptions.errors import (
    BadRequestError,
    ConflictError,
    ForbiddenError,
    GenerateError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)


def test_bad_request_error():
    error_msg = "Test BadRequest"
    with pytest.raises(BadRequestError) as e:
        print(e)
        raise BadRequestError(error_msg)

    assert e.value.status_code == 400
    assert e.value.message == error_msg


def test_unauthorized_error():
    error_msg = "Test UnauthorizedError"
    with pytest.raises(UnauthorizedError) as e:
        raise UnauthorizedError(error_msg)

    assert e.value.status_code == 401
    assert e.value.message == error_msg


def test_forbidden_error():
    error_msg = "Test ForbiddenError"
    with pytest.raises(ForbiddenError) as e:
        raise ForbiddenError(error_msg)

    assert e.value.status_code == 403
    assert e.value.message == error_msg


def test_not_found_error():
    error_msg = "Test NotFoundError"
    with pytest.raises(NotFoundError) as e:
        raise NotFoundError(error_msg)

    assert e.value.status_code == 404
    assert e.value.message == error_msg


def test_conflict_error():
    error_msg = "Test ConflictError"
    with pytest.raises(ConflictError) as e:
        raise ConflictError(error_msg)

    assert e.value.status_code == 409
    assert e.value.message == error_msg


def test_internal_server_error():
    error_msg = "Test InternalServerError"
    with pytest.raises(InternalServerError) as e:
        raise InternalServerError(error_msg)

    assert e.value.status_code == 500
    assert e.value.message == error_msg


@pytest.mark.parametrize(
    "status_code, error_message",
    [
        (422, "Test UnprocessableError"),
        (500, "Something went wrong!")
    ]
)
def test_generate_exception(status_code, error_message):
    with pytest.raises(GenerateError) as e:
        raise GenerateError(error_message, status_code)

    assert e.value.status_code == status_code
    assert e.value.message == error_message


@pytest.mark.parametrize(
    "error_message",
    [
        "Internal error! Field not found: some_field",
        "Internal error! Field not found: another_field",
        "some_random_field does not exists",
    ]
)
def test_key_error(error_message):
    with pytest.raises(KeyError) as e:
        raise KeyError(error_message)

    assert str(e.value).replace("'", "") == error_message


@pytest.mark.parametrize(
    "error_message",
    [
        "Test NameError",
        "some name error"
    ]
)
def test_name_error(error_message):
    with pytest.raises(NameError) as e:
        raise NameError(error_message)

    str(e.value).replace("'", "") == error_message
