# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserListParams", "Q", "QFilter", "QOrderBy"]


class UserListParams(TypedDict, total=False):
    exclude_from_team: Annotated[str, PropertyInfo(alias="exclude-from-team")]
    """Name of team to exclude members from"""

    page_number: Annotated[int, PropertyInfo(alias="page-number")]
    """The page number of result"""

    page_size: Annotated[int, PropertyInfo(alias="page-size")]
    """The page size of result"""

    q: Q
    """User Search Parameters.

    Only 'filters' and 'orderBy' for 'name' and 'email' are implemented
    """


class QFilter(TypedDict, total=False):
    field: str

    value: str


class QOrderBy(TypedDict, total=False):
    field: str

    value: Literal["ASC", "DESC"]


class Q(TypedDict, total=False):
    fields: List[str]

    filters: Iterable[QFilter]

    group_by: Annotated[str, PropertyInfo(alias="groupBy")]

    order_by: Annotated[Iterable[QOrderBy], PropertyInfo(alias="orderBy")]

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    query: str

    query_fields: Annotated[List[str], PropertyInfo(alias="queryFields")]

    scored_size: Annotated[int, PropertyInfo(alias="scoredSize")]
