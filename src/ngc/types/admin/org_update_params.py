# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "OrgUpdateParams",
    "AlternateContact",
    "InfinityManagerSettings",
    "OrgOwner",
    "ProductEnablement",
    "ProductEnablementPoDetail",
    "ProductSubscription",
    "RepoScanSettings",
]


class OrgUpdateParams(TypedDict, total=False):
    alternate_contact: Annotated[AlternateContact, PropertyInfo(alias="alternateContact")]
    """Org Owner Alternate Contact"""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Name of the company"""

    description: str
    """optional description of the organization"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Name of the organization that will be shown to users."""

    idp_id: Annotated[str, PropertyInfo(alias="idpId")]
    """Identity Provider ID."""

    infinity_manager_settings: Annotated[InfinityManagerSettings, PropertyInfo(alias="infinityManagerSettings")]
    """Infinity manager setting definition"""

    is_dataset_service_enabled: Annotated[bool, PropertyInfo(alias="isDatasetServiceEnabled")]
    """Dataset Service enable flag for an organization"""

    is_internal: Annotated[bool, PropertyInfo(alias="isInternal")]
    """Is NVIDIA internal org or not"""

    is_quick_start_enabled: Annotated[bool, PropertyInfo(alias="isQuickStartEnabled")]
    """Quick Start enable flag for an organization"""

    is_registry_sse_enabled: Annotated[bool, PropertyInfo(alias="isRegistrySSEEnabled")]
    """If a server side encryption is enabled for private registry (models, resources)"""

    is_secrets_manager_service_enabled: Annotated[bool, PropertyInfo(alias="isSecretsManagerServiceEnabled")]
    """Secrets Manager Service enable flag for an organization"""

    is_secure_credential_sharing_service_enabled: Annotated[
        bool, PropertyInfo(alias="isSecureCredentialSharingServiceEnabled")
    ]
    """Secure Credential Sharing Service enable flag for an organization"""

    is_separate_influx_db_used: Annotated[bool, PropertyInfo(alias="isSeparateInfluxDbUsed")]
    """
    If a separate influx db used for an organization in Base Command Platform job
    telemetry
    """

    org_owner: Annotated[OrgOwner, PropertyInfo(alias="orgOwner")]
    """Org owner."""

    org_owners: Annotated[Iterable[OrgOwner], PropertyInfo(alias="orgOwners")]
    """Org owners"""

    pec_name: Annotated[str, PropertyInfo(alias="pecName")]
    """product end customer name for enterprise(Fleet Command) product"""

    pec_sfdc_id: Annotated[str, PropertyInfo(alias="pecSfdcId")]
    """
    product end customer salesforce.com Id (external customer Id) for
    enterprise(Fleet Command) product
    """

    product_enablements: Annotated[Iterable[ProductEnablement], PropertyInfo(alias="productEnablements")]

    product_subscriptions: Annotated[Iterable[ProductSubscription], PropertyInfo(alias="productSubscriptions")]

    repo_scan_settings: Annotated[RepoScanSettings, PropertyInfo(alias="repoScanSettings")]
    """Repo scan setting definition"""

    type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"]


class AlternateContact(TypedDict, total=False):
    email: str
    """Alternate contact's email."""

    full_name: Annotated[str, PropertyInfo(alias="fullName")]
    """Full name of the alternate contact."""


class InfinityManagerSettings(TypedDict, total=False):
    infinity_manager_enabled: Annotated[bool, PropertyInfo(alias="infinityManagerEnabled")]
    """Enable the infinity manager or not. Used both in org and team level object"""

    infinity_manager_enable_team_override: Annotated[bool, PropertyInfo(alias="infinityManagerEnableTeamOverride")]
    """Allow override settings at team level. Only used in org level object"""


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


class RepoScanSettings(TypedDict, total=False):
    repo_scan_allow_override: Annotated[bool, PropertyInfo(alias="repoScanAllowOverride")]
    """Allow org admin to override the org level repo scan settings"""

    repo_scan_by_default: Annotated[bool, PropertyInfo(alias="repoScanByDefault")]
    """Allow repository scanning by default"""

    repo_scan_enabled: Annotated[bool, PropertyInfo(alias="repoScanEnabled")]
    """Enable the repository scan or not. Only used in org level object"""

    repo_scan_enable_notifications: Annotated[bool, PropertyInfo(alias="repoScanEnableNotifications")]
    """Sends notification to end user after scanning is done"""

    repo_scan_enable_team_override: Annotated[bool, PropertyInfo(alias="repoScanEnableTeamOverride")]
    """Allow override settings at team level. Only used in org level object"""

    repo_scan_show_results: Annotated[bool, PropertyInfo(alias="repoScanShowResults")]
    """Allow showing scan results to CLI or UI"""
