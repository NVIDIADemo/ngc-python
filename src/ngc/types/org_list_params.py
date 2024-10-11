# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgListParams"]


class OrgListParams(TypedDict, total=False):
    filter_using_org_display_name: Annotated[str, PropertyInfo(alias="Filter using org display name")]

    filter_using_org_name: Annotated[str, PropertyInfo(alias="Filter using org name")]

    filter_using_org_owner_email: Annotated[str, PropertyInfo(alias="Filter using org owner email")]

    filter_using_org_owner_name: Annotated[str, PropertyInfo(alias="Filter using org owner name")]

    filter_using_pec_id: Annotated[str, PropertyInfo(alias="Filter using PEC ID")]

    page_number: Annotated[int, PropertyInfo(alias="page-number")]
    """The page number of result"""

    page_size: Annotated[int, PropertyInfo(alias="page-size")]
    """The page size of result"""
