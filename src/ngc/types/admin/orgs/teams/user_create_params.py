# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["UserCreateParams", "UserMetadata"]


class UserCreateParams(TypedDict, total=False):
    org_name: Required[Annotated[str, PropertyInfo(alias="org-name")]]

    email: Required[str]
    """Email address of the user. This should be unique."""

    idp_id: Annotated[str, PropertyInfo(alias="idp-id")]
    """
    If the IDP ID is provided then it is used instead of the one configured for the
    organization
    """

    send_email: Annotated[bool, PropertyInfo(alias="send-email")]
    """Boolean to send email notification, default is true"""

    email_opt_in: Annotated[bool, PropertyInfo(alias="emailOptIn")]
    """indicates if user has opt in to nvidia emails"""

    eula_accepted: Annotated[bool, PropertyInfo(alias="eulaAccepted")]
    """indicates if user has accepted EULA"""

    name: str
    """user name"""

    role_type: Annotated[str, PropertyInfo(alias="roleType")]
    """DEPRECATED - use roleTypes which allows multiple roles"""

    role_types: Annotated[List[str], PropertyInfo(alias="roleTypes")]
    """feature roles to give to the user"""

    salesforce_contact_job_role: Annotated[str, PropertyInfo(alias="salesforceContactJobRole")]
    """user job role"""

    user_metadata: Annotated[UserMetadata, PropertyInfo(alias="userMetadata")]
    """Metadata information about the user."""


class UserMetadata(TypedDict, total=False):
    company: str
    """Name of the company"""

    company_url: Annotated[str, PropertyInfo(alias="companyUrl")]
    """Company URL"""

    country: str
    """Country of the user"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """User's first name"""

    industry: str
    """Industry segment"""

    interest: List[str]
    """List of development areas that user has interest"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """User's last name"""

    role: str
    """Role of the user in the company"""
