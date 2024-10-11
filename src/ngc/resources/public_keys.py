# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.public_key_retrieve_all_response import PublicKeyRetrieveAllResponse

__all__ = ["PublicKeysResource", "AsyncPublicKeysResource"]


class PublicKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return PublicKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return PublicKeysResourceWithStreamingResponse(self)

    def retrieve_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicKeyRetrieveAllResponse:
        """Used to check the health status of the web service only"""
        return self._get(
            "/public-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicKeyRetrieveAllResponse,
        )


class AsyncPublicKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncPublicKeysResourceWithStreamingResponse(self)

    async def retrieve_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicKeyRetrieveAllResponse:
        """Used to check the health status of the web service only"""
        return await self._get(
            "/public-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicKeyRetrieveAllResponse,
        )


class PublicKeysResourceWithRawResponse:
    def __init__(self, public_keys: PublicKeysResource) -> None:
        self._public_keys = public_keys

        self.retrieve_all = to_raw_response_wrapper(
            public_keys.retrieve_all,
        )


class AsyncPublicKeysResourceWithRawResponse:
    def __init__(self, public_keys: AsyncPublicKeysResource) -> None:
        self._public_keys = public_keys

        self.retrieve_all = async_to_raw_response_wrapper(
            public_keys.retrieve_all,
        )


class PublicKeysResourceWithStreamingResponse:
    def __init__(self, public_keys: PublicKeysResource) -> None:
        self._public_keys = public_keys

        self.retrieve_all = to_streamed_response_wrapper(
            public_keys.retrieve_all,
        )


class AsyncPublicKeysResourceWithStreamingResponse:
    def __init__(self, public_keys: AsyncPublicKeysResource) -> None:
        self._public_keys = public_keys

        self.retrieve_all = async_to_streamed_response_wrapper(
            public_keys.retrieve_all,
        )
