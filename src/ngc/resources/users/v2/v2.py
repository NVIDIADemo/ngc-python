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
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def api_key(self) -> APIKeyResource:
        return APIKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def api_key(self) -> AsyncAPIKeyResource:
        return AsyncAPIKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def api_key(self) -> APIKeyResourceWithRawResponse:
        return APIKeyResourceWithRawResponse(self._v2.api_key)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def api_key(self) -> AsyncAPIKeyResourceWithRawResponse:
        return AsyncAPIKeyResourceWithRawResponse(self._v2.api_key)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def api_key(self) -> APIKeyResourceWithStreamingResponse:
        return APIKeyResourceWithStreamingResponse(self._v2.api_key)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def api_key(self) -> AsyncAPIKeyResourceWithStreamingResponse:
        return AsyncAPIKeyResourceWithStreamingResponse(self._v2.api_key)
