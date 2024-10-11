# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPageNumberTeams, AsyncPageNumberTeams
from ....types.orgs import team_list_params
from .starfleet_ids import (
    StarfleetIDsResource,
    AsyncStarfleetIDsResource,
    StarfleetIDsResourceWithRawResponse,
    AsyncStarfleetIDsResourceWithRawResponse,
    StarfleetIDsResourceWithStreamingResponse,
    AsyncStarfleetIDsResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from .nca_invitations import (
    NcaInvitationsResource,
    AsyncNcaInvitationsResource,
    NcaInvitationsResourceWithRawResponse,
    AsyncNcaInvitationsResourceWithRawResponse,
    NcaInvitationsResourceWithStreamingResponse,
    AsyncNcaInvitationsResourceWithStreamingResponse,
)
from ....types.orgs.team_list_response import TeamListResponse

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def starfleet_ids(self) -> StarfleetIDsResource:
        return StarfleetIDsResource(self._client)

    @cached_property
    def nca_invitations(self) -> NcaInvitationsResource:
        return NcaInvitationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return TeamsResourceWithStreamingResponse(self)

    def list(
        self,
        org_name: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageNumberTeams[TeamListResponse]:
        """
        List all Teams

        Args:
          page_number: The page number of result

          page_size: The page size of result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._get_api_list(
            f"/v2/org/{org_name}/teams",
            page=SyncPageNumberTeams[TeamListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    team_list_params.TeamListParams,
                ),
            ),
            model=TeamListResponse,
        )


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def starfleet_ids(self) -> AsyncStarfleetIDsResource:
        return AsyncStarfleetIDsResource(self._client)

    @cached_property
    def nca_invitations(self) -> AsyncNcaInvitationsResource:
        return AsyncNcaInvitationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncTeamsResourceWithStreamingResponse(self)

    def list(
        self,
        org_name: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TeamListResponse, AsyncPageNumberTeams[TeamListResponse]]:
        """
        List all Teams

        Args:
          page_number: The page number of result

          page_size: The page size of result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._get_api_list(
            f"/v2/org/{org_name}/teams",
            page=AsyncPageNumberTeams[TeamListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    team_list_params.TeamListParams,
                ),
            ),
            model=TeamListResponse,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.list = to_raw_response_wrapper(
            teams.list,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._teams.users)

    @cached_property
    def starfleet_ids(self) -> StarfleetIDsResourceWithRawResponse:
        return StarfleetIDsResourceWithRawResponse(self._teams.starfleet_ids)

    @cached_property
    def nca_invitations(self) -> NcaInvitationsResourceWithRawResponse:
        return NcaInvitationsResourceWithRawResponse(self._teams.nca_invitations)


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.list = async_to_raw_response_wrapper(
            teams.list,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._teams.users)

    @cached_property
    def starfleet_ids(self) -> AsyncStarfleetIDsResourceWithRawResponse:
        return AsyncStarfleetIDsResourceWithRawResponse(self._teams.starfleet_ids)

    @cached_property
    def nca_invitations(self) -> AsyncNcaInvitationsResourceWithRawResponse:
        return AsyncNcaInvitationsResourceWithRawResponse(self._teams.nca_invitations)


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.list = to_streamed_response_wrapper(
            teams.list,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._teams.users)

    @cached_property
    def starfleet_ids(self) -> StarfleetIDsResourceWithStreamingResponse:
        return StarfleetIDsResourceWithStreamingResponse(self._teams.starfleet_ids)

    @cached_property
    def nca_invitations(self) -> NcaInvitationsResourceWithStreamingResponse:
        return NcaInvitationsResourceWithStreamingResponse(self._teams.nca_invitations)


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.list = async_to_streamed_response_wrapper(
            teams.list,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._teams.users)

    @cached_property
    def starfleet_ids(self) -> AsyncStarfleetIDsResourceWithStreamingResponse:
        return AsyncStarfleetIDsResourceWithStreamingResponse(self._teams.starfleet_ids)

    @cached_property
    def nca_invitations(self) -> AsyncNcaInvitationsResourceWithStreamingResponse:
        return AsyncNcaInvitationsResourceWithStreamingResponse(self._teams.nca_invitations)
