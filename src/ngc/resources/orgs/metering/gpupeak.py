# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...._base_client import make_request_options
from ....types.orgs.metering import gpupeak_retrieve_all_params
from ....types.shared.metering_result_list import MeteringResultList

__all__ = ["GpupeakResource", "AsyncGpupeakResource"]


class GpupeakResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GpupeakResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return GpupeakResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GpupeakResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return GpupeakResourceWithStreamingResponse(self)

    def retrieve_all(
        self,
        org_name: str,
        *,
        the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss: gpupeak_retrieve_all_params.TheToDateInISO8601FormatIncludingTimeZoneInformationYyyyMmDdTHhMmSS
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResultList:
        """Returns GPU Peak Usage as measurement series.

        Requires admin privileges for
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._get(
            f"/v2/org/{org_name}/meterings/gpupeak",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss": the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss
                    },
                    gpupeak_retrieve_all_params.GpupeakRetrieveAllParams,
                ),
            ),
            cast_to=MeteringResultList,
        )


class AsyncGpupeakResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGpupeakResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGpupeakResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGpupeakResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncGpupeakResourceWithStreamingResponse(self)

    async def retrieve_all(
        self,
        org_name: str,
        *,
        the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss: gpupeak_retrieve_all_params.TheToDateInISO8601FormatIncludingTimeZoneInformationYyyyMmDdTHhMmSS
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResultList:
        """Returns GPU Peak Usage as measurement series.

        Requires admin privileges for
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return await self._get(
            f"/v2/org/{org_name}/meterings/gpupeak",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss": the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss
                    },
                    gpupeak_retrieve_all_params.GpupeakRetrieveAllParams,
                ),
            ),
            cast_to=MeteringResultList,
        )


class GpupeakResourceWithRawResponse:
    def __init__(self, gpupeak: GpupeakResource) -> None:
        self._gpupeak = gpupeak

        self.retrieve_all = to_raw_response_wrapper(
            gpupeak.retrieve_all,
        )


class AsyncGpupeakResourceWithRawResponse:
    def __init__(self, gpupeak: AsyncGpupeakResource) -> None:
        self._gpupeak = gpupeak

        self.retrieve_all = async_to_raw_response_wrapper(
            gpupeak.retrieve_all,
        )


class GpupeakResourceWithStreamingResponse:
    def __init__(self, gpupeak: GpupeakResource) -> None:
        self._gpupeak = gpupeak

        self.retrieve_all = to_streamed_response_wrapper(
            gpupeak.retrieve_all,
        )


class AsyncGpupeakResourceWithStreamingResponse:
    def __init__(self, gpupeak: AsyncGpupeakResource) -> None:
        self._gpupeak = gpupeak

        self.retrieve_all = async_to_streamed_response_wrapper(
            gpupeak.retrieve_all,
        )
