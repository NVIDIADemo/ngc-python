# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .teams import (
    TeamsResource,
    AsyncTeamsResource,
    TeamsResourceWithRawResponse,
    AsyncTeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
    AsyncTeamsResourceWithStreamingResponse,
)
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from .teams.teams import TeamsResource, AsyncTeamsResource
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.super_admin_user.org_org_owner_backfill_response import OrgOrgOwnerBackfillResponse

__all__ = ["OrgsResource", "AsyncOrgsResource"]


class OrgsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def teams(self) -> TeamsResource:
        return TeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return OrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return OrgsResourceWithStreamingResponse(self)

    def org_owner_backfill(
        self,
        org_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgOrgOwnerBackfillResponse:
        """
        Backfill the org owner for users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._post(
            f"/v2/admin/org/{org_name}/org-owner-backfill",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgOrgOwnerBackfillResponse,
        )


class AsyncOrgsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        return AsyncTeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncOrgsResourceWithStreamingResponse(self)

    async def org_owner_backfill(
        self,
        org_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgOrgOwnerBackfillResponse:
        """
        Backfill the org owner for users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return await self._post(
            f"/v2/admin/org/{org_name}/org-owner-backfill",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgOrgOwnerBackfillResponse,
        )


class OrgsResourceWithRawResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.org_owner_backfill = to_raw_response_wrapper(
            orgs.org_owner_backfill,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._orgs.users)

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self._orgs.teams)


class AsyncOrgsResourceWithRawResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.org_owner_backfill = async_to_raw_response_wrapper(
            orgs.org_owner_backfill,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._orgs.users)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self._orgs.teams)


class OrgsResourceWithStreamingResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.org_owner_backfill = to_streamed_response_wrapper(
            orgs.org_owner_backfill,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._orgs.users)

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self._orgs.teams)


class AsyncOrgsResourceWithStreamingResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.org_owner_backfill = async_to_streamed_response_wrapper(
            orgs.org_owner_backfill,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._orgs.users)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self._orgs.teams)
