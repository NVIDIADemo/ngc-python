# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["UserUpdateParams", "InfinityManagerSettings", "RepoScanSettings"]


class UserUpdateParams(TypedDict, total=False):
    org_name: Required[Annotated[str, PropertyInfo(alias="org-name")]]

    description: str
    """description of the team"""

    infinity_manager_settings: Annotated[InfinityManagerSettings, PropertyInfo(alias="infinityManagerSettings")]
    """Infinity manager setting definition"""

    repo_scan_settings: Annotated[RepoScanSettings, PropertyInfo(alias="repoScanSettings")]
    """Repo scan setting definition"""


class InfinityManagerSettings(TypedDict, total=False):
    infinity_manager_enabled: Annotated[bool, PropertyInfo(alias="infinityManagerEnabled")]
    """Enable the infinity manager or not. Used both in org and team level object"""

    infinity_manager_enable_team_override: Annotated[bool, PropertyInfo(alias="infinityManagerEnableTeamOverride")]
    """Allow override settings at team level. Only used in org level object"""


class RepoScanSettings(TypedDict, total=False):
    repo_scan_allow_override: Annotated[bool, PropertyInfo(alias="repoScanAllowOverride")]
    """Allow org admin to override the org level repo scan settings"""

    repo_scan_by_default: Annotated[bool, PropertyInfo(alias="repoScanByDefault")]
    """Allow repository scanning by default"""

    repo_scan_enabled: Annotated[bool, PropertyInfo(alias="repoScanEnabled")]
    """Enable the repository scan or not. Only used in org level object"""

    repo_scan_enable_notifications: Annotated[bool, PropertyInfo(alias="repoScanEnableNotifications")]
    """Sends notification to end user after scanning is done"""

    repo_scan_enable_team_override: Annotated[bool, PropertyInfo(alias="repoScanEnableTeamOverride")]
    """Allow override settings at team level. Only used in org level object"""

    repo_scan_show_results: Annotated[bool, PropertyInfo(alias="repoScanShowResults")]
    """Allow showing scan results to CLI or UI"""
