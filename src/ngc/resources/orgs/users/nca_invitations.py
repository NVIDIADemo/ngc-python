# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.orgs.users import nca_invitation_create_params
from ....types.shared.user import User

__all__ = ["NcaInvitationsResource", "AsyncNcaInvitationsResource"]


class NcaInvitationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NcaInvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return NcaInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NcaInvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return NcaInvitationsResourceWithStreamingResponse(self)

    def create(
        self,
        org_name: str,
        *,
        email: str | NotGiven = NOT_GIVEN,
        invitation_expiration_in: int | NotGiven = NOT_GIVEN,
        invite_as: Literal["ADMIN", "MEMBER"] | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Invites and creates a User in org

        Args:
          email: Is the user email

          invitation_expiration_in: Is the numbers of days the invitation will expire

          invite_as: Nca allow users to be invited as Admin and as Member

          message: Is a message to the new user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._post(
            f"/v3/orgs/{org_name}/users/nca-invitations",
            body=maybe_transform(
                {
                    "email": email,
                    "invitation_expiration_in": invitation_expiration_in,
                    "invite_as": invite_as,
                    "message": message,
                },
                nca_invitation_create_params.NcaInvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AsyncNcaInvitationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNcaInvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNcaInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNcaInvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncNcaInvitationsResourceWithStreamingResponse(self)

    async def create(
        self,
        org_name: str,
        *,
        email: str | NotGiven = NOT_GIVEN,
        invitation_expiration_in: int | NotGiven = NOT_GIVEN,
        invite_as: Literal["ADMIN", "MEMBER"] | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Invites and creates a User in org

        Args:
          email: Is the user email

          invitation_expiration_in: Is the numbers of days the invitation will expire

          invite_as: Nca allow users to be invited as Admin and as Member

          message: Is a message to the new user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return await self._post(
            f"/v3/orgs/{org_name}/users/nca-invitations",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "invitation_expiration_in": invitation_expiration_in,
                    "invite_as": invite_as,
                    "message": message,
                },
                nca_invitation_create_params.NcaInvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class NcaInvitationsResourceWithRawResponse:
    def __init__(self, nca_invitations: NcaInvitationsResource) -> None:
        self._nca_invitations = nca_invitations

        self.create = to_raw_response_wrapper(
            nca_invitations.create,
        )


class AsyncNcaInvitationsResourceWithRawResponse:
    def __init__(self, nca_invitations: AsyncNcaInvitationsResource) -> None:
        self._nca_invitations = nca_invitations

        self.create = async_to_raw_response_wrapper(
            nca_invitations.create,
        )


class NcaInvitationsResourceWithStreamingResponse:
    def __init__(self, nca_invitations: NcaInvitationsResource) -> None:
        self._nca_invitations = nca_invitations

        self.create = to_streamed_response_wrapper(
            nca_invitations.create,
        )


class AsyncNcaInvitationsResourceWithStreamingResponse:
    def __init__(self, nca_invitations: AsyncNcaInvitationsResource) -> None:
        self._nca_invitations = nca_invitations

        self.create = async_to_streamed_response_wrapper(
            nca_invitations.create,
        )
