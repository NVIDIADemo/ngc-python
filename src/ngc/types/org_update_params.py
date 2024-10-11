# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgUpdateParams"]


class OrgUpdateParams(TypedDict, total=False):
    description: str
    """optional description of the organization"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Name of the organization that will be shown to users"""
