# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncPageNumberOrganizations",
    "AsyncPageNumberOrganizations",
    "SyncPageNumberUsers",
    "AsyncPageNumberUsers",
    "SyncPageNumberTeams",
    "AsyncPageNumberTeams",
    "SyncPageNumberInvitations",
    "AsyncPageNumberInvitations",
]

_T = TypeVar("_T")


class SyncPageNumberOrganizations(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    organizations: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        organizations = self.organizations
        if not organizations:
            return []
        return organizations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page-number")) or 1

        return PageInfo(params={"page-number": last_page + 1})


class AsyncPageNumberOrganizations(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    organizations: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        organizations = self.organizations
        if not organizations:
            return []
        return organizations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page-number")) or 1

        return PageInfo(params={"page-number": last_page + 1})


class SyncPageNumberUsers(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    users: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        users = self.users
        if not users:
            return []
        return users

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page-number")) or 1

        return PageInfo(params={"page-number": last_page + 1})


class AsyncPageNumberUsers(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    users: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        users = self.users
        if not users:
            return []
        return users

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page-number")) or 1

        return PageInfo(params={"page-number": last_page + 1})


class SyncPageNumberTeams(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    teams: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        teams = self.teams
        if not teams:
            return []
        return teams

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page-number")) or 1

        return PageInfo(params={"page-number": last_page + 1})


class AsyncPageNumberTeams(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    teams: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        teams = self.teams
        if not teams:
            return []
        return teams

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page-number")) or 1

        return PageInfo(params={"page-number": last_page + 1})


class SyncPageNumberInvitations(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    invitations: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        invitations = self.invitations
        if not invitations:
            return []
        return invitations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page-number")) or 1

        return PageInfo(params={"page-number": last_page + 1})


class AsyncPageNumberInvitations(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    invitations: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        invitations = self.invitations
        if not invitations:
            return []
        return invitations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page-number")) or 1

        return PageInfo(params={"page-number": last_page + 1})
