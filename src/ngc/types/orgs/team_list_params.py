# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TeamListParams"]


class TeamListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page-number")]
    """The page number of result"""

    page_size: Annotated[int, PropertyInfo(alias="page-size")]
    """The page size of result"""
