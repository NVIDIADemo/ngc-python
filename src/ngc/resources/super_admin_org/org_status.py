# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ...types.super_admin_org import org_status_create_params

__all__ = ["OrgStatusResource", "AsyncOrgStatusResource"]


class OrgStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrgStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return OrgStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return OrgStatusResourceWithStreamingResponse(self)

    def create(
        self,
        org_name: str,
        *,
        create_subscription: bool,
        product_enablement: org_status_create_params.ProductEnablement,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Create org product enablement

        Args:
          create_subscription: False only if called by SbMS.

          product_enablement: Product Enablement

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v2/admin/org/{org_name}/enablement",
            body=maybe_transform(
                {
                    "create_subscription": create_subscription,
                    "product_enablement": product_enablement,
                },
                org_status_create_params.OrgStatusCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncOrgStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrgStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncOrgStatusResourceWithStreamingResponse(self)

    async def create(
        self,
        org_name: str,
        *,
        create_subscription: bool,
        product_enablement: org_status_create_params.ProductEnablement,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Create org product enablement

        Args:
          create_subscription: False only if called by SbMS.

          product_enablement: Product Enablement

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v2/admin/org/{org_name}/enablement",
            body=await async_maybe_transform(
                {
                    "create_subscription": create_subscription,
                    "product_enablement": product_enablement,
                },
                org_status_create_params.OrgStatusCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class OrgStatusResourceWithRawResponse:
    def __init__(self, org_status: OrgStatusResource) -> None:
        self._org_status = org_status

        self.create = to_custom_raw_response_wrapper(
            org_status.create,
            BinaryAPIResponse,
        )


class AsyncOrgStatusResourceWithRawResponse:
    def __init__(self, org_status: AsyncOrgStatusResource) -> None:
        self._org_status = org_status

        self.create = async_to_custom_raw_response_wrapper(
            org_status.create,
            AsyncBinaryAPIResponse,
        )


class OrgStatusResourceWithStreamingResponse:
    def __init__(self, org_status: OrgStatusResource) -> None:
        self._org_status = org_status

        self.create = to_custom_streamed_response_wrapper(
            org_status.create,
            StreamedBinaryAPIResponse,
        )


class AsyncOrgStatusResourceWithStreamingResponse:
    def __init__(self, org_status: AsyncOrgStatusResource) -> None:
        self._org_status = org_status

        self.create = async_to_custom_streamed_response_wrapper(
            org_status.create,
            AsyncStreamedBinaryAPIResponse,
        )
