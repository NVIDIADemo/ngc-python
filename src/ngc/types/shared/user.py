# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "User",
    "RequestStatus",
    "UserRole",
    "UserRoleOrg",
    "UserRoleOrgAlternateContact",
    "UserRoleOrgInfinityManagerSettings",
    "UserRoleOrgOrgOwner",
    "UserRoleOrgProductEnablement",
    "UserRoleOrgProductEnablementPoDetail",
    "UserRoleOrgProductSubscription",
    "UserRoleOrgRepoScanSettings",
    "UserRoleOrgUsersInfo",
    "UserRoleTargetSystemUserIdentifier",
    "UserRoleTeam",
    "UserRoleTeamInfinityManagerSettings",
    "UserRoleTeamRepoScanSettings",
]


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


class UserRoleOrgAlternateContact(BaseModel):
    email: Optional[str] = None
    """Alternate contact's email."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """Full name of the alternate contact."""


class UserRoleOrgInfinityManagerSettings(BaseModel):
    infinity_manager_enabled: Optional[bool] = FieldInfo(alias="infinityManagerEnabled", default=None)
    """Enable the infinity manager or not. Used both in org and team level object"""

    infinity_manager_enable_team_override: Optional[bool] = FieldInfo(
        alias="infinityManagerEnableTeamOverride", default=None
    )
    """Allow override settings at team level. Only used in org level object"""


class UserRoleOrgOrgOwner(BaseModel):
    email: str
    """Email address of the org owner."""

    full_name: str = FieldInfo(alias="fullName")
    """Org owner name."""

    last_login_date: Optional[str] = FieldInfo(alias="lastLoginDate", default=None)
    """Last time the org owner logged in."""


class UserRoleOrgProductEnablementPoDetail(BaseModel):
    entitlement_id: Optional[str] = FieldInfo(alias="entitlementId", default=None)
    """Entitlement identifier."""

    pk_id: Optional[str] = FieldInfo(alias="pkId", default=None)
    """PAK (Product Activation Key) identifier."""


class UserRoleOrgProductEnablement(BaseModel):
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

    po_details: Optional[List[UserRoleOrgProductEnablementPoDetail]] = FieldInfo(alias="poDetails", default=None)


class UserRoleOrgProductSubscription(BaseModel):
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


class UserRoleOrgRepoScanSettings(BaseModel):
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


class UserRoleOrgUsersInfo(BaseModel):
    total_users: Optional[int] = FieldInfo(alias="totalUsers", default=None)
    """Total number of users."""


class UserRoleOrg(BaseModel):
    id: Optional[int] = None
    """Unique Id of this team."""

    alternate_contact: Optional[UserRoleOrgAlternateContact] = FieldInfo(alias="alternateContact", default=None)
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

    infinity_manager_settings: Optional[UserRoleOrgInfinityManagerSettings] = FieldInfo(
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

    org_owner: Optional[UserRoleOrgOrgOwner] = FieldInfo(alias="orgOwner", default=None)
    """Org owner."""

    org_owners: Optional[List[UserRoleOrgOrgOwner]] = FieldInfo(alias="orgOwners", default=None)
    """Org owners"""

    pec_sfdc_id: Optional[str] = FieldInfo(alias="pecSfdcId", default=None)
    """Product end customer salesforce.com Id (external customer Id).

    pecSfdcId is for EMS (entitlement management service) to track external paid
    customer.
    """

    product_enablements: Optional[List[UserRoleOrgProductEnablement]] = FieldInfo(
        alias="productEnablements", default=None
    )

    product_subscriptions: Optional[List[UserRoleOrgProductSubscription]] = FieldInfo(
        alias="productSubscriptions", default=None
    )

    repo_scan_settings: Optional[UserRoleOrgRepoScanSettings] = FieldInfo(alias="repoScanSettings", default=None)
    """Repo scan setting definition"""

    type: Optional[Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"]] = None

    users_info: Optional[UserRoleOrgUsersInfo] = FieldInfo(alias="usersInfo", default=None)
    """Users information."""


class UserRoleTargetSystemUserIdentifier(BaseModel):
    gid: Optional[int] = None
    """gid of the user on this team"""

    org_name: Optional[str] = FieldInfo(alias="orgName", default=None)
    """Org context for the job"""

    starfleet_id: Optional[str] = FieldInfo(alias="starfleetId", default=None)
    """Starfleet ID of the user creating the job."""

    team_name: Optional[str] = FieldInfo(alias="teamName", default=None)
    """Team context for the job"""

    uid: Optional[int] = None
    """uid of the user on this team"""

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)
    """Unique ID of the user who submitted the job"""


class UserRoleTeamInfinityManagerSettings(BaseModel):
    infinity_manager_enabled: Optional[bool] = FieldInfo(alias="infinityManagerEnabled", default=None)
    """Enable the infinity manager or not. Used both in org and team level object"""

    infinity_manager_enable_team_override: Optional[bool] = FieldInfo(
        alias="infinityManagerEnableTeamOverride", default=None
    )
    """Allow override settings at team level. Only used in org level object"""


class UserRoleTeamRepoScanSettings(BaseModel):
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


class UserRoleTeam(BaseModel):
    id: Optional[int] = None
    """unique Id of this team."""

    description: Optional[str] = None
    """description of the team"""

    infinity_manager_settings: Optional[UserRoleTeamInfinityManagerSettings] = FieldInfo(
        alias="infinityManagerSettings", default=None
    )
    """Infinity manager setting definition"""

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)
    """indicates if the team is deleted or not"""

    name: Optional[str] = None
    """team name"""

    repo_scan_settings: Optional[UserRoleTeamRepoScanSettings] = FieldInfo(alias="repoScanSettings", default=None)
    """Repo scan setting definition"""


class UserRole(BaseModel):
    org: Optional[UserRoleOrg] = None
    """Information about the Organization"""

    org_roles: Optional[List[str]] = FieldInfo(alias="orgRoles", default=None)
    """List of org role types that the user have"""

    role_types: Optional[List[str]] = FieldInfo(alias="roleTypes", default=None)
    """DEPRECATED - List of role types that the user have"""

    target_system_user_identifier: Optional[UserRoleTargetSystemUserIdentifier] = FieldInfo(
        alias="targetSystemUserIdentifier", default=None
    )
    """Information about the user who is attempting to run the job"""

    team: Optional[UserRoleTeam] = None
    """Information about the team"""

    team_roles: Optional[List[str]] = FieldInfo(alias="teamRoles", default=None)
    """List of team role types that the user have"""


class User(BaseModel):
    activation_token: Optional[str] = FieldInfo(alias="activationToken", default=None)
    """token needed to activate the user to enable login and other features"""

    nca_role: Optional[Literal["UNKNOWN", "ADMINISTRATOR", "MEMBER", "OWNER", "PENDING"]] = FieldInfo(
        alias="ncaRole", default=None
    )
    """NCA role"""

    request_status: Optional[RequestStatus] = FieldInfo(alias="requestStatus", default=None)

    user: Optional[User] = None
    """information about the user"""

    user_roles: Optional[List[UserRole]] = FieldInfo(alias="userRoles", default=None)
    """DEPRECATED - Please use roles inside user"""
