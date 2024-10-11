# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserAddParams"]


class UserAddParams(TypedDict, total=False):
    org_name: Required[Annotated[str, PropertyInfo(alias="org-name")]]

    user_role_defaults_to_registry_read: Annotated[str, PropertyInfo(alias="user role, defaults to REGISTRY_READ")]
