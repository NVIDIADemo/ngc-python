# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.shared.user import User

__all__ = ["StarfleetIDsResource", "AsyncStarfleetIDsResource"]


class StarfleetIDsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StarfleetIDsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return StarfleetIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StarfleetIDsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return StarfleetIDsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        starfleet_id: str,
        *,
        org_name: str,
        team_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Get User details in team by starfleet Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not team_name:
            raise ValueError(f"Expected a non-empty value for `team_name` but received {team_name!r}")
        if not starfleet_id:
            raise ValueError(f"Expected a non-empty value for `starfleet_id` but received {starfleet_id!r}")
        return self._get(
            f"/v2/org/{org_name}/team/{team_name}/starfleetIds/{starfleet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AsyncStarfleetIDsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStarfleetIDsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStarfleetIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStarfleetIDsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncStarfleetIDsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        starfleet_id: str,
        *,
        org_name: str,
        team_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Get User details in team by starfleet Id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not team_name:
            raise ValueError(f"Expected a non-empty value for `team_name` but received {team_name!r}")
        if not starfleet_id:
            raise ValueError(f"Expected a non-empty value for `starfleet_id` but received {starfleet_id!r}")
        return await self._get(
            f"/v2/org/{org_name}/team/{team_name}/starfleetIds/{starfleet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class StarfleetIDsResourceWithRawResponse:
    def __init__(self, starfleet_ids: StarfleetIDsResource) -> None:
        self._starfleet_ids = starfleet_ids

        self.retrieve = to_raw_response_wrapper(
            starfleet_ids.retrieve,
        )


class AsyncStarfleetIDsResourceWithRawResponse:
    def __init__(self, starfleet_ids: AsyncStarfleetIDsResource) -> None:
        self._starfleet_ids = starfleet_ids

        self.retrieve = async_to_raw_response_wrapper(
            starfleet_ids.retrieve,
        )


class StarfleetIDsResourceWithStreamingResponse:
    def __init__(self, starfleet_ids: StarfleetIDsResource) -> None:
        self._starfleet_ids = starfleet_ids

        self.retrieve = to_streamed_response_wrapper(
            starfleet_ids.retrieve,
        )


class AsyncStarfleetIDsResourceWithStreamingResponse:
    def __init__(self, starfleet_ids: AsyncStarfleetIDsResource) -> None:
        self._starfleet_ids = starfleet_ids

        self.retrieve = async_to_streamed_response_wrapper(
            starfleet_ids.retrieve,
        )
