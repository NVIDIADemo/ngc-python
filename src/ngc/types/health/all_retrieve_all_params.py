# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AllRetrieveAllParams"]


class AllRetrieveAllParams(TypedDict, total=False):
    secret: str
    """secret value that validates the call in order to show details"""

    show_details: Annotated[bool, PropertyInfo(alias="showDetails")]
    """boolean value to indicating to show details or not"""
