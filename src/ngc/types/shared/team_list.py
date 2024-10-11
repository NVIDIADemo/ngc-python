# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TeamList", "PaginationInfo", "RequestStatus", "Team", "TeamInfinityManagerSettings", "TeamRepoScanSettings"]


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


class TeamInfinityManagerSettings(BaseModel):
    infinity_manager_enabled: Optional[bool] = FieldInfo(alias="infinityManagerEnabled", default=None)
    """Enable the infinity manager or not. Used both in org and team level object"""

    infinity_manager_enable_team_override: Optional[bool] = FieldInfo(
        alias="infinityManagerEnableTeamOverride", default=None
    )
    """Allow override settings at team level. Only used in org level object"""


class TeamRepoScanSettings(BaseModel):
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


class Team(BaseModel):
    id: Optional[int] = None
    """unique Id of this team."""

    description: Optional[str] = None
    """description of the team"""

    infinity_manager_settings: Optional[TeamInfinityManagerSettings] = FieldInfo(
        alias="infinityManagerSettings", default=None
    )
    """Infinity manager setting definition"""

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)
    """indicates if the team is deleted or not"""

    name: Optional[str] = None
    """team name"""

    repo_scan_settings: Optional[TeamRepoScanSettings] = FieldInfo(alias="repoScanSettings", default=None)
    """Repo scan setting definition"""


class TeamList(BaseModel):
    pagination_info: Optional[PaginationInfo] = FieldInfo(alias="paginationInfo", default=None)
    """object that describes the pagination information"""

    request_status: Optional[RequestStatus] = FieldInfo(alias="requestStatus", default=None)

    teams: Optional[List[Team]] = None
