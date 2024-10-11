# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserInvitationList", "Invitation", "PaginationInfo", "RequestStatus"]


class Invitation(BaseModel):
    id: Optional[str] = None
    """Unique invitation ID"""

    created_date: Optional[str] = FieldInfo(alias="createdDate", default=None)
    """Date on which the invitation was created. (ISO-8601 format)"""

    email: Optional[str] = None
    """Email address of the user."""

    is_processed: Optional[bool] = FieldInfo(alias="isProcessed", default=None)
    """Flag indicating if the invitation has already been accepted by the user."""

    name: Optional[str] = None
    """user name"""

    org: Optional[str] = None
    """Org to which a user was invited."""

    roles: Optional[List[str]] = None
    """List of roles that the user have."""

    team: Optional[str] = None
    """Team to which a user was invited."""

    type: Optional[Literal["ORGANIZATION", "TEAM"]] = None
    """Type of invitation.

    The invitation is either to an organization or to a team within organization.
    """


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


class UserInvitationList(BaseModel):
    invitations: Optional[List[Invitation]] = None
    """List of invitations."""

    pagination_info: Optional[PaginationInfo] = FieldInfo(alias="paginationInfo", default=None)
    """object that describes the pagination information"""

    request_status: Optional[RequestStatus] = FieldInfo(alias="requestStatus", default=None)
