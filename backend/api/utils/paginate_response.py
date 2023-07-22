from typing import Any

from django.core.paginator import Paginator


def paginate_response(items: Any, serializer: Any, per_page: int, page: int) -> dict:
    paginator = Paginator(object_list=items, per_page=per_page)

    data = paginator.page(page)
    results = serializer(data, many=True).data

    payload = {
        "info": {
            "count": paginator.count,
            "page": page,
            "per_page": per_page,
            "has_next": data.has_next(),
            "has_previous": data.has_previous(),
        },
        "results": results,
    }

    return payload
