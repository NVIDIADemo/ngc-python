# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .teams import (
    TeamsResource,
    AsyncTeamsResource,
    TeamsResourceWithRawResponse,
    AsyncTeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
    AsyncTeamsResourceWithStreamingResponse,
)
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import org_list_params, org_create_params, org_update_params
from .credits import (
    CreditsResource,
    AsyncCreditsResource,
    CreditsResourceWithRawResponse,
    AsyncCreditsResourceWithRawResponse,
    CreditsResourceWithStreamingResponse,
    AsyncCreditsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .metering import (
    MeteringResource,
    AsyncMeteringResource,
    MeteringResourceWithRawResponse,
    AsyncMeteringResourceWithRawResponse,
    MeteringResourceWithStreamingResponse,
    AsyncMeteringResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .proto_org import (
    ProtoOrgResource,
    AsyncProtoOrgResource,
    ProtoOrgResourceWithRawResponse,
    AsyncProtoOrgResourceWithRawResponse,
    ProtoOrgResourceWithStreamingResponse,
    AsyncProtoOrgResourceWithStreamingResponse,
)
from .audit_logs import (
    AuditLogsResource,
    AsyncAuditLogsResource,
    AuditLogsResourceWithRawResponse,
    AsyncAuditLogsResourceWithRawResponse,
    AuditLogsResourceWithStreamingResponse,
    AsyncAuditLogsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .teams.teams import TeamsResource, AsyncTeamsResource
from .users.users import UsersResource, AsyncUsersResource
from ...pagination import SyncPageNumberOrganizations, AsyncPageNumberOrganizations
from .starfleet_ids import (
    StarfleetIDsResource,
    AsyncStarfleetIDsResource,
    StarfleetIDsResourceWithRawResponse,
    AsyncStarfleetIDsResourceWithRawResponse,
    StarfleetIDsResourceWithStreamingResponse,
    AsyncStarfleetIDsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from .metering.metering import MeteringResource, AsyncMeteringResource
from ...types.org_response import OrgResponse
from ...types.org_list_response import OrgListResponse

__all__ = ["OrgsResource", "AsyncOrgsResource"]


class OrgsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def teams(self) -> TeamsResource:
        return TeamsResource(self._client)

    @cached_property
    def proto_org(self) -> ProtoOrgResource:
        return ProtoOrgResource(self._client)

    @cached_property
    def credits(self) -> CreditsResource:
        return CreditsResource(self._client)

    @cached_property
    def starfleet_ids(self) -> StarfleetIDsResource:
        return StarfleetIDsResource(self._client)

    @cached_property
    def metering(self) -> MeteringResource:
        return MeteringResource(self._client)

    @cached_property
    def audit_logs(self) -> AuditLogsResource:
        return AuditLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return OrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return OrgsResourceWithStreamingResponse(self)

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
        org_owner: org_create_params.OrgOwner | NotGiven = NOT_GIVEN,
        pec_name: str | NotGiven = NOT_GIVEN,
        pec_sfdc_id: str | NotGiven = NOT_GIVEN,
        product_enablements: Iterable[org_create_params.ProductEnablement] | NotGiven = NOT_GIVEN,
        product_subscriptions: Iterable[org_create_params.ProductSubscription] | NotGiven = NOT_GIVEN,
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
        Create a new organization based on the org info provided in the request.

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
            "/v3/orgs",
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
                org_create_params.OrgCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgResponse,
        )

    def retrieve(
        self,
        org_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgResponse:
        """
        Get organization information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._get(
            f"/v2/orgs/{org_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgResponse,
        )

    def update(
        self,
        org_name: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgResponse:
        """
        Update organization information

        Args:
          description: optional description of the organization

          display_name: Name of the organization that will be shown to users

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return self._patch(
            f"/v2/orgs/{org_name}",
            body=maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                },
                org_update_params.OrgUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgResponse,
        )

    def list(
        self,
        *,
        filter_using_org_display_name: str | NotGiven = NOT_GIVEN,
        filter_using_org_name: str | NotGiven = NOT_GIVEN,
        filter_using_org_owner_email: str | NotGiven = NOT_GIVEN,
        filter_using_org_owner_name: str | NotGiven = NOT_GIVEN,
        filter_using_pec_id: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPageNumberOrganizations[OrgListResponse]:
        """
        List all organizations of the user

        Args:
          page_number: The page number of result

          page_size: The page size of result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/orgs",
            page=SyncPageNumberOrganizations[OrgListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_using_org_display_name": filter_using_org_display_name,
                        "filter_using_org_name": filter_using_org_name,
                        "filter_using_org_owner_email": filter_using_org_owner_email,
                        "filter_using_org_owner_name": filter_using_org_owner_name,
                        "filter_using_pec_id": filter_using_pec_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    org_list_params.OrgListParams,
                ),
            ),
            model=OrgListResponse,
        )


class AsyncOrgsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        return AsyncTeamsResource(self._client)

    @cached_property
    def proto_org(self) -> AsyncProtoOrgResource:
        return AsyncProtoOrgResource(self._client)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        return AsyncCreditsResource(self._client)

    @cached_property
    def starfleet_ids(self) -> AsyncStarfleetIDsResource:
        return AsyncStarfleetIDsResource(self._client)

    @cached_property
    def metering(self) -> AsyncMeteringResource:
        return AsyncMeteringResource(self._client)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResource:
        return AsyncAuditLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncOrgsResourceWithStreamingResponse(self)

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
        org_owner: org_create_params.OrgOwner | NotGiven = NOT_GIVEN,
        pec_name: str | NotGiven = NOT_GIVEN,
        pec_sfdc_id: str | NotGiven = NOT_GIVEN,
        product_enablements: Iterable[org_create_params.ProductEnablement] | NotGiven = NOT_GIVEN,
        product_subscriptions: Iterable[org_create_params.ProductSubscription] | NotGiven = NOT_GIVEN,
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
        Create a new organization based on the org info provided in the request.

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
            "/v3/orgs",
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
                org_create_params.OrgCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgResponse,
        )

    async def retrieve(
        self,
        org_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgResponse:
        """
        Get organization information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return await self._get(
            f"/v2/orgs/{org_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgResponse,
        )

    async def update(
        self,
        org_name: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgResponse:
        """
        Update organization information

        Args:
          description: optional description of the organization

          display_name: Name of the organization that will be shown to users

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        return await self._patch(
            f"/v2/orgs/{org_name}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                },
                org_update_params.OrgUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgResponse,
        )

    def list(
        self,
        *,
        filter_using_org_display_name: str | NotGiven = NOT_GIVEN,
        filter_using_org_name: str | NotGiven = NOT_GIVEN,
        filter_using_org_owner_email: str | NotGiven = NOT_GIVEN,
        filter_using_org_owner_name: str | NotGiven = NOT_GIVEN,
        filter_using_pec_id: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OrgListResponse, AsyncPageNumberOrganizations[OrgListResponse]]:
        """
        List all organizations of the user

        Args:
          page_number: The page number of result

          page_size: The page size of result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/orgs",
            page=AsyncPageNumberOrganizations[OrgListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_using_org_display_name": filter_using_org_display_name,
                        "filter_using_org_name": filter_using_org_name,
                        "filter_using_org_owner_email": filter_using_org_owner_email,
                        "filter_using_org_owner_name": filter_using_org_owner_name,
                        "filter_using_pec_id": filter_using_pec_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    org_list_params.OrgListParams,
                ),
            ),
            model=OrgListResponse,
        )


class OrgsResourceWithRawResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.create = to_raw_response_wrapper(
            orgs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            orgs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            orgs.update,
        )
        self.list = to_raw_response_wrapper(
            orgs.list,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._orgs.users)

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self._orgs.teams)

    @cached_property
    def proto_org(self) -> ProtoOrgResourceWithRawResponse:
        return ProtoOrgResourceWithRawResponse(self._orgs.proto_org)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._orgs.credits)

    @cached_property
    def starfleet_ids(self) -> StarfleetIDsResourceWithRawResponse:
        return StarfleetIDsResourceWithRawResponse(self._orgs.starfleet_ids)

    @cached_property
    def metering(self) -> MeteringResourceWithRawResponse:
        return MeteringResourceWithRawResponse(self._orgs.metering)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithRawResponse:
        return AuditLogsResourceWithRawResponse(self._orgs.audit_logs)


class AsyncOrgsResourceWithRawResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.create = async_to_raw_response_wrapper(
            orgs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            orgs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            orgs.update,
        )
        self.list = async_to_raw_response_wrapper(
            orgs.list,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._orgs.users)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self._orgs.teams)

    @cached_property
    def proto_org(self) -> AsyncProtoOrgResourceWithRawResponse:
        return AsyncProtoOrgResourceWithRawResponse(self._orgs.proto_org)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._orgs.credits)

    @cached_property
    def starfleet_ids(self) -> AsyncStarfleetIDsResourceWithRawResponse:
        return AsyncStarfleetIDsResourceWithRawResponse(self._orgs.starfleet_ids)

    @cached_property
    def metering(self) -> AsyncMeteringResourceWithRawResponse:
        return AsyncMeteringResourceWithRawResponse(self._orgs.metering)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithRawResponse:
        return AsyncAuditLogsResourceWithRawResponse(self._orgs.audit_logs)


class OrgsResourceWithStreamingResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.create = to_streamed_response_wrapper(
            orgs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            orgs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            orgs.update,
        )
        self.list = to_streamed_response_wrapper(
            orgs.list,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._orgs.users)

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self._orgs.teams)

    @cached_property
    def proto_org(self) -> ProtoOrgResourceWithStreamingResponse:
        return ProtoOrgResourceWithStreamingResponse(self._orgs.proto_org)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._orgs.credits)

    @cached_property
    def starfleet_ids(self) -> StarfleetIDsResourceWithStreamingResponse:
        return StarfleetIDsResourceWithStreamingResponse(self._orgs.starfleet_ids)

    @cached_property
    def metering(self) -> MeteringResourceWithStreamingResponse:
        return MeteringResourceWithStreamingResponse(self._orgs.metering)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithStreamingResponse:
        return AuditLogsResourceWithStreamingResponse(self._orgs.audit_logs)


class AsyncOrgsResourceWithStreamingResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.create = async_to_streamed_response_wrapper(
            orgs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            orgs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            orgs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            orgs.list,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._orgs.users)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self._orgs.teams)

    @cached_property
    def proto_org(self) -> AsyncProtoOrgResourceWithStreamingResponse:
        return AsyncProtoOrgResourceWithStreamingResponse(self._orgs.proto_org)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._orgs.credits)

    @cached_property
    def starfleet_ids(self) -> AsyncStarfleetIDsResourceWithStreamingResponse:
        return AsyncStarfleetIDsResourceWithStreamingResponse(self._orgs.starfleet_ids)

    @cached_property
    def metering(self) -> AsyncMeteringResourceWithStreamingResponse:
        return AsyncMeteringResourceWithStreamingResponse(self._orgs.metering)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        return AsyncAuditLogsResourceWithStreamingResponse(self._orgs.audit_logs)
