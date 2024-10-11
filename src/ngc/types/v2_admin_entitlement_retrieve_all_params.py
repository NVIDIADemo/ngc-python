# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["V2AdminEntitlementRetrieveAllParams"]


class V2AdminEntitlementRetrieveAllParams(TypedDict, total=False):
    is_paid_subscription: Annotated[bool, PropertyInfo(alias="is-paid-subscription")]
    """get is paid subscription entitlements"""

    product_name: Annotated[str, PropertyInfo(alias="product-name")]
    """filter by product-name"""
