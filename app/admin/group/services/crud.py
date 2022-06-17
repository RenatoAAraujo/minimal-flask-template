"""Group CRUD"""
from flask import request
from sqlalchemy import or_

from app.admin.group.models import Group
from app.admin.group.schemas import GroupSchema
from app.services.exceptions.errors import NotFoundError
from app.services.requests.helpers import request_default_filters
from app.services.sqlalchemy.pagination import get_pagination_info


def create_group(schema=None):
    """
    Creates a group

    :param schema: return schema (boolean)
    """
    dict_body = request.get_json()

    item = Group().create_item(dict_body).save()

    if schema:
        item = GroupSchema().dump(item)

    return item


def get_group(group_id, schema=None, columns=None):
    """
    Get group by ID

    :param group_id: group id (int)
    :param schema: return schema (boolean)
    :param columns: columns to return [columns name]
    """
    query = Group.query
    if columns:
        query = query.with_entities(*[getattr(Group, column) for column in columns])

    item = query.filter(Group.id == group_id).first()

    if not item:
        raise NotFoundError()
    if schema:
        item = GroupSchema().dump(item)

    return item


def get_groups(schema=None, columns=None):
    """
    Get groups

    :param schema: return schema (boolean)
    :param columns: columns to return [columns name]
    """
    filters = request_default_filters()
    query = Group.query.filter(Group.deleted_at == None)

    if columns:
        query = query.with_entities(*[getattr(Group, column) for column in columns])

    if filters["search"]:
        query = query.filter(or_(Group.name.like(f'%%{filters["search"]}%%')))

    items = query.paginate(filters.get("page", 1), filters.get("per_page", 10), False)
    pagination_info = get_pagination_info(items)

    if schema:
        items = GroupSchema(many=True).dump(items.items)

    return items, pagination_info


def update_group(group_id, schema=None):
    """
    Update group by ID

    :param group_id: group id (int)
    :param schema: return schema (boolean)
    """
    dict_body = request.get_json()

    item = get_group(group_id)
    item.update_item(dict_body).update()

    if schema:
        item = GroupSchema().dump(item)

    return item


def delete_group(group_id):
    """
    delete group by ID

    :param group_id: group id (int)
    """
    item = get_group(group_id)
    item.delete()

    return GroupSchema().dump(item)
