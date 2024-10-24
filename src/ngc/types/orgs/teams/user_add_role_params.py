# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserAddRoleParams"]


class UserAddRoleParams(TypedDict, total=False):
    org_name: Required[Annotated[str, PropertyInfo(alias="org-name")]]

    team_name: Required[Annotated[str, PropertyInfo(alias="team-name")]]

    roles: Required[List[str]]
