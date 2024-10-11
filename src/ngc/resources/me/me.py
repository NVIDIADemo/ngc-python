# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .api_key import (
    APIKeyResource,
    AsyncAPIKeyResource,
    APIKeyResourceWithRawResponse,
    AsyncAPIKeyResourceWithRawResponse,
    APIKeyResourceWithStreamingResponse,
    AsyncAPIKeyResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def api_key(self) -> APIKeyResource:
        return APIKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def api_key(self) -> AsyncAPIKeyResource:
        return AsyncAPIKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

    @cached_property
    def api_key(self) -> APIKeyResourceWithRawResponse:
        return APIKeyResourceWithRawResponse(self._me.api_key)


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

    @cached_property
    def api_key(self) -> AsyncAPIKeyResourceWithRawResponse:
        return AsyncAPIKeyResourceWithRawResponse(self._me.api_key)


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

    @cached_property
    def api_key(self) -> APIKeyResourceWithStreamingResponse:
        return APIKeyResourceWithStreamingResponse(self._me.api_key)


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

    @cached_property
    def api_key(self) -> AsyncAPIKeyResourceWithStreamingResponse:
        return AsyncAPIKeyResourceWithStreamingResponse(self._me.api_key)
