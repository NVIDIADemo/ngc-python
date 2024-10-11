# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .orgs import (
    OrgsResource,
    AsyncOrgsResource,
    OrgsResourceWithRawResponse,
    AsyncOrgsResourceWithRawResponse,
    OrgsResourceWithStreamingResponse,
    AsyncOrgsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .orgs.orgs import OrgsResource, AsyncOrgsResource
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.user import User
from ...types.super_admin_user_crm_sync_response import SuperAdminUserCRMSyncResponse

__all__ = ["SuperAdminUserResource", "AsyncSuperAdminUserResource"]


class SuperAdminUserResource(SyncAPIResource):
    @cached_property
    def orgs(self) -> OrgsResource:
        return OrgsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SuperAdminUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return SuperAdminUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuperAdminUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return SuperAdminUserResourceWithStreamingResponse(self)

    def crm_sync(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuperAdminUserCRMSyncResponse:
        """
        Sync crm id with user email (Super Admin privileges required)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/v2/admin/users/{id}/crm-sync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuperAdminUserCRMSyncResponse,
        )

    def migrate_deprecated_roles(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Migrate User Deprecated Roles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v2/admin/users/{id}/migrate-deprecated-roles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AsyncSuperAdminUserResource(AsyncAPIResource):
    @cached_property
    def orgs(self) -> AsyncOrgsResource:
        return AsyncOrgsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSuperAdminUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuperAdminUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuperAdminUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncSuperAdminUserResourceWithStreamingResponse(self)

    async def crm_sync(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuperAdminUserCRMSyncResponse:
        """
        Sync crm id with user email (Super Admin privileges required)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/v2/admin/users/{id}/crm-sync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuperAdminUserCRMSyncResponse,
        )

    async def migrate_deprecated_roles(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Migrate User Deprecated Roles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v2/admin/users/{id}/migrate-deprecated-roles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class SuperAdminUserResourceWithRawResponse:
    def __init__(self, super_admin_user: SuperAdminUserResource) -> None:
        self._super_admin_user = super_admin_user

        self.crm_sync = to_raw_response_wrapper(
            super_admin_user.crm_sync,
        )
        self.migrate_deprecated_roles = to_raw_response_wrapper(
            super_admin_user.migrate_deprecated_roles,
        )

    @cached_property
    def orgs(self) -> OrgsResourceWithRawResponse:
        return OrgsResourceWithRawResponse(self._super_admin_user.orgs)


class AsyncSuperAdminUserResourceWithRawResponse:
    def __init__(self, super_admin_user: AsyncSuperAdminUserResource) -> None:
        self._super_admin_user = super_admin_user

        self.crm_sync = async_to_raw_response_wrapper(
            super_admin_user.crm_sync,
        )
        self.migrate_deprecated_roles = async_to_raw_response_wrapper(
            super_admin_user.migrate_deprecated_roles,
        )

    @cached_property
    def orgs(self) -> AsyncOrgsResourceWithRawResponse:
        return AsyncOrgsResourceWithRawResponse(self._super_admin_user.orgs)


class SuperAdminUserResourceWithStreamingResponse:
    def __init__(self, super_admin_user: SuperAdminUserResource) -> None:
        self._super_admin_user = super_admin_user

        self.crm_sync = to_streamed_response_wrapper(
            super_admin_user.crm_sync,
        )
        self.migrate_deprecated_roles = to_streamed_response_wrapper(
            super_admin_user.migrate_deprecated_roles,
        )

    @cached_property
    def orgs(self) -> OrgsResourceWithStreamingResponse:
        return OrgsResourceWithStreamingResponse(self._super_admin_user.orgs)


class AsyncSuperAdminUserResourceWithStreamingResponse:
    def __init__(self, super_admin_user: AsyncSuperAdminUserResource) -> None:
        self._super_admin_user = super_admin_user

        self.crm_sync = async_to_streamed_response_wrapper(
            super_admin_user.crm_sync,
        )
        self.migrate_deprecated_roles = async_to_streamed_response_wrapper(
            super_admin_user.migrate_deprecated_roles,
        )

    @cached_property
    def orgs(self) -> AsyncOrgsResourceWithStreamingResponse:
        return AsyncOrgsResourceWithStreamingResponse(self._super_admin_user.orgs)
