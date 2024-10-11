# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.shared.user import User
from .....types.admin.orgs.teams import user_add_params, user_create_params, user_update_params, user_add_role_params

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

    def create(
        self,
        team_name: str,
        *,
        org_name: str,
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
        """
        Create an Org-Admin User (Super Admin privileges required)

        Args:
          email: Email address of the user. This should be unique.

          idp_id: If the IDP ID is provided then it is used instead of the one configured for the
              organization

          send_email: Boolean to send email notification, default is true

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
        if not team_name:
            raise ValueError(f"Expected a non-empty value for `team_name` but received {team_name!r}")
        return self._post(
            f"/v2/admin/org/{org_name}/team/{team_name}/users",
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
        infinity_manager_settings: user_update_params.InfinityManagerSettings | NotGiven = NOT_GIVEN,
        repo_scan_settings: user_update_params.RepoScanSettings | NotGiven = NOT_GIVEN,
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
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def add(
        self,
        id: str,
        *,
        org_name: str,
        team_name: str,
        user_role_defaults_to_registry_read: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Add existing User to an Team

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v2/admin/org/{org_name}/team/{team_name}/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"user_role_defaults_to_registry_read": user_role_defaults_to_registry_read},
                    user_add_params.UserAddParams,
                ),
            ),
            cast_to=User,
        )

    def add_role(
        self,
        id: str,
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
        Add user role in team.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v2/admin/org/{org_name}/team/{team_name}/users/{id}/add-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"roles": roles}, user_add_role_params.UserAddRoleParams),
            ),
            cast_to=User,
        )

    def retrieve_user(
        self,
        user_email_or_id: str,
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
        Get info and role/invitation in a team by email or id

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
        return self._get(
            f"/v3/orgs/{org_name}/teams/{team_name}/users/{user_email_or_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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

    async def create(
        self,
        team_name: str,
        *,
        org_name: str,
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
        """
        Create an Org-Admin User (Super Admin privileges required)

        Args:
          email: Email address of the user. This should be unique.

          idp_id: If the IDP ID is provided then it is used instead of the one configured for the
              organization

          send_email: Boolean to send email notification, default is true

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
        if not team_name:
            raise ValueError(f"Expected a non-empty value for `team_name` but received {team_name!r}")
        return await self._post(
            f"/v2/admin/org/{org_name}/team/{team_name}/users",
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
        infinity_manager_settings: user_update_params.InfinityManagerSettings | NotGiven = NOT_GIVEN,
        repo_scan_settings: user_update_params.RepoScanSettings | NotGiven = NOT_GIVEN,
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
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def add(
        self,
        id: str,
        *,
        org_name: str,
        team_name: str,
        user_role_defaults_to_registry_read: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Add existing User to an Team

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v2/admin/org/{org_name}/team/{team_name}/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"user_role_defaults_to_registry_read": user_role_defaults_to_registry_read},
                    user_add_params.UserAddParams,
                ),
            ),
            cast_to=User,
        )

    async def add_role(
        self,
        id: str,
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
        Add user role in team.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v2/admin/org/{org_name}/team/{team_name}/users/{id}/add-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"roles": roles}, user_add_role_params.UserAddRoleParams),
            ),
            cast_to=User,
        )

    async def retrieve_user(
        self,
        user_email_or_id: str,
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
        Get info and role/invitation in a team by email or id

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
        return await self._get(
            f"/v3/orgs/{org_name}/teams/{team_name}/users/{user_email_or_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = to_custom_raw_response_wrapper(
            users.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            users.update,
            BinaryAPIResponse,
        )
        self.add = to_raw_response_wrapper(
            users.add,
        )
        self.add_role = to_raw_response_wrapper(
            users.add_role,
        )
        self.retrieve_user = to_raw_response_wrapper(
            users.retrieve_user,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_custom_raw_response_wrapper(
            users.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            users.update,
            AsyncBinaryAPIResponse,
        )
        self.add = async_to_raw_response_wrapper(
            users.add,
        )
        self.add_role = async_to_raw_response_wrapper(
            users.add_role,
        )
        self.retrieve_user = async_to_raw_response_wrapper(
            users.retrieve_user,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = to_custom_streamed_response_wrapper(
            users.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            users.update,
            StreamedBinaryAPIResponse,
        )
        self.add = to_streamed_response_wrapper(
            users.add,
        )
        self.add_role = to_streamed_response_wrapper(
            users.add_role,
        )
        self.retrieve_user = to_streamed_response_wrapper(
            users.retrieve_user,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_custom_streamed_response_wrapper(
            users.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            users.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.add = async_to_streamed_response_wrapper(
            users.add,
        )
        self.add_role = async_to_streamed_response_wrapper(
            users.add_role,
        )
        self.retrieve_user = async_to_streamed_response_wrapper(
            users.retrieve_user,
        )
