# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MeUpdateParams", "UserMetadata"]


class MeUpdateParams(TypedDict, total=False):
    has_email_opt_in: Annotated[bool, PropertyInfo(alias="hasEmailOptIn")]
    """indicates if user has opt in to nvidia emails"""

    has_signed_ai_foundry_partnerships_eula: Annotated[bool, PropertyInfo(alias="hasSignedAiFoundryPartnershipsEULA")]
    """
    indicates if user has accepted AI Foundry Partnerships End User License
    Agreement.
    """

    has_signed_base_command_eula: Annotated[bool, PropertyInfo(alias="hasSignedBaseCommandEULA")]
    """indicates if user has accepted Base Command EULA"""

    has_signed_base_command_manager_eula: Annotated[bool, PropertyInfo(alias="hasSignedBaseCommandManagerEULA")]
    """indicates if user has accepted Base Command Manager End User License Agreement."""

    has_signed_bio_ne_mo_eula: Annotated[bool, PropertyInfo(alias="hasSignedBioNeMoEULA")]
    """indicates if user has accepted BioNeMo End User License Agreement."""

    has_signed_container_publishing_eula: Annotated[bool, PropertyInfo(alias="hasSignedContainerPublishingEULA")]
    """indicates if user has accepted container publishing eula"""

    has_signed_cu_opt_eula: Annotated[bool, PropertyInfo(alias="hasSignedCuOptEULA")]
    """indicates if user has accepted CuOpt End User License Agreement."""

    has_signed_earth2_eula: Annotated[bool, PropertyInfo(alias="hasSignedEarth2EULA")]
    """indicates if user has accepted Earth-2 End User License Agreement."""

    has_signed_egx_eula: Annotated[bool, PropertyInfo(alias="hasSignedEgxEULA")]
    """indicates if user has accepted EGX EULA"""

    has_signed_eula: Annotated[bool, PropertyInfo(alias="hasSignedEULA")]
    """indicates if user has accepted NGC EULA"""

    has_signed_fleet_command_eula: Annotated[bool, PropertyInfo(alias="hasSignedFleetCommandEULA")]
    """indicates if user has accepted Fleet Command End User License Agreement."""

    has_signed_llm_eula: Annotated[bool, PropertyInfo(alias="hasSignedLlmEULA")]
    """indicates if user has accepted LLM End User License Agreement."""

    has_signed_nvaieeula: Annotated[bool, PropertyInfo(alias="hasSignedNVAIEEULA")]
    """indicates if user has accepted Fleet Command End User License Agreement."""

    has_signed_nvidia_eula: Annotated[bool, PropertyInfo(alias="hasSignedNvidiaEULA")]
    """indicates if user has accepted NVIDIA EULA"""

    has_signed_nvqceula: Annotated[bool, PropertyInfo(alias="hasSignedNVQCEULA")]
    """indicates if user has accepted Nvidia Quantum Cloud End User License Agreement."""

    has_signed_omniverse_eula: Annotated[bool, PropertyInfo(alias="hasSignedOmniverseEULA")]
    """indicates if user has accepted Omniverse End User License Agreement."""

    has_signed_privacy_policy: Annotated[bool, PropertyInfo(alias="hasSignedPrivacyPolicy")]
    """indicates if the user has signed the Privacy Policy"""

    has_signed_third_party_registry_share_eula: Annotated[
        bool, PropertyInfo(alias="hasSignedThirdPartyRegistryShareEULA")
    ]
    """
    indicates if user has consented to share their registration info with other
    parties
    """

    name: str
    """user name"""

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
