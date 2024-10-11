# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserRoleDefinitions", "RequestStatus", "Role", "RoleAllowedAction", "RoleProduct"]


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


class RoleAllowedAction(BaseModel):
    access_levels: Optional[List[str]] = FieldInfo(alias="accessLevels", default=None)
    """List of access levels that this role allows"""

    service: Optional[str] = None
    """Service that this role allows"""


class RoleProduct(BaseModel):
    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """
    Display Name of the product from the product catalog to which this role is
    associated with
    """

    name: Optional[str] = None
    """
    Name of the product from the product catalog to which this role is associated
    with
    """


class Role(BaseModel):
    allowed_actions: Optional[List[RoleAllowedAction]] = FieldInfo(alias="allowedActions", default=None)
    """List of actions that this role allows"""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display Name of the role"""

    name: Optional[str] = None
    """Name of the role"""

    product: Optional[RoleProduct] = None
    """Product information of the role"""

    short_display_name: Optional[str] = FieldInfo(alias="shortDisplayName", default=None)
    """Short Display Name of the role"""


class UserRoleDefinitions(BaseModel):
    request_status: Optional[RequestStatus] = FieldInfo(alias="requestStatus", default=None)

    roles: Optional[List[Role]] = None
    """List of roles"""
