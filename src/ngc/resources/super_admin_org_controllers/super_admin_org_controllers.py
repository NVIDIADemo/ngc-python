# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .org import (
    OrgResource,
    AsyncOrgResource,
    OrgResourceWithRawResponse,
    AsyncOrgResourceWithRawResponse,
    OrgResourceWithStreamingResponse,
    AsyncOrgResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["SuperAdminOrgControllersResource", "AsyncSuperAdminOrgControllersResource"]


class SuperAdminOrgControllersResource(SyncAPIResource):
    @cached_property
    def org(self) -> OrgResource:
        return OrgResource(self._client)

    @cached_property
    def with_raw_response(self) -> SuperAdminOrgControllersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return SuperAdminOrgControllersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuperAdminOrgControllersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return SuperAdminOrgControllersResourceWithStreamingResponse(self)

    def backfill_orgs_to_kratos(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Backfill Orgs to Kratos"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v2/admin/backfill-orgs-to-kratos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSuperAdminOrgControllersResource(AsyncAPIResource):
    @cached_property
    def org(self) -> AsyncOrgResource:
        return AsyncOrgResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSuperAdminOrgControllersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuperAdminOrgControllersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuperAdminOrgControllersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncSuperAdminOrgControllersResourceWithStreamingResponse(self)

    async def backfill_orgs_to_kratos(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Backfill Orgs to Kratos"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v2/admin/backfill-orgs-to-kratos",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SuperAdminOrgControllersResourceWithRawResponse:
    def __init__(self, super_admin_org_controllers: SuperAdminOrgControllersResource) -> None:
        self._super_admin_org_controllers = super_admin_org_controllers

        self.backfill_orgs_to_kratos = to_custom_raw_response_wrapper(
            super_admin_org_controllers.backfill_orgs_to_kratos,
            BinaryAPIResponse,
        )

    @cached_property
    def org(self) -> OrgResourceWithRawResponse:
        return OrgResourceWithRawResponse(self._super_admin_org_controllers.org)


class AsyncSuperAdminOrgControllersResourceWithRawResponse:
    def __init__(self, super_admin_org_controllers: AsyncSuperAdminOrgControllersResource) -> None:
        self._super_admin_org_controllers = super_admin_org_controllers

        self.backfill_orgs_to_kratos = async_to_custom_raw_response_wrapper(
            super_admin_org_controllers.backfill_orgs_to_kratos,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def org(self) -> AsyncOrgResourceWithRawResponse:
        return AsyncOrgResourceWithRawResponse(self._super_admin_org_controllers.org)


class SuperAdminOrgControllersResourceWithStreamingResponse:
    def __init__(self, super_admin_org_controllers: SuperAdminOrgControllersResource) -> None:
        self._super_admin_org_controllers = super_admin_org_controllers

        self.backfill_orgs_to_kratos = to_custom_streamed_response_wrapper(
            super_admin_org_controllers.backfill_orgs_to_kratos,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def org(self) -> OrgResourceWithStreamingResponse:
        return OrgResourceWithStreamingResponse(self._super_admin_org_controllers.org)


class AsyncSuperAdminOrgControllersResourceWithStreamingResponse:
    def __init__(self, super_admin_org_controllers: AsyncSuperAdminOrgControllersResource) -> None:
        self._super_admin_org_controllers = super_admin_org_controllers

        self.backfill_orgs_to_kratos = async_to_custom_streamed_response_wrapper(
            super_admin_org_controllers.backfill_orgs_to_kratos,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def org(self) -> AsyncOrgResourceWithStreamingResponse:
        return AsyncOrgResourceWithStreamingResponse(self._super_admin_org_controllers.org)
