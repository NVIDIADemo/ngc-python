# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v2 import (
    V2Resource,
    AsyncV2Resource,
    V2ResourceWithRawResponse,
    AsyncV2ResourceWithRawResponse,
    V2ResourceWithStreamingResponse,
    AsyncV2ResourceWithStreamingResponse,
)
from .v2.v2 import V2Resource, AsyncV2Resource
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def v2(self) -> V2Resource:
        return V2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def v2(self) -> AsyncV2Resource:
        return AsyncV2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

    @cached_property
    def v2(self) -> V2ResourceWithRawResponse:
        return V2ResourceWithRawResponse(self._users.v2)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

    @cached_property
    def v2(self) -> AsyncV2ResourceWithRawResponse:
        return AsyncV2ResourceWithRawResponse(self._users.v2)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

    @cached_property
    def v2(self) -> V2ResourceWithStreamingResponse:
        return V2ResourceWithStreamingResponse(self._users.v2)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

    @cached_property
    def v2(self) -> AsyncV2ResourceWithStreamingResponse:
        return AsyncV2ResourceWithStreamingResponse(self._users.v2)
