# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import service_version_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.service_version_response import ServiceVersionResponse

__all__ = ["ServicesResource", "AsyncServicesResource"]


class ServicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return ServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return ServicesResourceWithStreamingResponse(self)

    def version(
        self,
        *,
        package: str | NotGiven = NOT_GIVEN,
        repo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceVersionResponse:
        """
        Used to get the latest version number of a given package.

        Args:
          package: name of package

          repo: repository of package

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "package": package,
                        "repo": repo,
                    },
                    service_version_params.ServiceVersionParams,
                ),
            ),
            cast_to=ServiceVersionResponse,
        )


class AsyncServicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncServicesResourceWithStreamingResponse(self)

    async def version(
        self,
        *,
        package: str | NotGiven = NOT_GIVEN,
        repo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceVersionResponse:
        """
        Used to get the latest version number of a given package.

        Args:
          package: name of package

          repo: repository of package

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "package": package,
                        "repo": repo,
                    },
                    service_version_params.ServiceVersionParams,
                ),
            ),
            cast_to=ServiceVersionResponse,
        )


class ServicesResourceWithRawResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.version = to_raw_response_wrapper(
            services.version,
        )


class AsyncServicesResourceWithRawResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.version = async_to_raw_response_wrapper(
            services.version,
        )


class ServicesResourceWithStreamingResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.version = to_streamed_response_wrapper(
            services.version,
        )


class AsyncServicesResourceWithStreamingResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.version = async_to_streamed_response_wrapper(
            services.version,
        )
