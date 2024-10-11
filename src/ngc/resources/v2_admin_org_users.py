# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import v2_admin_org_user_add_role_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.user import User

__all__ = ["V2AdminOrgUsersResource", "AsyncV2AdminOrgUsersResource"]


class V2AdminOrgUsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2AdminOrgUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return V2AdminOrgUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2AdminOrgUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return V2AdminOrgUsersResourceWithStreamingResponse(self)

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
                query=maybe_transform({"roles": roles}, v2_admin_org_user_add_role_params.V2AdminOrgUserAddRoleParams),
            ),
            cast_to=User,
        )


class AsyncV2AdminOrgUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2AdminOrgUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2AdminOrgUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2AdminOrgUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncV2AdminOrgUsersResourceWithStreamingResponse(self)

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
                query=await async_maybe_transform(
                    {"roles": roles}, v2_admin_org_user_add_role_params.V2AdminOrgUserAddRoleParams
                ),
            ),
            cast_to=User,
        )


class V2AdminOrgUsersResourceWithRawResponse:
    def __init__(self, v2_admin_org_users: V2AdminOrgUsersResource) -> None:
        self._v2_admin_org_users = v2_admin_org_users

        self.add_role = to_raw_response_wrapper(
            v2_admin_org_users.add_role,
        )


class AsyncV2AdminOrgUsersResourceWithRawResponse:
    def __init__(self, v2_admin_org_users: AsyncV2AdminOrgUsersResource) -> None:
        self._v2_admin_org_users = v2_admin_org_users

        self.add_role = async_to_raw_response_wrapper(
            v2_admin_org_users.add_role,
        )


class V2AdminOrgUsersResourceWithStreamingResponse:
    def __init__(self, v2_admin_org_users: V2AdminOrgUsersResource) -> None:
        self._v2_admin_org_users = v2_admin_org_users

        self.add_role = to_streamed_response_wrapper(
            v2_admin_org_users.add_role,
        )


class AsyncV2AdminOrgUsersResourceWithStreamingResponse:
    def __init__(self, v2_admin_org_users: AsyncV2AdminOrgUsersResource) -> None:
        self._v2_admin_org_users = v2_admin_org_users

        self.add_role = async_to_streamed_response_wrapper(
            v2_admin_org_users.add_role,
        )
