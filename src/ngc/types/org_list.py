# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OrgList",
    "Organization",
    "OrganizationAlternateContact",
    "OrganizationInfinityManagerSettings",
    "OrganizationOrgOwner",
    "OrganizationProductEnablement",
    "OrganizationProductEnablementPoDetail",
    "OrganizationProductSubscription",
    "OrganizationRepoScanSettings",
    "OrganizationUsersInfo",
    "PaginationInfo",
    "RequestStatus",
]


class OrganizationAlternateContact(BaseModel):
    email: Optional[str] = None
    """Alternate contact's email."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """Full name of the alternate contact."""


class OrganizationInfinityManagerSettings(BaseModel):
    infinity_manager_enabled: Optional[bool] = FieldInfo(alias="infinityManagerEnabled", default=None)
    """Enable the infinity manager or not. Used both in org and team level object"""

    infinity_manager_enable_team_override: Optional[bool] = FieldInfo(
        alias="infinityManagerEnableTeamOverride", default=None
    )
    """Allow override settings at team level. Only used in org level object"""


class OrganizationOrgOwner(BaseModel):
    email: str
    """Email address of the org owner."""

    full_name: str = FieldInfo(alias="fullName")
    """Org owner name."""

    last_login_date: Optional[str] = FieldInfo(alias="lastLoginDate", default=None)
    """Last time the org owner logged in."""


class OrganizationProductEnablementPoDetail(BaseModel):
    entitlement_id: Optional[str] = FieldInfo(alias="entitlementId", default=None)
    """Entitlement identifier."""

    pk_id: Optional[str] = FieldInfo(alias="pkId", default=None)
    """PAK (Product Activation Key) identifier."""


class OrganizationProductEnablement(BaseModel):
    product_name: str = FieldInfo(alias="productName")
    """Product Name (NVAIE, BASE_COMMAND, REGISTRY, etc)"""

    type: Literal[
        "NGC_ADMIN_EVAL",
        "NGC_ADMIN_NFR",
        "NGC_ADMIN_COMMERCIAL",
        "EMS_EVAL",
        "EMS_NFR",
        "EMS_COMMERCIAL",
        "NGC_ADMIN_DEVELOPER",
    ]
    """Product Enablement Types"""

    expiration_date: Optional[str] = FieldInfo(alias="expirationDate", default=None)
    """Date on which the subscription expires.

    The subscription is invalid after this date. (yyyy-MM-dd)
    """

    po_details: Optional[List[OrganizationProductEnablementPoDetail]] = FieldInfo(alias="poDetails", default=None)


class OrganizationProductSubscription(BaseModel):
    product_name: str = FieldInfo(alias="productName")
    """Product Name (NVAIE, BASE_COMMAND, FleetCommand, REGISTRY, etc)."""

    id: Optional[str] = None
    """Unique entitlement identifier"""

    ems_entitlement_type: Optional[Literal["EMS_EVAL", "EMS_NFR", "EMS_COMMERICAL", "EMS_COMMERCIAL"]] = FieldInfo(
        alias="emsEntitlementType", default=None
    )
    """EMS Subscription type. (options: EMS_EVAL, EMS_NFR and EMS_COMMERCIAL)"""

    expiration_date: Optional[str] = FieldInfo(alias="expirationDate", default=None)
    """Date on which the subscription expires.

    The subscription is invalid after this date. (yyyy-MM-dd)
    """

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)
    """Date on which the subscription becomes active. (yyyy-MM-dd)"""

    type: Optional[Literal["NGC_ADMIN_EVAL", "NGC_ADMIN_NFR", "NGC_ADMIN_COMMERCIAL"]] = None
    """Subscription type.

    (options: NGC_ADMIN_EVAL, NGC_ADMIN_NFR, NGC_ADMIN_COMMERCIAL)
    """


class OrganizationRepoScanSettings(BaseModel):
    repo_scan_allow_override: Optional[bool] = FieldInfo(alias="repoScanAllowOverride", default=None)
    """Allow org admin to override the org level repo scan settings"""

    repo_scan_by_default: Optional[bool] = FieldInfo(alias="repoScanByDefault", default=None)
    """Allow repository scanning by default"""

    repo_scan_enabled: Optional[bool] = FieldInfo(alias="repoScanEnabled", default=None)
    """Enable the repository scan or not. Only used in org level object"""

    repo_scan_enable_notifications: Optional[bool] = FieldInfo(alias="repoScanEnableNotifications", default=None)
    """Sends notification to end user after scanning is done"""

    repo_scan_enable_team_override: Optional[bool] = FieldInfo(alias="repoScanEnableTeamOverride", default=None)
    """Allow override settings at team level. Only used in org level object"""

    repo_scan_show_results: Optional[bool] = FieldInfo(alias="repoScanShowResults", default=None)
    """Allow showing scan results to CLI or UI"""


class OrganizationUsersInfo(BaseModel):
    total_users: Optional[int] = FieldInfo(alias="totalUsers", default=None)
    """Total number of users."""


class Organization(BaseModel):
    id: Optional[int] = None
    """Unique Id of this team."""

    alternate_contact: Optional[OrganizationAlternateContact] = FieldInfo(alias="alternateContact", default=None)
    """Org Owner Alternate Contact"""

    billing_account_id: Optional[str] = FieldInfo(alias="billingAccountId", default=None)
    """Billing account ID."""

    can_add_on: Optional[bool] = FieldInfo(alias="canAddOn", default=None)
    """Identifies if the org can be reused."""

    country: Optional[str] = None
    """ISO country code of the organization."""

    description: Optional[str] = None
    """Optional description of the organization."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Name of the organization that will be shown to users."""

    idp_id: Optional[str] = FieldInfo(alias="idpId", default=None)
    """Identity Provider ID."""

    industry: Optional[str] = None
    """Industry of the organization."""

    infinity_manager_settings: Optional[OrganizationInfinityManagerSettings] = FieldInfo(
        alias="infinityManagerSettings", default=None
    )
    """Infinity manager setting definition"""

    is_dataset_service_enabled: Optional[bool] = FieldInfo(alias="isDatasetServiceEnabled", default=None)
    """Dataset Service enable flag for an organization"""

    is_internal: Optional[bool] = FieldInfo(alias="isInternal", default=None)
    """Is NVIDIA internal org or not"""

    is_proto: Optional[bool] = FieldInfo(alias="isProto", default=None)
    """Indicates when the org is a proto org"""

    is_quick_start_enabled: Optional[bool] = FieldInfo(alias="isQuickStartEnabled", default=None)
    """Quick Start enable flag for an organization"""

    is_registry_sse_enabled: Optional[bool] = FieldInfo(alias="isRegistrySSEEnabled", default=None)
    """If a server side encryption is enabled for private registry (models, resources)"""

    is_secrets_manager_service_enabled: Optional[bool] = FieldInfo(alias="isSecretsManagerServiceEnabled", default=None)
    """Secrets Manager Service enable flag for an organization"""

    is_secure_credential_sharing_service_enabled: Optional[bool] = FieldInfo(
        alias="isSecureCredentialSharingServiceEnabled", default=None
    )
    """Secure Credential Sharing Service enable flag for an organization"""

    is_separate_influx_db_used: Optional[bool] = FieldInfo(alias="isSeparateInfluxDbUsed", default=None)
    """If a separate influx db used for an organization in BCP for job telemetry"""

    name: Optional[str] = None
    """Organization name."""

    nan: Optional[str] = None
    """NVIDIA Cloud Account Number."""

    org_owner: Optional[OrganizationOrgOwner] = FieldInfo(alias="orgOwner", default=None)
    """Org owner."""

    org_owners: Optional[List[OrganizationOrgOwner]] = FieldInfo(alias="orgOwners", default=None)
    """Org owners"""

    pec_sfdc_id: Optional[str] = FieldInfo(alias="pecSfdcId", default=None)
    """Product end customer salesforce.com Id (external customer Id).

    pecSfdcId is for EMS (entitlement management service) to track external paid
    customer.
    """

    product_enablements: Optional[List[OrganizationProductEnablement]] = FieldInfo(
        alias="productEnablements", default=None
    )

    product_subscriptions: Optional[List[OrganizationProductSubscription]] = FieldInfo(
        alias="productSubscriptions", default=None
    )

    repo_scan_settings: Optional[OrganizationRepoScanSettings] = FieldInfo(alias="repoScanSettings", default=None)
    """Repo scan setting definition"""

    type: Optional[Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"]] = None

    users_info: Optional[OrganizationUsersInfo] = FieldInfo(alias="usersInfo", default=None)
    """Users information."""


class PaginationInfo(BaseModel):
    index: Optional[int] = None
    """Page index of results"""

    next_page: Optional[str] = FieldInfo(alias="nextPage", default=None)
    """Serialized pointer to the next results page.

    Should be used for fetching next page. Can be empty
    """

    size: Optional[int] = None
    """Number of results in page"""

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
    """Total number of pages available"""

    total_results: Optional[int] = FieldInfo(alias="totalResults", default=None)
    """Total number of results available"""


class RequestStatus(BaseModel):
    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)

    server_id: Optional[str] = FieldInfo(alias="serverId", default=None)

    status_code: Optional[
        Literal[
            "UNKNOWN",
            "SUCCESS",
            "UNAUTHORIZED",
            "PAYMENT_REQUIRED",
            "FORBIDDEN",
            "TIMEOUT",
            "EXISTS",
            "NOT_FOUND",
            "INTERNAL_ERROR",
            "INVALID_REQUEST",
            "INVALID_REQUEST_VERSION",
            "INVALID_REQUEST_DATA",
            "METHOD_NOT_ALLOWED",
            "CONFLICT",
            "UNPROCESSABLE_ENTITY",
            "TOO_MANY_REQUESTS",
            "INSUFFICIENT_STORAGE",
            "SERVICE_UNAVAILABLE",
            "PAYLOAD_TOO_LARGE",
            "NOT_ACCEPTABLE",
            "UNAVAILABLE_FOR_LEGAL_REASONS",
            "BAD_GATEWAY",
        ]
    ] = FieldInfo(alias="statusCode", default=None)
    """Describes response status reported by the server."""

    status_description: Optional[str] = FieldInfo(alias="statusDescription", default=None)


class OrgList(BaseModel):
    organizations: Optional[List[Organization]] = None

    pagination_info: Optional[PaginationInfo] = FieldInfo(alias="paginationInfo", default=None)
    """object that describes the pagination information"""

    request_status: Optional[RequestStatus] = FieldInfo(alias="requestStatus", default=None)
