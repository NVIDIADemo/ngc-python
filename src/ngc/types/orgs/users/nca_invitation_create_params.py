# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["NcaInvitationCreateParams"]


class NcaInvitationCreateParams(TypedDict, total=False):
    email: str
    """Is the user email"""

    invitation_expiration_in: Annotated[int, PropertyInfo(alias="invitationExpirationIn")]
    """Is the numbers of days the invitation will expire"""

    invite_as: Annotated[Literal["ADMIN", "MEMBER"], PropertyInfo(alias="inviteAs")]
    """Nca allow users to be invited as Admin and as Member"""

    message: str
    """Is a message to the new user"""
