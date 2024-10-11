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
from ...._base_client import make_request_options
from ....types.admin.orgs import user_add_params, user_create_params, user_add_role_params, user_get_entitlements_params
from ....types.shared.user import User
from ....types.admin.orgs.user_remove_response import UserRemoveResponse

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
        """
        Create an user in an Organization (Super Admin privileges required)

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
        return self._post(
            f"/v2/admin/org/{org_name}/users",
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

    def add(
        self,
        id: str,
        *,
        org_name: str,
        user_role_defaults_to_registry_read: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Add existing User to an Org

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
        return self._post(
            f"/v2/admin/org/{org_name}/users/{id}",
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
        roles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Add user role in org.

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
            f"/v2/admin/org/{org_name}/users/{id}/add-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"roles": roles}, user_add_role_params.UserAddRoleParams),
            ),
            cast_to=User,
        )

    def get_entitlements(
        self,
        org_name: str,
        *,
        is_paid_subscription: bool | NotGiven = NOT_GIVEN,
        product_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """List all organizations with entitlements.

        (SuperAdmin, ECM and Billing
        privileges required)

        Args:
          is_paid_subscription: get is paid subscription entitlements

          product_name: filter by product-name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v2/admin/org/{org_name}/entitlements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_paid_subscription": is_paid_subscription,
                        "product_name": product_name,
                    },
                    user_get_entitlements_params.UserGetEntitlementsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def remove(
        self,
        id: str,
        *,
        org_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRemoveResponse:
        """
        Remove User from org.

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
        return self._delete(
            f"/v2/admin/org/{org_name}/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveResponse,
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
        """
        Create an user in an Organization (Super Admin privileges required)

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
        return await self._post(
            f"/v2/admin/org/{org_name}/users",
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

    async def add(
        self,
        id: str,
        *,
        org_name: str,
        user_role_defaults_to_registry_read: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Add existing User to an Org

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
        return await self._post(
            f"/v2/admin/org/{org_name}/users/{id}",
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
        roles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Add user role in org.

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
            f"/v2/admin/org/{org_name}/users/{id}/add-role",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"roles": roles}, user_add_role_params.UserAddRoleParams),
            ),
            cast_to=User,
        )

    async def get_entitlements(
        self,
        org_name: str,
        *,
        is_paid_subscription: bool | NotGiven = NOT_GIVEN,
        product_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """List all organizations with entitlements.

        (SuperAdmin, ECM and Billing
        privileges required)

        Args:
          is_paid_subscription: get is paid subscription entitlements

          product_name: filter by product-name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v2/admin/org/{org_name}/entitlements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_paid_subscription": is_paid_subscription,
                        "product_name": product_name,
                    },
                    user_get_entitlements_params.UserGetEntitlementsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def remove(
        self,
        id: str,
        *,
        org_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRemoveResponse:
        """
        Remove User from org.

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
        return await self._delete(
            f"/v2/admin/org/{org_name}/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.add = to_raw_response_wrapper(
            users.add,
        )
        self.add_role = to_raw_response_wrapper(
            users.add_role,
        )
        self.get_entitlements = to_custom_raw_response_wrapper(
            users.get_entitlements,
            BinaryAPIResponse,
        )
        self.remove = to_raw_response_wrapper(
            users.remove,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.add = async_to_raw_response_wrapper(
            users.add,
        )
        self.add_role = async_to_raw_response_wrapper(
            users.add_role,
        )
        self.get_entitlements = async_to_custom_raw_response_wrapper(
            users.get_entitlements,
            AsyncBinaryAPIResponse,
        )
        self.remove = async_to_raw_response_wrapper(
            users.remove,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.add = to_streamed_response_wrapper(
            users.add,
        )
        self.add_role = to_streamed_response_wrapper(
            users.add_role,
        )
        self.get_entitlements = to_custom_streamed_response_wrapper(
            users.get_entitlements,
            StreamedBinaryAPIResponse,
        )
        self.remove = to_streamed_response_wrapper(
            users.remove,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.add = async_to_streamed_response_wrapper(
            users.add,
        )
        self.add_role = async_to_streamed_response_wrapper(
            users.add_role,
        )
        self.get_entitlements = async_to_custom_streamed_response_wrapper(
            users.get_entitlements,
            AsyncStreamedBinaryAPIResponse,
        )
        self.remove = async_to_streamed_response_wrapper(
            users.remove,
        )
