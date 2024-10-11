# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoleRetrieveAllParams"]


class RoleRetrieveAllParams(TypedDict, total=False):
    show_hidden: Annotated[bool, PropertyInfo(alias="show-hidden")]
    """flag indicate if hidden roles should be included"""
