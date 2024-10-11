# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import v2_admin_org_entitlement_retrieve_all_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["V2AdminOrgEntitlementsResource", "AsyncV2AdminOrgEntitlementsResource"]


class V2AdminOrgEntitlementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2AdminOrgEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return V2AdminOrgEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2AdminOrgEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return V2AdminOrgEntitlementsResourceWithStreamingResponse(self)

    def retrieve_all(
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
                    v2_admin_org_entitlement_retrieve_all_params.V2AdminOrgEntitlementRetrieveAllParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncV2AdminOrgEntitlementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2AdminOrgEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2AdminOrgEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2AdminOrgEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncV2AdminOrgEntitlementsResourceWithStreamingResponse(self)

    async def retrieve_all(
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
                    v2_admin_org_entitlement_retrieve_all_params.V2AdminOrgEntitlementRetrieveAllParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class V2AdminOrgEntitlementsResourceWithRawResponse:
    def __init__(self, v2_admin_org_entitlements: V2AdminOrgEntitlementsResource) -> None:
        self._v2_admin_org_entitlements = v2_admin_org_entitlements

        self.retrieve_all = to_custom_raw_response_wrapper(
            v2_admin_org_entitlements.retrieve_all,
            BinaryAPIResponse,
        )


class AsyncV2AdminOrgEntitlementsResourceWithRawResponse:
    def __init__(self, v2_admin_org_entitlements: AsyncV2AdminOrgEntitlementsResource) -> None:
        self._v2_admin_org_entitlements = v2_admin_org_entitlements

        self.retrieve_all = async_to_custom_raw_response_wrapper(
            v2_admin_org_entitlements.retrieve_all,
            AsyncBinaryAPIResponse,
        )


class V2AdminOrgEntitlementsResourceWithStreamingResponse:
    def __init__(self, v2_admin_org_entitlements: V2AdminOrgEntitlementsResource) -> None:
        self._v2_admin_org_entitlements = v2_admin_org_entitlements

        self.retrieve_all = to_custom_streamed_response_wrapper(
            v2_admin_org_entitlements.retrieve_all,
            StreamedBinaryAPIResponse,
        )


class AsyncV2AdminOrgEntitlementsResourceWithStreamingResponse:
    def __init__(self, v2_admin_org_entitlements: AsyncV2AdminOrgEntitlementsResource) -> None:
        self._v2_admin_org_entitlements = v2_admin_org_entitlements

        self.retrieve_all = async_to_custom_streamed_response_wrapper(
            v2_admin_org_entitlements.retrieve_all,
            AsyncStreamedBinaryAPIResponse,
        )
