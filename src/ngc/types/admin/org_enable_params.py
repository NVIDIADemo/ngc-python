# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OrgEnableParams", "ProductEnablement", "ProductEnablementPoDetail"]


class OrgEnableParams(TypedDict, total=False):
    create_subscription: Required[Annotated[bool, PropertyInfo(alias="createSubscription")]]
    """False only if called by SbMS."""

    product_enablement: Required[Annotated[ProductEnablement, PropertyInfo(alias="productEnablement")]]
    """Product Enablement"""


class ProductEnablementPoDetail(TypedDict, total=False):
    entitlement_id: Annotated[str, PropertyInfo(alias="entitlementId")]
    """Entitlement identifier."""

    pk_id: Annotated[str, PropertyInfo(alias="pkId")]
    """PAK (Product Activation Key) identifier."""


class ProductEnablement(TypedDict, total=False):
    product_name: Required[Annotated[str, PropertyInfo(alias="productName")]]
    """Product Name (NVAIE, BASE_COMMAND, REGISTRY, etc)"""

    type: Required[
        Literal[
            "NGC_ADMIN_EVAL",
            "NGC_ADMIN_NFR",
            "NGC_ADMIN_COMMERCIAL",
            "EMS_EVAL",
            "EMS_NFR",
            "EMS_COMMERCIAL",
            "NGC_ADMIN_DEVELOPER",
        ]
    ]
    """Product Enablement Types"""

    expiration_date: Annotated[str, PropertyInfo(alias="expirationDate")]
    """Date on which the subscription expires.

    The subscription is invalid after this date. (yyyy-MM-dd)
    """

    po_details: Annotated[Iterable[ProductEnablementPoDetail], PropertyInfo(alias="poDetails")]
