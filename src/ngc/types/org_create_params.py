# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgCreateParams", "OrgOwner", "ProductEnablement", "ProductEnablementPoDetail", "ProductSubscription"]


class OrgCreateParams(TypedDict, total=False):
    country: str
    """user country"""

    description: str
    """optional description of the organization"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Name of the organization that will be shown to users."""

    initiator: str
    """Identify the initiator of the org request"""

    is_internal: Annotated[bool, PropertyInfo(alias="isInternal")]
    """Is NVIDIA internal org or not"""

    name: str
    """Organization name"""

    nca_id: Annotated[str, PropertyInfo(alias="ncaId")]
    """NVIDIA Cloud Account Identifier"""

    nca_number: Annotated[str, PropertyInfo(alias="ncaNumber")]
    """NVIDIA Cloud Account Number"""

    org_owner: Annotated[OrgOwner, PropertyInfo(alias="orgOwner")]
    """Org owner."""

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

    proto_org_id: Annotated[str, PropertyInfo(alias="protoOrgId")]
    """Proto org identifier"""

    salesforce_account_industry: Annotated[str, PropertyInfo(alias="salesforceAccountIndustry")]
    """Company or organization industry"""

    send_email: Annotated[bool, PropertyInfo(alias="sendEmail")]
    """Send email to org owner or not. Default is true"""

    type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"]


class OrgOwner(TypedDict, total=False):
    email: Required[str]
    """Email address of the org owner."""

    full_name: Annotated[str, PropertyInfo(alias="fullName")]
    """Org owner name."""

    idp_id: Annotated[str, PropertyInfo(alias="idpId")]
    """Identity Provider ID of the org owner."""

    starfleet_id: Annotated[str, PropertyInfo(alias="starfleetId")]
    """Starfleet ID of the org owner."""


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
