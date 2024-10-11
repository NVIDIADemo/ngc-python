# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import super_admin_org_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .org_status import (
    OrgStatusResource,
    AsyncOrgStatusResource,
    OrgStatusResourceWithRawResponse,
    AsyncOrgStatusResourceWithRawResponse,
    OrgStatusResourceWithStreamingResponse,
    AsyncOrgStatusResourceWithStreamingResponse,
)
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

__all__ = ["SuperAdminOrgResource", "AsyncSuperAdminOrgResource"]


class SuperAdminOrgResource(SyncAPIResource):
    @cached_property
    def org_status(self) -> OrgStatusResource:
        return OrgStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> SuperAdminOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return SuperAdminOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuperAdminOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return SuperAdminOrgResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        org_owner: super_admin_org_create_params.OrgOwner,
        country: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        idp_id: str | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pec_name: str | NotGiven = NOT_GIVEN,
        pec_sfdc_id: str | NotGiven = NOT_GIVEN,
        product_enablements: Iterable[super_admin_org_create_params.ProductEnablement] | NotGiven = NOT_GIVEN,
        product_subscriptions: Iterable[super_admin_org_create_params.ProductSubscription] | NotGiven = NOT_GIVEN,
        salesforce_account_industry: str | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Create a new organization.

        (SuperAdmin privileges required)

        Args:
          org_owner: Org owner.

          country: user country

          description: optional description of the organization

          display_name: Name of the organization that will be shown to users.

          idp_id: Identity Provider ID.

          is_internal: Is NVIDIA internal org or not

          name: Organization name

          pec_name: product end customer name for enterprise(Fleet Command) product

          pec_sfdc_id: product end customer salesforce.com Id (external customer Id) for
              enterprise(Fleet Command) product

          product_subscriptions: This should be deprecated, use productEnablements instead

          salesforce_account_industry: Company or organization industry

          send_email: Send email to org owner or not. Default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v2/admin/orgs",
            body=maybe_transform(
                {
                    "org_owner": org_owner,
                    "country": country,
                    "description": description,
                    "display_name": display_name,
                    "idp_id": idp_id,
                    "is_internal": is_internal,
                    "name": name,
                    "pec_name": pec_name,
                    "pec_sfdc_id": pec_sfdc_id,
                    "product_enablements": product_enablements,
                    "product_subscriptions": product_subscriptions,
                    "salesforce_account_industry": salesforce_account_industry,
                    "send_email": send_email,
                    "type": type,
                },
                super_admin_org_create_params.SuperAdminOrgCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSuperAdminOrgResource(AsyncAPIResource):
    @cached_property
    def org_status(self) -> AsyncOrgStatusResource:
        return AsyncOrgStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSuperAdminOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuperAdminOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuperAdminOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncSuperAdminOrgResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        org_owner: super_admin_org_create_params.OrgOwner,
        country: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        idp_id: str | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        pec_name: str | NotGiven = NOT_GIVEN,
        pec_sfdc_id: str | NotGiven = NOT_GIVEN,
        product_enablements: Iterable[super_admin_org_create_params.ProductEnablement] | NotGiven = NOT_GIVEN,
        product_subscriptions: Iterable[super_admin_org_create_params.ProductSubscription] | NotGiven = NOT_GIVEN,
        salesforce_account_industry: str | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Create a new organization.

        (SuperAdmin privileges required)

        Args:
          org_owner: Org owner.

          country: user country

          description: optional description of the organization

          display_name: Name of the organization that will be shown to users.

          idp_id: Identity Provider ID.

          is_internal: Is NVIDIA internal org or not

          name: Organization name

          pec_name: product end customer name for enterprise(Fleet Command) product

          pec_sfdc_id: product end customer salesforce.com Id (external customer Id) for
              enterprise(Fleet Command) product

          product_subscriptions: This should be deprecated, use productEnablements instead

          salesforce_account_industry: Company or organization industry

          send_email: Send email to org owner or not. Default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v2/admin/orgs",
            body=await async_maybe_transform(
                {
                    "org_owner": org_owner,
                    "country": country,
                    "description": description,
                    "display_name": display_name,
                    "idp_id": idp_id,
                    "is_internal": is_internal,
                    "name": name,
                    "pec_name": pec_name,
                    "pec_sfdc_id": pec_sfdc_id,
                    "product_enablements": product_enablements,
                    "product_subscriptions": product_subscriptions,
                    "salesforce_account_industry": salesforce_account_industry,
                    "send_email": send_email,
                    "type": type,
                },
                super_admin_org_create_params.SuperAdminOrgCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SuperAdminOrgResourceWithRawResponse:
    def __init__(self, super_admin_org: SuperAdminOrgResource) -> None:
        self._super_admin_org = super_admin_org

        self.create = to_custom_raw_response_wrapper(
            super_admin_org.create,
            BinaryAPIResponse,
        )

    @cached_property
    def org_status(self) -> OrgStatusResourceWithRawResponse:
        return OrgStatusResourceWithRawResponse(self._super_admin_org.org_status)


class AsyncSuperAdminOrgResourceWithRawResponse:
    def __init__(self, super_admin_org: AsyncSuperAdminOrgResource) -> None:
        self._super_admin_org = super_admin_org

        self.create = async_to_custom_raw_response_wrapper(
            super_admin_org.create,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def org_status(self) -> AsyncOrgStatusResourceWithRawResponse:
        return AsyncOrgStatusResourceWithRawResponse(self._super_admin_org.org_status)


class SuperAdminOrgResourceWithStreamingResponse:
    def __init__(self, super_admin_org: SuperAdminOrgResource) -> None:
        self._super_admin_org = super_admin_org

        self.create = to_custom_streamed_response_wrapper(
            super_admin_org.create,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def org_status(self) -> OrgStatusResourceWithStreamingResponse:
        return OrgStatusResourceWithStreamingResponse(self._super_admin_org.org_status)


class AsyncSuperAdminOrgResourceWithStreamingResponse:
    def __init__(self, super_admin_org: AsyncSuperAdminOrgResource) -> None:
        self._super_admin_org = super_admin_org

        self.create = async_to_custom_streamed_response_wrapper(
            super_admin_org.create,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def org_status(self) -> AsyncOrgStatusResourceWithStreamingResponse:
        return AsyncOrgStatusResourceWithStreamingResponse(self._super_admin_org.org_status)
