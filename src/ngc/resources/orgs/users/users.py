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
from ....pagination import SyncPageNumberUsers, AsyncPageNumberUsers
from ....types.orgs import (
    user_list_params,
    user_create_params,
    user_delete_params,
    user_add_role_params,
    user_remove_role_params,
    user_update_role_params,
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
from ....types.shared.user import User
from ....types.orgs.user_list_response import UserListResponse
from ....types.orgs.user_delete_response import UserDeleteResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def nca_invitations(self) -> NcaInvitationsResource:
        return NcaInvitationsResource(self._client)

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

    def create(
        self,
        org_name: str,
        *,
        email: str,
        idp_id: str | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        email_opt_in: bool | NotGiven = NOT_GIVEN,
        eula_accepted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        role_type: str | NotGiven = NOT_GIVEN,
        role_types: List[str] | NotGiven = NOT_GIVEN,
        salesforce_contact_job_role: str | NotGiven = NOT_GIVEN,
        user_metadata: user_create_params.UserMetadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """Creates a User

        Args:
          email: Email address of the user.

        This should be unique.

          idp_id: If the IDP ID is provided then it is used instead of the one configured for the
              organization

          email_opt_in: indicates if user has opt in to nvidia emails

          eula_accepted: indicates if user has accepted EULA

          name: user name

          role_type: DEPRECATED - use roleTypes which allows multiple roles

          role_types: feature roles to give to the user

          salesforce_contact_job_role: user job role

          user_metadata: Metadata information about the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._post(
            f"/v2/org/{org_name}/users",
            body=maybe_transform(
                {
                    "email": email,
                    "email_opt_in": email_opt_in,
                    "eula_accepted": eula_accepted,
                    "name": name,
                    "role_type": role_type,
                    "role_types": role_types,
                    "salesforce_contact_job_role": salesforce_contact_job_role,
                    "user_metadata": user_metadata,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "idp_id": idp_id,
                        "send_email": send_email,
                    },
                    user_create_params.UserCreateParams,
                ),
            ),
            cast_to=User,
        )

    def list(
        self,
        org_name: str,
        *,
        exclude_from_team: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        q: user_list_params.Q | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageNumberUsers[UserListResponse]:
        """Get list of users in organization.

        (User Admin in org privileges required)

        Args:
          exclude_from_team: Name of team to exclude members from

          page_number: The page number of result

          page_size: The page size of result

          q: User Search Parameters. Only 'filters' and 'orderBy' for 'name' and 'email' are
              implemented

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._get_api_list(
            f"/v2/org/{org_name}/users",
            page=SyncPageNumberUsers[UserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_from_team": exclude_from_team,
                        "page_number": page_number,
                        "page_size": page_size,
                        "q": q,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=UserListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        org_name: str,
        anonymize: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteResponse:
        """
        Remove User from org.

        Args:
          anonymize: If anonymize is true, then org owner permission is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v3/orgs/{org_name}/users/{id}",
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
        roles: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Invite if user does not exist, otherwise add role in org

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return self._patch(
            f"/v3/orgs/{org_name}/users/{user_email_or_id}/add-role",
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
        roles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Remove role in org if user exists, otherwise remove invitation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return self._delete(
            f"/v3/orgs/{org_name}/users/{user_email_or_id}/remove-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"roles": roles}, user_remove_role_params.UserRemoveRoleParams),
            ),
            cast_to=User,
        )

    def update_role(
        self,
        id: str,
        *,
        org_name: str,
        roles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Update User Role in org

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v2/org/{org_name}/users/{id}/update-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"roles": roles}, user_update_role_params.UserUpdateRoleParams),
            ),
            cast_to=User,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def nca_invitations(self) -> AsyncNcaInvitationsResource:
        return AsyncNcaInvitationsResource(self._client)

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

    async def create(
        self,
        org_name: str,
        *,
        email: str,
        idp_id: str | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        email_opt_in: bool | NotGiven = NOT_GIVEN,
        eula_accepted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        role_type: str | NotGiven = NOT_GIVEN,
        role_types: List[str] | NotGiven = NOT_GIVEN,
        salesforce_contact_job_role: str | NotGiven = NOT_GIVEN,
        user_metadata: user_create_params.UserMetadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """Creates a User

        Args:
          email: Email address of the user.

        This should be unique.

          idp_id: If the IDP ID is provided then it is used instead of the one configured for the
              organization

          email_opt_in: indicates if user has opt in to nvidia emails

          eula_accepted: indicates if user has accepted EULA

          name: user name

          role_type: DEPRECATED - use roleTypes which allows multiple roles

          role_types: feature roles to give to the user

          salesforce_contact_job_role: user job role

          user_metadata: Metadata information about the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return await self._post(
            f"/v2/org/{org_name}/users",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "email_opt_in": email_opt_in,
                    "eula_accepted": eula_accepted,
                    "name": name,
                    "role_type": role_type,
                    "role_types": role_types,
                    "salesforce_contact_job_role": salesforce_contact_job_role,
                    "user_metadata": user_metadata,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "idp_id": idp_id,
                        "send_email": send_email,
                    },
                    user_create_params.UserCreateParams,
                ),
            ),
            cast_to=User,
        )

    def list(
        self,
        org_name: str,
        *,
        exclude_from_team: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        q: user_list_params.Q | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[UserListResponse, AsyncPageNumberUsers[UserListResponse]]:
        """Get list of users in organization.

        (User Admin in org privileges required)

        Args:
          exclude_from_team: Name of team to exclude members from

          page_number: The page number of result

          page_size: The page size of result

          q: User Search Parameters. Only 'filters' and 'orderBy' for 'name' and 'email' are
              implemented

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._get_api_list(
            f"/v2/org/{org_name}/users",
            page=AsyncPageNumberUsers[UserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_from_team": exclude_from_team,
                        "page_number": page_number,
                        "page_size": page_size,
                        "q": q,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=UserListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        org_name: str,
        anonymize: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteResponse:
        """
        Remove User from org.

        Args:
          anonymize: If anonymize is true, then org owner permission is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v3/orgs/{org_name}/users/{id}",
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
        roles: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Invite if user does not exist, otherwise add role in org

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return await self._patch(
            f"/v3/orgs/{org_name}/users/{user_email_or_id}/add-role",
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
        roles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Remove role in org if user exists, otherwise remove invitation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return await self._delete(
            f"/v3/orgs/{org_name}/users/{user_email_or_id}/remove-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"roles": roles}, user_remove_role_params.UserRemoveRoleParams),
            ),
            cast_to=User,
        )

    async def update_role(
        self,
        id: str,
        *,
        org_name: str,
        roles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Update User Role in org

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v2/org/{org_name}/users/{id}/update-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"roles": roles}, user_update_role_params.UserUpdateRoleParams),
            ),
            cast_to=User,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.add_role = to_raw_response_wrapper(
            users.add_role,
        )
        self.remove_role = to_raw_response_wrapper(
            users.remove_role,
        )
        self.update_role = to_raw_response_wrapper(
            users.update_role,
        )

    @cached_property
    def nca_invitations(self) -> NcaInvitationsResourceWithRawResponse:
        return NcaInvitationsResourceWithRawResponse(self._users.nca_invitations)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.add_role = async_to_raw_response_wrapper(
            users.add_role,
        )
        self.remove_role = async_to_raw_response_wrapper(
            users.remove_role,
        )
        self.update_role = async_to_raw_response_wrapper(
            users.update_role,
        )

    @cached_property
    def nca_invitations(self) -> AsyncNcaInvitationsResourceWithRawResponse:
        return AsyncNcaInvitationsResourceWithRawResponse(self._users.nca_invitations)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.add_role = to_streamed_response_wrapper(
            users.add_role,
        )
        self.remove_role = to_streamed_response_wrapper(
            users.remove_role,
        )
        self.update_role = to_streamed_response_wrapper(
            users.update_role,
        )

    @cached_property
    def nca_invitations(self) -> NcaInvitationsResourceWithStreamingResponse:
        return NcaInvitationsResourceWithStreamingResponse(self._users.nca_invitations)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.add_role = async_to_streamed_response_wrapper(
            users.add_role,
        )
        self.remove_role = async_to_streamed_response_wrapper(
            users.remove_role,
        )
        self.update_role = async_to_streamed_response_wrapper(
            users.update_role,
        )

    @cached_property
    def nca_invitations(self) -> AsyncNcaInvitationsResourceWithStreamingResponse:
        return AsyncNcaInvitationsResourceWithStreamingResponse(self._users.nca_invitations)
