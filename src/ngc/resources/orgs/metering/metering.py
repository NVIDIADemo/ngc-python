# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .gpupeak import (
    GpupeakResource,
    AsyncGpupeakResource,
    GpupeakResourceWithRawResponse,
    AsyncGpupeakResourceWithRawResponse,
    GpupeakResourceWithStreamingResponse,
    AsyncGpupeakResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.orgs import metering_retrieve_all_params
from ...._base_client import make_request_options
from ....types.shared.metering_result_list import MeteringResultList

__all__ = ["MeteringResource", "AsyncMeteringResource"]


class MeteringResource(SyncAPIResource):
    @cached_property
    def gpupeak(self) -> GpupeakResource:
        return GpupeakResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeteringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return MeteringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeteringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return MeteringResourceWithStreamingResponse(self)

    def retrieve_all(
        self,
        org_name: str,
        *,
        q: metering_retrieve_all_params.Q,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResultList:
        """
        Returns Private Registry / EGX resources usage metering as measurement series.
        Requires admin privileges for organization.

        Args:
          q: request params for getting metering usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._get(
            f"/v2/org/{org_name}/metering",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"q": q}, metering_retrieve_all_params.MeteringRetrieveAllParams),
            ),
            cast_to=MeteringResultList,
        )


class AsyncMeteringResource(AsyncAPIResource):
    @cached_property
    def gpupeak(self) -> AsyncGpupeakResource:
        return AsyncGpupeakResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeteringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeteringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeteringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncMeteringResourceWithStreamingResponse(self)

    async def retrieve_all(
        self,
        org_name: str,
        *,
        q: metering_retrieve_all_params.Q,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResultList:
        """
        Returns Private Registry / EGX resources usage metering as measurement series.
        Requires admin privileges for organization.

        Args:
          q: request params for getting metering usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return await self._get(
            f"/v2/org/{org_name}/metering",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"q": q}, metering_retrieve_all_params.MeteringRetrieveAllParams),
            ),
            cast_to=MeteringResultList,
        )


class MeteringResourceWithRawResponse:
    def __init__(self, metering: MeteringResource) -> None:
        self._metering = metering

        self.retrieve_all = to_raw_response_wrapper(
            metering.retrieve_all,
        )

    @cached_property
    def gpupeak(self) -> GpupeakResourceWithRawResponse:
        return GpupeakResourceWithRawResponse(self._metering.gpupeak)


class AsyncMeteringResourceWithRawResponse:
    def __init__(self, metering: AsyncMeteringResource) -> None:
        self._metering = metering

        self.retrieve_all = async_to_raw_response_wrapper(
            metering.retrieve_all,
        )

    @cached_property
    def gpupeak(self) -> AsyncGpupeakResourceWithRawResponse:
        return AsyncGpupeakResourceWithRawResponse(self._metering.gpupeak)


class MeteringResourceWithStreamingResponse:
    def __init__(self, metering: MeteringResource) -> None:
        self._metering = metering

        self.retrieve_all = to_streamed_response_wrapper(
            metering.retrieve_all,
        )

    @cached_property
    def gpupeak(self) -> GpupeakResourceWithStreamingResponse:
        return GpupeakResourceWithStreamingResponse(self._metering.gpupeak)


class AsyncMeteringResourceWithStreamingResponse:
    def __init__(self, metering: AsyncMeteringResource) -> None:
        self._metering = metering

        self.retrieve_all = async_to_streamed_response_wrapper(
            metering.retrieve_all,
        )

    @cached_property
    def gpupeak(self) -> AsyncGpupeakResourceWithStreamingResponse:
        return AsyncGpupeakResourceWithStreamingResponse(self._metering.gpupeak)
