# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import v2_admin_org_team_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["V2AdminOrgTeamsResource", "AsyncV2AdminOrgTeamsResource"]


class V2AdminOrgTeamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2AdminOrgTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return V2AdminOrgTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2AdminOrgTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return V2AdminOrgTeamsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        team_name: str,
        *,
        org_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Get one team

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v2/admin/org/{org_name}/teams/{team_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        team_name: str,
        *,
        org_name: str,
        description: str | NotGiven = NOT_GIVEN,
        infinity_manager_settings: v2_admin_org_team_update_params.InfinityManagerSettings | NotGiven = NOT_GIVEN,
        repo_scan_settings: v2_admin_org_team_update_params.RepoScanSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Edit a Team

        Args:
          description: description of the team

          infinity_manager_settings: Infinity manager setting definition

          repo_scan_settings: Repo scan setting definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not team_name:
            raise ValueError(f"Expected a non-empty value for `team_name` but received {team_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/v2/admin/org/{org_name}/teams/{team_name}",
            body=maybe_transform(
                {
                    "description": description,
                    "infinity_manager_settings": infinity_manager_settings,
                    "repo_scan_settings": repo_scan_settings,
                },
                v2_admin_org_team_update_params.V2AdminOrgTeamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncV2AdminOrgTeamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2AdminOrgTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2AdminOrgTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2AdminOrgTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncV2AdminOrgTeamsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        team_name: str,
        *,
        org_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Get one team

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v2/admin/org/{org_name}/teams/{team_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        team_name: str,
        *,
        org_name: str,
        description: str | NotGiven = NOT_GIVEN,
        infinity_manager_settings: v2_admin_org_team_update_params.InfinityManagerSettings | NotGiven = NOT_GIVEN,
        repo_scan_settings: v2_admin_org_team_update_params.RepoScanSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Edit a Team

        Args:
          description: description of the team

          infinity_manager_settings: Infinity manager setting definition

          repo_scan_settings: Repo scan setting definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not team_name:
            raise ValueError(f"Expected a non-empty value for `team_name` but received {team_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/v2/admin/org/{org_name}/teams/{team_name}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "infinity_manager_settings": infinity_manager_settings,
                    "repo_scan_settings": repo_scan_settings,
                },
                v2_admin_org_team_update_params.V2AdminOrgTeamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class V2AdminOrgTeamsResourceWithRawResponse:
    def __init__(self, v2_admin_org_teams: V2AdminOrgTeamsResource) -> None:
        self._v2_admin_org_teams = v2_admin_org_teams

        self.retrieve = to_custom_raw_response_wrapper(
            v2_admin_org_teams.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            v2_admin_org_teams.update,
            BinaryAPIResponse,
        )


class AsyncV2AdminOrgTeamsResourceWithRawResponse:
    def __init__(self, v2_admin_org_teams: AsyncV2AdminOrgTeamsResource) -> None:
        self._v2_admin_org_teams = v2_admin_org_teams

        self.retrieve = async_to_custom_raw_response_wrapper(
            v2_admin_org_teams.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            v2_admin_org_teams.update,
            AsyncBinaryAPIResponse,
        )


class V2AdminOrgTeamsResourceWithStreamingResponse:
    def __init__(self, v2_admin_org_teams: V2AdminOrgTeamsResource) -> None:
        self._v2_admin_org_teams = v2_admin_org_teams

        self.retrieve = to_custom_streamed_response_wrapper(
            v2_admin_org_teams.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            v2_admin_org_teams.update,
            StreamedBinaryAPIResponse,
        )


class AsyncV2AdminOrgTeamsResourceWithStreamingResponse:
    def __init__(self, v2_admin_org_teams: AsyncV2AdminOrgTeamsResource) -> None:
        self._v2_admin_org_teams = v2_admin_org_teams

        self.retrieve = async_to_custom_streamed_response_wrapper(
            v2_admin_org_teams.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            v2_admin_org_teams.update,
            AsyncStreamedBinaryAPIResponse,
        )
