# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ....types.orgs.teams import user_delete_params, user_add_role_params, user_remove_role_params
from ....types.shared.user import User
from ....types.orgs.teams.user_delete_response import UserDeleteResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def delete(
        self,
        id: str,
        *,
        org_name: str,
        team_name: str,
        anonymize: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteResponse:
        """
        Remove User from team.

        Args:
          anonymize: If anonymize is true, then org owner permission is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not team_name:
            raise ValueError(f"Expected a non-empty value for `team_name` but received {team_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v3/orgs/{org_name}/teams/{team_name}/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"anonymize": anonymize}, user_delete_params.UserDeleteParams),
            ),
            cast_to=UserDeleteResponse,
        )

    def add_role(
        self,
        user_email_or_id: str,
        *,
        org_name: str,
        team_name: str,
        roles: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Invite if user does not exist, otherwise add role in team

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
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return self._patch(
            f"/v3/orgs/{org_name}/teams/{team_name}/users/{user_email_or_id}/add-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"roles": roles}, user_add_role_params.UserAddRoleParams),
            ),
            cast_to=User,
        )

    def remove_role(
        self,
        user_email_or_id: str,
        *,
        org_name: str,
        team_name: str,
        roles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Remove role in team if user exists, otherwise remove invitation

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
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return self._delete(
            f"/v3/orgs/{org_name}/teams/{team_name}/users/{user_email_or_id}/remove-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"roles": roles}, user_remove_role_params.UserRemoveRoleParams),
            ),
            cast_to=User,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def delete(
        self,
        id: str,
        *,
        org_name: str,
        team_name: str,
        anonymize: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteResponse:
        """
        Remove User from team.

        Args:
          anonymize: If anonymize is true, then org owner permission is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not team_name:
            raise ValueError(f"Expected a non-empty value for `team_name` but received {team_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v3/orgs/{org_name}/teams/{team_name}/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"anonymize": anonymize}, user_delete_params.UserDeleteParams),
            ),
            cast_to=UserDeleteResponse,
        )

    async def add_role(
        self,
        user_email_or_id: str,
        *,
        org_name: str,
        team_name: str,
        roles: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Invite if user does not exist, otherwise add role in team

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
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return await self._patch(
            f"/v3/orgs/{org_name}/teams/{team_name}/users/{user_email_or_id}/add-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"roles": roles}, user_add_role_params.UserAddRoleParams),
            ),
            cast_to=User,
        )

    async def remove_role(
        self,
        user_email_or_id: str,
        *,
        org_name: str,
        team_name: str,
        roles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Remove role in team if user exists, otherwise remove invitation

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
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return await self._delete(
            f"/v3/orgs/{org_name}/teams/{team_name}/users/{user_email_or_id}/remove-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"roles": roles}, user_remove_role_params.UserRemoveRoleParams),
            ),
            cast_to=User,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.add_role = to_raw_response_wrapper(
            users.add_role,
        )
        self.remove_role = to_raw_response_wrapper(
            users.remove_role,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.add_role = async_to_raw_response_wrapper(
            users.add_role,
        )
        self.remove_role = async_to_raw_response_wrapper(
            users.remove_role,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.add_role = to_streamed_response_wrapper(
            users.add_role,
        )
        self.remove_role = to_streamed_response_wrapper(
            users.remove_role,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.add_role = async_to_streamed_response_wrapper(
            users.add_role,
        )
        self.remove_role = async_to_streamed_response_wrapper(
            users.remove_role,
        )
