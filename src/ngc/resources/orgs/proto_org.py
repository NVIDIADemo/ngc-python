# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.orgs import proto_org_create_params
from ..._base_client import make_request_options
from ...types.org_response import OrgResponse

__all__ = ["ProtoOrgResource", "AsyncProtoOrgResource"]


class ProtoOrgResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProtoOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return ProtoOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProtoOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return ProtoOrgResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        country: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        initiator: str | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        nca_id: str | NotGiven = NOT_GIVEN,
        nca_number: str | NotGiven = NOT_GIVEN,
        org_owner: proto_org_create_params.OrgOwner | NotGiven = NOT_GIVEN,
        pec_name: str | NotGiven = NOT_GIVEN,
        pec_sfdc_id: str | NotGiven = NOT_GIVEN,
        product_enablements: Iterable[proto_org_create_params.ProductEnablement] | NotGiven = NOT_GIVEN,
        product_subscriptions: Iterable[proto_org_create_params.ProductSubscription] | NotGiven = NOT_GIVEN,
        proto_org_id: str | NotGiven = NOT_GIVEN,
        salesforce_account_industry: str | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgResponse:
        """
        Create a new organization based on the org info retrieved from the ProtoOrg.

        Args:
          country: user country

          description: optional description of the organization

          display_name: Name of the organization that will be shown to users.

          initiator: Identify the initiator of the org request

          is_internal: Is NVIDIA internal org or not

          name: Organization name

          nca_id: NVIDIA Cloud Account Identifier

          nca_number: NVIDIA Cloud Account Number

          org_owner: Org owner.

          pec_name: product end customer name for enterprise(Fleet Command) product

          pec_sfdc_id: product end customer salesforce.com Id (external customer Id) for
              enterprise(Fleet Command) product

          product_subscriptions: This should be deprecated, use productEnablements instead

          proto_org_id: Proto org identifier

          salesforce_account_industry: Company or organization industry

          send_email: Send email to org owner or not. Default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/orgs/proto-org",
            body=maybe_transform(
                {
                    "country": country,
                    "description": description,
                    "display_name": display_name,
                    "initiator": initiator,
                    "is_internal": is_internal,
                    "name": name,
                    "nca_id": nca_id,
                    "nca_number": nca_number,
                    "org_owner": org_owner,
                    "pec_name": pec_name,
                    "pec_sfdc_id": pec_sfdc_id,
                    "product_enablements": product_enablements,
                    "product_subscriptions": product_subscriptions,
                    "proto_org_id": proto_org_id,
                    "salesforce_account_industry": salesforce_account_industry,
                    "send_email": send_email,
                    "type": type,
                },
                proto_org_create_params.ProtoOrgCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgResponse,
        )


class AsyncProtoOrgResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProtoOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProtoOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProtoOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncProtoOrgResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        country: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        initiator: str | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        nca_id: str | NotGiven = NOT_GIVEN,
        nca_number: str | NotGiven = NOT_GIVEN,
        org_owner: proto_org_create_params.OrgOwner | NotGiven = NOT_GIVEN,
        pec_name: str | NotGiven = NOT_GIVEN,
        pec_sfdc_id: str | NotGiven = NOT_GIVEN,
        product_enablements: Iterable[proto_org_create_params.ProductEnablement] | NotGiven = NOT_GIVEN,
        product_subscriptions: Iterable[proto_org_create_params.ProductSubscription] | NotGiven = NOT_GIVEN,
        proto_org_id: str | NotGiven = NOT_GIVEN,
        salesforce_account_industry: str | NotGiven = NOT_GIVEN,
        send_email: bool | NotGiven = NOT_GIVEN,
        type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgResponse:
        """
        Create a new organization based on the org info retrieved from the ProtoOrg.

        Args:
          country: user country

          description: optional description of the organization

          display_name: Name of the organization that will be shown to users.

          initiator: Identify the initiator of the org request

          is_internal: Is NVIDIA internal org or not

          name: Organization name

          nca_id: NVIDIA Cloud Account Identifier

          nca_number: NVIDIA Cloud Account Number

          org_owner: Org owner.

          pec_name: product end customer name for enterprise(Fleet Command) product

          pec_sfdc_id: product end customer salesforce.com Id (external customer Id) for
              enterprise(Fleet Command) product

          product_subscriptions: This should be deprecated, use productEnablements instead

          proto_org_id: Proto org identifier

          salesforce_account_industry: Company or organization industry

          send_email: Send email to org owner or not. Default is true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/orgs/proto-org",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "description": description,
                    "display_name": display_name,
                    "initiator": initiator,
                    "is_internal": is_internal,
                    "name": name,
                    "nca_id": nca_id,
                    "nca_number": nca_number,
                    "org_owner": org_owner,
                    "pec_name": pec_name,
                    "pec_sfdc_id": pec_sfdc_id,
                    "product_enablements": product_enablements,
                    "product_subscriptions": product_subscriptions,
                    "proto_org_id": proto_org_id,
                    "salesforce_account_industry": salesforce_account_industry,
                    "send_email": send_email,
                    "type": type,
                },
                proto_org_create_params.ProtoOrgCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgResponse,
        )


class ProtoOrgResourceWithRawResponse:
    def __init__(self, proto_org: ProtoOrgResource) -> None:
        self._proto_org = proto_org

        self.create = to_raw_response_wrapper(
            proto_org.create,
        )


class AsyncProtoOrgResourceWithRawResponse:
    def __init__(self, proto_org: AsyncProtoOrgResource) -> None:
        self._proto_org = proto_org

        self.create = async_to_raw_response_wrapper(
            proto_org.create,
        )


class ProtoOrgResourceWithStreamingResponse:
    def __init__(self, proto_org: ProtoOrgResource) -> None:
        self._proto_org = proto_org

        self.create = to_streamed_response_wrapper(
            proto_org.create,
        )


class AsyncProtoOrgResourceWithStreamingResponse:
    def __init__(self, proto_org: AsyncProtoOrgResource) -> None:
        self._proto_org = proto_org

        self.create = async_to_streamed_response_wrapper(
            proto_org.create,
        )
