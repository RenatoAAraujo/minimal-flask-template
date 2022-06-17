"""Request pagination helpers"""
from app.services.requests.helpers import request_default_filters


def get_pagination_info(paginated_query):
    """
    Build pagination info

    :param paginated_query: paginated query object
    """
    request_filters = request_default_filters()

    try:
        query_by_id_total = paginated_query.count()
    except (Exception,):
        query_by_id_total = None

    try:
        return {
            "has_next": paginated_query.has_next,
            "has_prev": paginated_query.has_prev,
            "next_num": paginated_query.next_num,
            "prev_num": paginated_query.prev_num,
            "page": paginated_query.page,
            "pages": paginated_query.pages,
            "per_page": paginated_query.per_page,
            "total": paginated_query.total,
        }
    except (AttributeError, KeyError):
        if query_by_id_total:  # pylint: disable=no-else-return
            return {
                "has_next": False,
                "has_prev": False,
                "next_num": None,
                "prev_num": None,
                "page": request_filters["page"],
                "pages": 1,
                "per_page": request_filters["per_page"],
                "total": query_by_id_total,
            }

        return {
            "has_next": None,
            "has_prev": None,
            "next_num": None,
            "prev_num": None,
            "page": request_filters["page"],
            "pages": None,
            "per_page": request_filters["per_page"],
            "total": None,
        }
