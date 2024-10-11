# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OrgCreateParams", "OrgOwner", "ProductEnablement", "ProductEnablementPoDetail", "ProductSubscription"]


class OrgCreateParams(TypedDict, total=False):
    org_owner: Required[Annotated[OrgOwner, PropertyInfo(alias="orgOwner")]]
    """Org owner."""

    country: str
    """user country"""

    description: str
    """optional description of the organization"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Name of the organization that will be shown to users."""

    idp_id: Annotated[str, PropertyInfo(alias="idpId")]
    """Identity Provider ID."""

    is_internal: Annotated[bool, PropertyInfo(alias="isInternal")]
    """Is NVIDIA internal org or not"""

    name: str
    """Organization name"""

    pec_name: Annotated[str, PropertyInfo(alias="pecName")]
    """product end customer name for enterprise(Fleet Command) product"""

    pec_sfdc_id: Annotated[str, PropertyInfo(alias="pecSfdcId")]
    """
    product end customer salesforce.com Id (external customer Id) for
    enterprise(Fleet Command) product
    """

    product_enablements: Annotated[Iterable[ProductEnablement], PropertyInfo(alias="productEnablements")]

    product_subscriptions: Annotated[Iterable[ProductSubscription], PropertyInfo(alias="productSubscriptions")]
    """This should be deprecated, use productEnablements instead"""

    salesforce_account_industry: Annotated[str, PropertyInfo(alias="salesforceAccountIndustry")]
    """Company or organization industry"""

    send_email: Annotated[bool, PropertyInfo(alias="sendEmail")]
    """Send email to org owner or not. Default is true"""

    type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"]


class OrgOwner(TypedDict, total=False):
    email: Required[str]
    """Email address of the org owner."""

    full_name: Required[Annotated[str, PropertyInfo(alias="fullName")]]
    """Org owner name."""

    last_login_date: Annotated[str, PropertyInfo(alias="lastLoginDate")]
    """Last time the org owner logged in."""


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


class ProductSubscription(TypedDict, total=False):
    product_name: Required[Annotated[str, PropertyInfo(alias="productName")]]
    """Product Name (NVAIE, BASE_COMMAND, FleetCommand, REGISTRY, etc)."""

    id: str
    """Unique entitlement identifier"""

    ems_entitlement_type: Annotated[
        Literal["EMS_EVAL", "EMS_NFR", "EMS_COMMERICAL", "EMS_COMMERCIAL"], PropertyInfo(alias="emsEntitlementType")
    ]
    """EMS Subscription type. (options: EMS_EVAL, EMS_NFR and EMS_COMMERCIAL)"""

    expiration_date: Annotated[str, PropertyInfo(alias="expirationDate")]
    """Date on which the subscription expires.

    The subscription is invalid after this date. (yyyy-MM-dd)
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Date on which the subscription becomes active. (yyyy-MM-dd)"""

    type: Literal["NGC_ADMIN_EVAL", "NGC_ADMIN_NFR", "NGC_ADMIN_COMMERCIAL"]
    """Subscription type.

    (options: NGC_ADMIN_EVAL, NGC_ADMIN_NFR, NGC_ADMIN_COMMERCIAL)
    """
