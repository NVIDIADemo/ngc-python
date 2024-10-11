# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserDeleteParams"]


class UserDeleteParams(TypedDict, total=False):
    org_name: Required[Annotated[str, PropertyInfo(alias="org-name")]]

    anonymize: bool
    """If anonymize is true, then org owner permission is required."""
