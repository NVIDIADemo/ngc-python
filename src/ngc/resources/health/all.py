# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.health import all_retrieve_all_params
from ...types.shared.health import Health

__all__ = ["AllResource", "AsyncAllResource"]


class AllResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AllResourceWithStreamingResponse(self)

    def retrieve_all(
        self,
        *,
        secret: str | NotGiven = NOT_GIVEN,
        show_details: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Health:
        """
        Used to get health status of all services

        Args:
          secret: secret value that validates the call in order to show details

          show_details: boolean value to indicating to show details or not

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/health/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "secret": secret,
                        "show_details": show_details,
                    },
                    all_retrieve_all_params.AllRetrieveAllParams,
                ),
            ),
            cast_to=Health,
        )


class AsyncAllResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncAllResourceWithStreamingResponse(self)

    async def retrieve_all(
        self,
        *,
        secret: str | NotGiven = NOT_GIVEN,
        show_details: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Health:
        """
        Used to get health status of all services

        Args:
          secret: secret value that validates the call in order to show details

          show_details: boolean value to indicating to show details or not

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/health/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "secret": secret,
                        "show_details": show_details,
                    },
                    all_retrieve_all_params.AllRetrieveAllParams,
                ),
            ),
            cast_to=Health,
        )


class AllResourceWithRawResponse:
    def __init__(self, all: AllResource) -> None:
        self._all = all

        self.retrieve_all = to_raw_response_wrapper(
            all.retrieve_all,
        )


class AsyncAllResourceWithRawResponse:
    def __init__(self, all: AsyncAllResource) -> None:
        self._all = all

        self.retrieve_all = async_to_raw_response_wrapper(
            all.retrieve_all,
        )


class AllResourceWithStreamingResponse:
    def __init__(self, all: AllResource) -> None:
        self._all = all

        self.retrieve_all = to_streamed_response_wrapper(
            all.retrieve_all,
        )


class AsyncAllResourceWithStreamingResponse:
    def __init__(self, all: AsyncAllResource) -> None:
        self._all = all

        self.retrieve_all = async_to_streamed_response_wrapper(
            all.retrieve_all,
        )
