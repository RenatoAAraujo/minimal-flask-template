"""User CRUD"""
from sqlalchemy import or_

from app.admin.users.models import User
from app.admin.users.schemas import UserSchema
from app.services.exceptions.errors import ConflictError, NotFoundError
from app.services.requests.helpers import request_default_filters
from app.services.sqlalchemy.pagination import get_pagination_info


def get_users(
    user_id: int = None,
    user_hash_id: str = None,
    filters: dict = None,
    schema: bool = True,
):
    """
    Returns user entities.
    The param user_id is used internally and user_hash_is is called externally

    :param user_id: Filter user by id
    :param user_hash_id: Filter user by hash_id
    :param filters: filters items and paginate
    :param schema: return schema or object
    """
    if user_id:
        assert isinstance(int(user_id), int), '"user_id" must be an int'
    if user_hash_id:
        assert isinstance(user_hash_id, str), '"user_hash_id" must be an int'
    if filters:
        assert isinstance(filters, dict), '"filters" must be a dict'
    else:
        filters = request_default_filters()
    assert isinstance(schema, bool), '"schema" must be a boolean'

    items = User.query.filter(User.deleted_at == None)

    if user_id or user_hash_id:
        items = items.filter(
            or_(User.id == user_id, User.hash_id == user_hash_id)
        ).first()

        _id = user_id if user_id else user_hash_id
        if schema:
            items = UserSchema().dump(items)
            if len(items) == 0:
                raise NotFoundError(f"User (ID: {_id}) not found")
        else:
            if not items:
                raise NotFoundError(f"User (ID: {_id}) not found")

        pagination_info = get_pagination_info(items)
    else:
        if filters.get("email"):
            items = items.filter(User.email == filters["email"])
        if filters.get("taxpayer_id"):
            items = items.filter(User.taxpayer_id == filters["taxpayer_id"])
        if filters.get("search"):
            items = items.filter(
                or_(
                    User.name.like(f'%%{filters["search"]}%%'),
                    User.email.like(f'%%{filters["search"]}%%'),
                )
            )

        items.paginate(
            page=filters.get("page", 1),
            per_page=filters.get("per_page", 10),
            error_out=False,
        )
        pagination_info = get_pagination_info(items)

        if schema:
            items = UserSchema(many=True).dump(items)
        else:
            items.all()

    return items, pagination_info


def create_user(user_data: dict, schema: bool = True) -> User:
    """
    Create user entity.

    :param user_data: user data
    :param schema: return schema or object
    """
    _users = User.query.filter(
        User.deleted_at == None,
        or_(
            User.email == user_data["email"],
            User.taxpayer_id == user_data["taxpayer_id"],
        ),
    ).first()
    if _users:
        raise ConflictError(
            "A user with this email or taxpayer_id has been registered."
        )

    user = User().create_item(user_data).save()

    if schema:
        user = UserSchema().dump(user)

    return user


def update_user(
    user_data: dict, user_id: int = None, user_hash_id: str = None, schema: bool = True
):
    """
    Create user entity.
    The param user_id is used internally and user_hash_is is called externally

    :param user_data: user data
    :param user_id: Filter user by id
    :param user_hash_id: Filter user by hash_id
    :param schema: return schema or object
    """
    user, _ = get_users(user_id, user_hash_id, schema=False)
    user.update_item(user_data).update()

    if schema:
        user = UserSchema().dump(user)

    return user


def delete_user(user_id: int = None, user_hash_id: str = None, schema: bool = True):
    """
    Delete user entity.
    The param user_id is used internally and user_hash_is is called externally

    :param user_id: Filter user by id
    :param user_hash_id: Filter user by hash_id
    :param schema: return schema or object
    """
    user, _ = get_users(user_id, user_hash_id, schema=False)
    user.delete()

    if schema:
        user = UserSchema().dump(user)

    return user
