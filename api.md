# Shared Types

```python
from ngc.types import Health, MeteringResultList, Team, TeamList, User, UserInvitationList, UserList
```

# Orgs

Types:

```python
from ngc.types import OrgList, OrgResponse, OrgListResponse
```

Methods:

- <code title="post /v3/orgs">client.orgs.<a href="./src/ngc/resources/orgs/orgs.py">create</a>(\*\*<a href="src/ngc/types/org_create_params.py">params</a>) -> <a href="./src/ngc/types/org_response.py">OrgResponse</a></code>
- <code title="get /v2/orgs/{org-name}">client.orgs.<a href="./src/ngc/resources/orgs/orgs.py">retrieve</a>(org_name) -> <a href="./src/ngc/types/org_response.py">OrgResponse</a></code>
- <code title="patch /v2/orgs/{org-name}">client.orgs.<a href="./src/ngc/resources/orgs/orgs.py">update</a>(org_name, \*\*<a href="src/ngc/types/org_update_params.py">params</a>) -> <a href="./src/ngc/types/org_response.py">OrgResponse</a></code>
- <code title="get /v2/orgs">client.orgs.<a href="./src/ngc/resources/orgs/orgs.py">list</a>(\*\*<a href="src/ngc/types/org_list_params.py">params</a>) -> <a href="./src/ngc/types/org_list_response.py">SyncPageNumberOrganizations[OrgListResponse]</a></code>

## Users

Types:

```python
from ngc.types.orgs import UserListResponse, UserDeleteResponse
```

Methods:

- <code title="post /v2/org/{org-name}/users">client.orgs.users.<a href="./src/ngc/resources/orgs/users/users.py">create</a>(org_name, \*\*<a href="src/ngc/types/orgs/user_create_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="get /v2/org/{org-name}/users">client.orgs.users.<a href="./src/ngc/resources/orgs/users/users.py">list</a>(org_name, \*\*<a href="src/ngc/types/orgs/user_list_params.py">params</a>) -> <a href="./src/ngc/types/orgs/user_list_response.py">SyncPageNumberUsers[UserListResponse]</a></code>
- <code title="delete /v3/orgs/{org-name}/users/{id}">client.orgs.users.<a href="./src/ngc/resources/orgs/users/users.py">delete</a>(id, \*, org_name, \*\*<a href="src/ngc/types/orgs/user_delete_params.py">params</a>) -> <a href="./src/ngc/types/orgs/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="patch /v3/orgs/{org-name}/users/{user-email-or-id}/add-role">client.orgs.users.<a href="./src/ngc/resources/orgs/users/users.py">add_role</a>(user_email_or_id, \*, org_name, \*\*<a href="src/ngc/types/orgs/user_add_role_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="delete /v3/orgs/{org-name}/users/{user-email-or-id}/remove-role">client.orgs.users.<a href="./src/ngc/resources/orgs/users/users.py">remove_role</a>(user_email_or_id, \*, org_name, \*\*<a href="src/ngc/types/orgs/user_remove_role_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="patch /v2/org/{org-name}/users/{id}/update-role">client.orgs.users.<a href="./src/ngc/resources/orgs/users/users.py">update_role</a>(id, \*, org_name, \*\*<a href="src/ngc/types/orgs/user_update_role_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>

### NcaInvitations

Methods:

- <code title="post /v3/orgs/{org-name}/users/nca-invitations">client.orgs.users.nca_invitations.<a href="./src/ngc/resources/orgs/users/nca_invitations.py">create</a>(org_name, \*\*<a href="src/ngc/types/orgs/users/nca_invitation_create_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>

## Teams

Types:

```python
from ngc.types.orgs import TeamResponse
```

Methods:

- <code title="get /v2/org/{org-name}/teams">client.orgs.teams.<a href="./src/ngc/resources/orgs/teams/teams.py">list</a>(org_name, \*\*<a href="src/ngc/types/orgs/team_list_params.py">params</a>) -> <a href="./src/ngc/types/shared/team.py">SyncPageNumberTeams[Team]</a></code>

### Users

Types:

```python
from ngc.types.orgs.teams import UserDeleteResponse
```

Methods:

- <code title="delete /v3/orgs/{org-name}/teams/{team-name}/users/{id}">client.orgs.teams.users.<a href="./src/ngc/resources/orgs/teams/users.py">delete</a>(id, \*, org_name, team_name, \*\*<a href="src/ngc/types/orgs/teams/user_delete_params.py">params</a>) -> <a href="./src/ngc/types/orgs/teams/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="patch /v3/orgs/{org-name}/teams/{team-name}/users/{user-email-or-id}/add-role">client.orgs.teams.users.<a href="./src/ngc/resources/orgs/teams/users.py">add_role</a>(user_email_or_id, \*, org_name, team_name, \*\*<a href="src/ngc/types/orgs/teams/user_add_role_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="delete /v3/orgs/{org-name}/teams/{team-name}/users/{user-email-or-id}/remove-role">client.orgs.teams.users.<a href="./src/ngc/resources/orgs/teams/users.py">remove_role</a>(user_email_or_id, \*, org_name, team_name, \*\*<a href="src/ngc/types/orgs/teams/user_remove_role_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>

### StarfleetIDs

Methods:

- <code title="get /v2/org/{org-name}/team/{team-name}/starfleetIds/{starfleet-id}">client.orgs.teams.starfleet_ids.<a href="./src/ngc/resources/orgs/teams/starfleet_ids.py">retrieve</a>(starfleet_id, \*, org_name, team_name) -> <a href="./src/ngc/types/shared/user.py">User</a></code>

### NcaInvitations

Methods:

- <code title="post /v3/orgs/{org-name}/teams/{team-name}/users/nca-invitations">client.orgs.teams.nca_invitations.<a href="./src/ngc/resources/orgs/teams/nca_invitations.py">create</a>(team_name, \*, org_name, \*\*<a href="src/ngc/types/orgs/teams/nca_invitation_create_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>

## ProtoOrg

Methods:

- <code title="post /v3/orgs/proto-org">client.orgs.proto_org.<a href="./src/ngc/resources/orgs/proto_org.py">create</a>(\*\*<a href="src/ngc/types/orgs/proto_org_create_params.py">params</a>) -> <a href="./src/ngc/types/org_response.py">OrgResponse</a></code>

## Credits

Types:

```python
from ngc.types.orgs import CreditsHistory
```

Methods:

- <code title="get /v2/orgs/{org-name}/credits">client.orgs.credits.<a href="./src/ngc/resources/orgs/credits.py">retrieve</a>(org_name) -> <a href="./src/ngc/types/orgs/credits_history.py">CreditsHistory</a></code>

## StarfleetIDs

Methods:

- <code title="get /v2/org/{org-name}/starfleetIds/{starfleet-id}">client.orgs.starfleet_ids.<a href="./src/ngc/resources/orgs/starfleet_ids.py">retrieve</a>(starfleet_id, \*, org_name) -> <a href="./src/ngc/types/shared/user.py">User</a></code>

## Metering

Methods:

- <code title="get /v2/org/{org-name}/metering">client.orgs.metering.<a href="./src/ngc/resources/orgs/metering/metering.py">retrieve_all</a>(org_name, \*\*<a href="src/ngc/types/orgs/metering_retrieve_all_params.py">params</a>) -> <a href="./src/ngc/types/shared/metering_result_list.py">MeteringResultList</a></code>

### Gpupeak

Methods:

- <code title="get /v2/org/{org-name}/meterings/gpupeak">client.orgs.metering.gpupeak.<a href="./src/ngc/resources/orgs/metering/gpupeak.py">retrieve_all</a>(org_name, \*\*<a href="src/ngc/types/orgs/metering/gpupeak_retrieve_all_params.py">params</a>) -> <a href="./src/ngc/types/shared/metering_result_list.py">MeteringResultList</a></code>

## AuditLogs

Types:

```python
from ngc.types.orgs import AuditLogsPresignedURL
```

Methods:

- <code title="get /v2/org/{org-name}/auditLogs/{log-id}">client.orgs.audit_logs.<a href="./src/ngc/resources/orgs/audit_logs.py">retrieve</a>(log_id, \*, org_name) -> <a href="./src/ngc/types/orgs/audit_logs_presigned_url.py">AuditLogsPresignedURL</a></code>

# Me

## APIKey

Types:

```python
from ngc.types.me import UserKeyResponse
```

Methods:

- <code title="get /v2/users/me">client.me.api_key.<a href="./src/ngc/resources/me/api_key.py">retrieve</a>(\*\*<a href="src/ngc/types/me/api_key_retrieve_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="patch /v2/users/me">client.me.api_key.<a href="./src/ngc/resources/me/api_key.py">update</a>(\*\*<a href="src/ngc/types/me/api_key_update_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="post /v2/users/me/api-key">client.me.api_key.<a href="./src/ngc/resources/me/api_key.py">create_api_key</a>() -> <a href="./src/ngc/types/me/user_key_response.py">UserKeyResponse</a></code>

# Admin

## Entitlements

Methods:

- <code title="get /v2/admin/entitlements">client.admin.entitlements.<a href="./src/ngc/resources/admin/entitlements.py">retrieve_all</a>(\*\*<a href="src/ngc/types/admin/entitlement_retrieve_all_params.py">params</a>) -> BinaryAPIResponse</code>

## Orgs

Types:

```python
from ngc.types.admin import OrgOrgOwnerBackfillResponse, OrgValidateResponse
```

Methods:

- <code title="post /v2/admin/orgs">client.admin.orgs.<a href="./src/ngc/resources/admin/orgs/orgs.py">create</a>(\*\*<a href="src/ngc/types/admin/org_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v3/admin/org/{org-name}">client.admin.orgs.<a href="./src/ngc/resources/admin/orgs/orgs.py">retrieve</a>(org_name) -> BinaryAPIResponse</code>
- <code title="patch /v3/admin/org/{org-name}">client.admin.orgs.<a href="./src/ngc/resources/admin/orgs/orgs.py">update</a>(org_name, \*\*<a href="src/ngc/types/admin/org_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v2/admin/backfill-orgs-to-kratos">client.admin.orgs.<a href="./src/ngc/resources/admin/orgs/orgs.py">backfill_orgs_to_kratos</a>() -> BinaryAPIResponse</code>
- <code title="post /v2/admin/org/{org-name}/enablement">client.admin.orgs.<a href="./src/ngc/resources/admin/orgs/orgs.py">enable</a>(org_name, \*\*<a href="src/ngc/types/admin/org_enable_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v2/admin/org/{org-name}/org-owner-backfill">client.admin.orgs.<a href="./src/ngc/resources/admin/orgs/orgs.py">org_owner_backfill</a>(org_name) -> <a href="./src/ngc/types/admin/org_org_owner_backfill_response.py">OrgOrgOwnerBackfillResponse</a></code>
- <code title="get /v3/orgs/proto-org/validate">client.admin.orgs.<a href="./src/ngc/resources/admin/orgs/orgs.py">validate</a>(\*\*<a href="src/ngc/types/admin/org_validate_params.py">params</a>) -> <a href="./src/ngc/types/admin/org_validate_response.py">OrgValidateResponse</a></code>

### Users

Types:

```python
from ngc.types.admin.orgs import UserRemoveResponse
```

Methods:

- <code title="post /v2/admin/org/{org-name}/users">client.admin.orgs.users.<a href="./src/ngc/resources/admin/orgs/users.py">create</a>(org_name, \*\*<a href="src/ngc/types/admin/orgs/user_create_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="get /v3/orgs/{org-name}/users/{user-email-or-id}">client.admin.orgs.users.<a href="./src/ngc/resources/admin/orgs/users.py">retrieve</a>(user_email_or_id, \*, org_name) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="post /v2/admin/org/{org-name}/users/{id}">client.admin.orgs.users.<a href="./src/ngc/resources/admin/orgs/users.py">add</a>(id, \*, org_name, \*\*<a href="src/ngc/types/admin/orgs/user_add_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="patch /v2/admin/org/{org-name}/users/{id}/add-role">client.admin.orgs.users.<a href="./src/ngc/resources/admin/orgs/users.py">add_role</a>(id, \*, org_name, \*\*<a href="src/ngc/types/admin/orgs/user_add_role_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="get /v2/admin/org/{org-name}/entitlements">client.admin.orgs.users.<a href="./src/ngc/resources/admin/orgs/users.py">get_entitlements</a>(org_name, \*\*<a href="src/ngc/types/admin/orgs/user_get_entitlements_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /v2/admin/org/{org-name}/users/{id}">client.admin.orgs.users.<a href="./src/ngc/resources/admin/orgs/users.py">remove</a>(id, \*, org_name) -> <a href="./src/ngc/types/admin/orgs/user_remove_response.py">UserRemoveResponse</a></code>

### Teams

#### Users

Methods:

- <code title="post /v2/admin/org/{org-name}/team/{team-name}/users">client.admin.orgs.teams.users.<a href="./src/ngc/resources/admin/orgs/teams/users.py">create</a>(team_name, \*, org_name, \*\*<a href="src/ngc/types/admin/orgs/teams/user_create_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="get /v2/admin/org/{org-name}/teams/{team-name}">client.admin.orgs.teams.users.<a href="./src/ngc/resources/admin/orgs/teams/users.py">retrieve</a>(team_name, \*, org_name) -> BinaryAPIResponse</code>
- <code title="patch /v2/admin/org/{org-name}/teams/{team-name}">client.admin.orgs.teams.users.<a href="./src/ngc/resources/admin/orgs/teams/users.py">update</a>(team_name, \*, org_name, \*\*<a href="src/ngc/types/admin/orgs/teams/user_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v2/admin/org/{org-name}/team/{team-name}/users/{id}">client.admin.orgs.teams.users.<a href="./src/ngc/resources/admin/orgs/teams/users.py">add</a>(id, \*, org_name, team_name, \*\*<a href="src/ngc/types/admin/orgs/teams/user_add_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="patch /v2/admin/org/{org-name}/team/{team-name}/users/{id}/add-role">client.admin.orgs.teams.users.<a href="./src/ngc/resources/admin/orgs/teams/users.py">add_role</a>(id, \*, org_name, team_name, \*\*<a href="src/ngc/types/admin/orgs/teams/user_add_role_params.py">params</a>) -> <a href="./src/ngc/types/shared/user.py">User</a></code>
- <code title="get /v3/orgs/{org-name}/teams/{team-name}/users/{user-email-or-id}">client.admin.orgs.teams.users.<a href="./src/ngc/resources/admin/orgs/teams/users.py">retrieve_user</a>(user_email_or_id, \*, org_name, team_name) -> <a href="./src/ngc/types/shared/user.py">User</a></code>

## Users

Types:

```python
from ngc.types.admin import UserCRMSyncResponse
```

Methods:

- <code title="post /v2/admin/users/{id}/crm-sync">client.admin.users.<a href="./src/ngc/resources/admin/users.py">crm_sync</a>(id) -> <a href="./src/ngc/types/admin/user_crm_sync_response.py">UserCRMSyncResponse</a></code>
- <code title="post /v2/admin/users/{id}/migrate-deprecated-roles">client.admin.users.<a href="./src/ngc/resources/admin/users.py">migrate_deprecated_roles</a>(id) -> <a href="./src/ngc/types/shared/user.py">User</a></code>

# Services

Types:

```python
from ngc.types import ServiceVersionResponse
```

Methods:

- <code title="get /version">client.services.<a href="./src/ngc/resources/services.py">version</a>(\*\*<a href="src/ngc/types/service_version_params.py">params</a>) -> <a href="./src/ngc/types/service_version_response.py">ServiceVersionResponse</a></code>

# Roles

Types:

```python
from ngc.types import UserRoleDefinitions
```

Methods:

- <code title="get /roles">client.roles.<a href="./src/ngc/resources/roles.py">retrieve_all</a>(\*\*<a href="src/ngc/types/role_retrieve_all_params.py">params</a>) -> <a href="./src/ngc/types/user_role_definitions.py">UserRoleDefinitions</a></code>

# PublicKeys

Types:

```python
from ngc.types import PublicKeyRetrieveAllResponse
```

Methods:

- <code title="get /public-keys">client.public_keys.<a href="./src/ngc/resources/public_keys.py">retrieve_all</a>() -> <a href="./src/ngc/types/public_key_retrieve_all_response.py">PublicKeyRetrieveAllResponse</a></code>

# Health

Methods:

- <code title="get /health">client.health.<a href="./src/ngc/resources/health/health.py">retrieve_all</a>() -> <a href="./src/ngc/types/shared/health.py">Health</a></code>

## All

Methods:

- <code title="get /health/all">client.health.all.<a href="./src/ngc/resources/health/all.py">retrieve_all</a>(\*\*<a href="src/ngc/types/health/all_retrieve_all_params.py">params</a>) -> <a href="./src/ngc/types/shared/health.py">Health</a></code>

# SwaggerResources

Methods:

- <code title="post /swagger-resources">client.swagger_resources.<a href="./src/ngc/resources/swagger_resources/swagger_resources.py">create</a>() -> BinaryAPIResponse</code>
- <code title="patch /swagger-resources">client.swagger_resources.<a href="./src/ngc/resources/swagger_resources/swagger_resources.py">update</a>() -> BinaryAPIResponse</code>
- <code title="delete /swagger-resources">client.swagger_resources.<a href="./src/ngc/resources/swagger_resources/swagger_resources.py">delete</a>() -> BinaryAPIResponse</code>
- <code title="get /swagger-resources">client.swagger_resources.<a href="./src/ngc/resources/swagger_resources/swagger_resources.py">retrieve_all</a>() -> BinaryAPIResponse</code>

## Configuration

### Ui

Methods:

- <code title="post /swagger-resources/configuration/ui">client.swagger_resources.configuration.ui.<a href="./src/ngc/resources/swagger_resources/configuration/ui.py">create</a>() -> BinaryAPIResponse</code>
- <code title="get /swagger-resources/configuration/ui">client.swagger_resources.configuration.ui.<a href="./src/ngc/resources/swagger_resources/configuration/ui.py">retrieve</a>() -> BinaryAPIResponse</code>
- <code title="patch /swagger-resources/configuration/ui">client.swagger_resources.configuration.ui.<a href="./src/ngc/resources/swagger_resources/configuration/ui.py">update</a>() -> BinaryAPIResponse</code>
- <code title="delete /swagger-resources/configuration/ui">client.swagger_resources.configuration.ui.<a href="./src/ngc/resources/swagger_resources/configuration/ui.py">delete</a>() -> BinaryAPIResponse</code>

### Security

Methods:

- <code title="post /swagger-resources/configuration/security">client.swagger_resources.configuration.security.<a href="./src/ngc/resources/swagger_resources/configuration/security.py">create</a>() -> BinaryAPIResponse</code>
- <code title="get /swagger-resources/configuration/security">client.swagger_resources.configuration.security.<a href="./src/ngc/resources/swagger_resources/configuration/security.py">retrieve</a>() -> BinaryAPIResponse</code>
- <code title="patch /swagger-resources/configuration/security">client.swagger_resources.configuration.security.<a href="./src/ngc/resources/swagger_resources/configuration/security.py">update</a>() -> BinaryAPIResponse</code>
- <code title="delete /swagger-resources/configuration/security">client.swagger_resources.configuration.security.<a href="./src/ngc/resources/swagger_resources/configuration/security.py">delete</a>() -> BinaryAPIResponse</code>
