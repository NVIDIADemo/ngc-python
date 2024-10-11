# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.team import Team

__all__ = [
    "UserListResponse",
    "Role",
    "RoleOrg",
    "RoleOrgAlternateContact",
    "RoleOrgInfinityManagerSettings",
    "RoleOrgOrgOwner",
    "RoleOrgProductEnablement",
    "RoleOrgProductEnablementPoDetail",
    "RoleOrgProductSubscription",
    "RoleOrgRepoScanSettings",
    "RoleOrgUsersInfo",
    "RoleTargetSystemUserIdentifier",
    "StorageQuota",
    "UserMetadata",
]


class RoleOrgAlternateContact(BaseModel):
    email: Optional[str] = None
    """Alternate contact's email."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """Full name of the alternate contact."""


class RoleOrgInfinityManagerSettings(BaseModel):
    infinity_manager_enabled: Optional[bool] = FieldInfo(alias="infinityManagerEnabled", default=None)
    """Enable the infinity manager or not. Used both in org and team level object"""

    infinity_manager_enable_team_override: Optional[bool] = FieldInfo(
        alias="infinityManagerEnableTeamOverride", default=None
    )
    """Allow override settings at team level. Only used in org level object"""


class RoleOrgOrgOwner(BaseModel):
    email: str
    """Email address of the org owner."""

    full_name: str = FieldInfo(alias="fullName")
    """Org owner name."""

    last_login_date: Optional[str] = FieldInfo(alias="lastLoginDate", default=None)
    """Last time the org owner logged in."""


class RoleOrgProductEnablementPoDetail(BaseModel):
    entitlement_id: Optional[str] = FieldInfo(alias="entitlementId", default=None)
    """Entitlement identifier."""

    pk_id: Optional[str] = FieldInfo(alias="pkId", default=None)
    """PAK (Product Activation Key) identifier."""


class RoleOrgProductEnablement(BaseModel):
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

    po_details: Optional[List[RoleOrgProductEnablementPoDetail]] = FieldInfo(alias="poDetails", default=None)


class RoleOrgProductSubscription(BaseModel):
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


class RoleOrgRepoScanSettings(BaseModel):
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


class RoleOrgUsersInfo(BaseModel):
    total_users: Optional[int] = FieldInfo(alias="totalUsers", default=None)
    """Total number of users."""


class RoleOrg(BaseModel):
    id: Optional[int] = None
    """Unique Id of this team."""

    alternate_contact: Optional[RoleOrgAlternateContact] = FieldInfo(alias="alternateContact", default=None)
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

    infinity_manager_settings: Optional[RoleOrgInfinityManagerSettings] = FieldInfo(
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

    org_owner: Optional[RoleOrgOrgOwner] = FieldInfo(alias="orgOwner", default=None)
    """Org owner."""

    org_owners: Optional[List[RoleOrgOrgOwner]] = FieldInfo(alias="orgOwners", default=None)
    """Org owners"""

    pec_sfdc_id: Optional[str] = FieldInfo(alias="pecSfdcId", default=None)
    """Product end customer salesforce.com Id (external customer Id).

    pecSfdcId is for EMS (entitlement management service) to track external paid
    customer.
    """

    product_enablements: Optional[List[RoleOrgProductEnablement]] = FieldInfo(alias="productEnablements", default=None)

    product_subscriptions: Optional[List[RoleOrgProductSubscription]] = FieldInfo(
        alias="productSubscriptions", default=None
    )

    repo_scan_settings: Optional[RoleOrgRepoScanSettings] = FieldInfo(alias="repoScanSettings", default=None)
    """Repo scan setting definition"""

    type: Optional[Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"]] = None

    users_info: Optional[RoleOrgUsersInfo] = FieldInfo(alias="usersInfo", default=None)
    """Users information."""


class RoleTargetSystemUserIdentifier(BaseModel):
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


class Role(BaseModel):
    org: Optional[RoleOrg] = None
    """Information about the Organization"""

    org_roles: Optional[List[str]] = FieldInfo(alias="orgRoles", default=None)
    """List of org role types that the user have"""

    role_types: Optional[List[str]] = FieldInfo(alias="roleTypes", default=None)
    """DEPRECATED - List of role types that the user have"""

    target_system_user_identifier: Optional[RoleTargetSystemUserIdentifier] = FieldInfo(
        alias="targetSystemUserIdentifier", default=None
    )
    """Information about the user who is attempting to run the job"""

    team: Optional[Team] = None
    """Information about the team"""

    team_roles: Optional[List[str]] = FieldInfo(alias="teamRoles", default=None)
    """List of team role types that the user have"""


class StorageQuota(BaseModel):
    ace_id: Optional[int] = FieldInfo(alias="aceId", default=None)
    """id of the ace"""

    ace_name: Optional[str] = FieldInfo(alias="aceName", default=None)
    """name of the ace"""

    available: Optional[int] = None
    """Available space in bytes"""

    dataset_count: Optional[int] = FieldInfo(alias="datasetCount", default=None)
    """Number of datasets that are a part of user's used storage"""

    datasets_usage: Optional[int] = FieldInfo(alias="datasetsUsage", default=None)
    """Space used by datasets in bytes"""

    org_name: Optional[str] = FieldInfo(alias="orgName", default=None)
    """The org name that this user quota tied to. This is needed for analytics"""

    quota: Optional[int] = None
    """Assigned quota in bytes"""

    resultset_count: Optional[int] = FieldInfo(alias="resultsetCount", default=None)
    """Number of resultsets that are a part of user's used storage"""

    resultsets_usage: Optional[int] = FieldInfo(alias="resultsetsUsage", default=None)
    """Space used by resultsets in bytes"""

    storage_cluster_description: Optional[str] = FieldInfo(alias="storageClusterDescription", default=None)
    """Description of this storage cluster"""

    storage_cluster_name: Optional[str] = FieldInfo(alias="storageClusterName", default=None)
    """Name of storage cluster"""

    storage_cluster_uuid: Optional[str] = FieldInfo(alias="storageClusterUuid", default=None)
    """Identifier to this storage cluster"""

    workspaces_count: Optional[int] = FieldInfo(alias="workspacesCount", default=None)
    """Number of workspaces that are a part of user's used storage"""

    workspaces_usage: Optional[int] = FieldInfo(alias="workspacesUsage", default=None)
    """Space used by workspaces in bytes"""


class UserMetadata(BaseModel):
    company: Optional[str] = None
    """Name of the company"""

    company_url: Optional[str] = FieldInfo(alias="companyUrl", default=None)
    """Company URL"""

    country: Optional[str] = None
    """Country of the user"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """User's first name"""

    industry: Optional[str] = None
    """Industry segment"""

    interest: Optional[List[str]] = None
    """List of development areas that user has interest"""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """User's last name"""

    role: Optional[str] = None
    """Role of the user in the company"""


class UserListResponse(BaseModel):
    id: Optional[int] = None
    """unique Id of this user."""

    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """unique auth client id of this user."""

    created_date: Optional[str] = FieldInfo(alias="createdDate", default=None)
    """Created date for this user"""

    email: Optional[str] = None
    """Email address of the user. This should be unique."""

    first_login_date: Optional[str] = FieldInfo(alias="firstLoginDate", default=None)
    """Last time the user logged in"""

    has_beta_access: Optional[bool] = FieldInfo(alias="hasBetaAccess", default=None)
    """Determines if the user has beta access"""

    has_profile: Optional[bool] = FieldInfo(alias="hasProfile", default=None)
    """indicate if user profile has been completed."""

    has_signed_ai_foundry_partnerships_eula: Optional[bool] = FieldInfo(
        alias="hasSignedAiFoundryPartnershipsEULA", default=None
    )
    """indicates if user has accepted AI Foundry Partnerships eula"""

    has_signed_base_command_eula: Optional[bool] = FieldInfo(alias="hasSignedBaseCommandEULA", default=None)
    """indicates if user has accepted Base Command End User License Agreement."""

    has_signed_base_command_manager_eula: Optional[bool] = FieldInfo(
        alias="hasSignedBaseCommandManagerEULA", default=None
    )
    """indicates if user has accepted Base Command Manager End User License Agreement."""

    has_signed_bio_ne_mo_eula: Optional[bool] = FieldInfo(alias="hasSignedBioNeMoEULA", default=None)
    """indicates if user has accepted BioNeMo End User License Agreement."""

    has_signed_container_publishing_eula: Optional[bool] = FieldInfo(
        alias="hasSignedContainerPublishingEULA", default=None
    )
    """indicates if user has accepted container publishing eula"""

    has_signed_cu_opt_eula: Optional[bool] = FieldInfo(alias="hasSignedCuOptEULA", default=None)
    """indicates if user has accepted CuOpt eula"""

    has_signed_earth2_eula: Optional[bool] = FieldInfo(alias="hasSignedEarth2EULA", default=None)
    """indicates if user has accepted Earth-2 eula"""

    has_signed_egx_eula: Optional[bool] = FieldInfo(alias="hasSignedEgxEULA", default=None)
    """[Deprecated] indicates if user has accepted EGX End User License Agreement."""

    has_signed_eula: Optional[bool] = FieldInfo(alias="hasSignedEULA", default=None)
    """Determines if the user has signed the NGC End User License Agreement."""

    has_signed_fleet_command_eula: Optional[bool] = FieldInfo(alias="hasSignedFleetCommandEULA", default=None)
    """indicates if user has accepted Fleet Command End User License Agreement."""

    has_signed_llm_eula: Optional[bool] = FieldInfo(alias="hasSignedLlmEULA", default=None)
    """indicates if user has accepted LLM End User License Agreement."""

    has_signed_nvaieeula: Optional[bool] = FieldInfo(alias="hasSignedNVAIEEULA", default=None)
    """indicates if user has accepted Fleet Command End User License Agreement."""

    has_signed_nvidia_eula: Optional[bool] = FieldInfo(alias="hasSignedNvidiaEULA", default=None)
    """Determines if the user has signed the NVIDIA End User License Agreement."""

    has_signed_nvqceula: Optional[bool] = FieldInfo(alias="hasSignedNVQCEULA", default=None)
    """indicates if user has accepted Nvidia Quantum Cloud End User License Agreement."""

    has_signed_omniverse_eula: Optional[bool] = FieldInfo(alias="hasSignedOmniverseEULA", default=None)
    """indicates if user has accepted Omniverse End User License Agreement."""

    has_signed_privacy_policy: Optional[bool] = FieldInfo(alias="hasSignedPrivacyPolicy", default=None)
    """Determines if the user has signed the Privacy Policy."""

    has_signed_third_party_registry_share_eula: Optional[bool] = FieldInfo(
        alias="hasSignedThirdPartyRegistryShareEULA", default=None
    )
    """
    indicates if user has consented to share their registration info with other
    parties
    """

    has_subscribed_to_email: Optional[bool] = FieldInfo(alias="hasSubscribedToEmail", default=None)
    """Determines if the user has opted in email subscription."""

    idp_type: Optional[Literal["NVIDIA", "ENTERPRISE"]] = FieldInfo(alias="idpType", default=None)
    """Type of IDP, Identity Provider. Used for login."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)
    """Determines if the user is active or not."""

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)
    """Indicates if user was deleted from the system."""

    is_saml: Optional[bool] = FieldInfo(alias="isSAML", default=None)
    """Determines if the user is a SAML account or not."""

    job_position_title: Optional[str] = FieldInfo(alias="jobPositionTitle", default=None)
    """Title of user's job position."""

    last_login_date: Optional[str] = FieldInfo(alias="lastLoginDate", default=None)
    """Last time the user logged in"""

    name: Optional[str] = None
    """user name"""

    roles: Optional[List[Role]] = None
    """List of roles that the user have"""

    starfleet_id: Optional[str] = FieldInfo(alias="starfleetId", default=None)
    """unique starfleet id of this user."""

    storage_quota: Optional[List[StorageQuota]] = FieldInfo(alias="storageQuota", default=None)
    """Storage quota for this user."""

    updated_date: Optional[str] = FieldInfo(alias="updatedDate", default=None)
    """Updated date for this user"""

    user_metadata: Optional[UserMetadata] = FieldInfo(alias="userMetadata", default=None)
    """Metadata information about the user."""
