# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .me import (
    MeResource,
    AsyncMeResource,
    MeResourceWithRawResponse,
    AsyncMeResourceWithRawResponse,
    MeResourceWithStreamingResponse,
    AsyncMeResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["UsersManagementResource", "AsyncUsersManagementResource"]


class UsersManagementResource(SyncAPIResource):
    @cached_property
    def me(self) -> MeResource:
        return MeResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return UsersManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return UsersManagementResourceWithStreamingResponse(self)


class AsyncUsersManagementResource(AsyncAPIResource):
    @cached_property
    def me(self) -> AsyncMeResource:
        return AsyncMeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncUsersManagementResourceWithStreamingResponse(self)


class UsersManagementResourceWithRawResponse:
    def __init__(self, users_management: UsersManagementResource) -> None:
        self._users_management = users_management

    @cached_property
    def me(self) -> MeResourceWithRawResponse:
        return MeResourceWithRawResponse(self._users_management.me)


class AsyncUsersManagementResourceWithRawResponse:
    def __init__(self, users_management: AsyncUsersManagementResource) -> None:
        self._users_management = users_management

    @cached_property
    def me(self) -> AsyncMeResourceWithRawResponse:
        return AsyncMeResourceWithRawResponse(self._users_management.me)


class UsersManagementResourceWithStreamingResponse:
    def __init__(self, users_management: UsersManagementResource) -> None:
        self._users_management = users_management

    @cached_property
    def me(self) -> MeResourceWithStreamingResponse:
        return MeResourceWithStreamingResponse(self._users_management.me)


class AsyncUsersManagementResourceWithStreamingResponse:
    def __init__(self, users_management: AsyncUsersManagementResource) -> None:
        self._users_management = users_management

    @cached_property
    def me(self) -> AsyncMeResourceWithStreamingResponse:
        return AsyncMeResourceWithStreamingResponse(self._users_management.me)
