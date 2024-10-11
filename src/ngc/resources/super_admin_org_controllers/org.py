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
from ...types.super_admin_org_controllers import org_update_params

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)

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
    ) -> BinaryAPIResponse:
        """Get organization or proto organization info.

        (SuperAdmin privileges required)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v3/admin/org/{org_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        org_name: str,
        *,
        alternate_contact: org_update_params.AlternateContact | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        idp_id: str | NotGiven = NOT_GIVEN,
        infinity_manager_settings: org_update_params.InfinityManagerSettings | NotGiven = NOT_GIVEN,
        is_dataset_service_enabled: bool | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        is_quick_start_enabled: bool | NotGiven = NOT_GIVEN,
        is_registry_sse_enabled: bool | NotGiven = NOT_GIVEN,
        is_secrets_manager_service_enabled: bool | NotGiven = NOT_GIVEN,
        is_secure_credential_sharing_service_enabled: bool | NotGiven = NOT_GIVEN,
        is_separate_influx_db_used: bool | NotGiven = NOT_GIVEN,
        org_owner: org_update_params.OrgOwner | NotGiven = NOT_GIVEN,
        org_owners: Iterable[org_update_params.OrgOwner] | NotGiven = NOT_GIVEN,
        pec_name: str | NotGiven = NOT_GIVEN,
        pec_sfdc_id: str | NotGiven = NOT_GIVEN,
        product_enablements: Iterable[org_update_params.ProductEnablement] | NotGiven = NOT_GIVEN,
        product_subscriptions: Iterable[org_update_params.ProductSubscription] | NotGiven = NOT_GIVEN,
        repo_scan_settings: org_update_params.RepoScanSettings | NotGiven = NOT_GIVEN,
        type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Update org information and settings.

        Superadmin privileges required

        Args:
          alternate_contact: Org Owner Alternate Contact

          company_name: Name of the company

          description: optional description of the organization

          display_name: Name of the organization that will be shown to users.

          idp_id: Identity Provider ID.

          infinity_manager_settings: Infinity manager setting definition

          is_dataset_service_enabled: Dataset Service enable flag for an organization

          is_internal: Is NVIDIA internal org or not

          is_quick_start_enabled: Quick Start enable flag for an organization

          is_registry_sse_enabled: If a server side encryption is enabled for private registry (models, resources)

          is_secrets_manager_service_enabled: Secrets Manager Service enable flag for an organization

          is_secure_credential_sharing_service_enabled: Secure Credential Sharing Service enable flag for an organization

          is_separate_influx_db_used: If a separate influx db used for an organization in Base Command Platform job
              telemetry

          org_owner: Org owner.

          org_owners: Org owners

          pec_name: product end customer name for enterprise(Fleet Command) product

          pec_sfdc_id: product end customer salesforce.com Id (external customer Id) for
              enterprise(Fleet Command) product

          repo_scan_settings: Repo scan setting definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/v3/admin/org/{org_name}",
            body=maybe_transform(
                {
                    "alternate_contact": alternate_contact,
                    "company_name": company_name,
                    "description": description,
                    "display_name": display_name,
                    "idp_id": idp_id,
                    "infinity_manager_settings": infinity_manager_settings,
                    "is_dataset_service_enabled": is_dataset_service_enabled,
                    "is_internal": is_internal,
                    "is_quick_start_enabled": is_quick_start_enabled,
                    "is_registry_sse_enabled": is_registry_sse_enabled,
                    "is_secrets_manager_service_enabled": is_secrets_manager_service_enabled,
                    "is_secure_credential_sharing_service_enabled": is_secure_credential_sharing_service_enabled,
                    "is_separate_influx_db_used": is_separate_influx_db_used,
                    "org_owner": org_owner,
                    "org_owners": org_owners,
                    "pec_name": pec_name,
                    "pec_sfdc_id": pec_sfdc_id,
                    "product_enablements": product_enablements,
                    "product_subscriptions": product_subscriptions,
                    "repo_scan_settings": repo_scan_settings,
                    "type": type,
                },
                org_update_params.OrgUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)

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
    ) -> AsyncBinaryAPIResponse:
        """Get organization or proto organization info.

        (SuperAdmin privileges required)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v3/admin/org/{org_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        org_name: str,
        *,
        alternate_contact: org_update_params.AlternateContact | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        idp_id: str | NotGiven = NOT_GIVEN,
        infinity_manager_settings: org_update_params.InfinityManagerSettings | NotGiven = NOT_GIVEN,
        is_dataset_service_enabled: bool | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        is_quick_start_enabled: bool | NotGiven = NOT_GIVEN,
        is_registry_sse_enabled: bool | NotGiven = NOT_GIVEN,
        is_secrets_manager_service_enabled: bool | NotGiven = NOT_GIVEN,
        is_secure_credential_sharing_service_enabled: bool | NotGiven = NOT_GIVEN,
        is_separate_influx_db_used: bool | NotGiven = NOT_GIVEN,
        org_owner: org_update_params.OrgOwner | NotGiven = NOT_GIVEN,
        org_owners: Iterable[org_update_params.OrgOwner] | NotGiven = NOT_GIVEN,
        pec_name: str | NotGiven = NOT_GIVEN,
        pec_sfdc_id: str | NotGiven = NOT_GIVEN,
        product_enablements: Iterable[org_update_params.ProductEnablement] | NotGiven = NOT_GIVEN,
        product_subscriptions: Iterable[org_update_params.ProductSubscription] | NotGiven = NOT_GIVEN,
        repo_scan_settings: org_update_params.RepoScanSettings | NotGiven = NOT_GIVEN,
        type: Literal["UNKNOWN", "CLOUD", "ENTERPRISE", "INDIVIDUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Update org information and settings.

        Superadmin privileges required

        Args:
          alternate_contact: Org Owner Alternate Contact

          company_name: Name of the company

          description: optional description of the organization

          display_name: Name of the organization that will be shown to users.

          idp_id: Identity Provider ID.

          infinity_manager_settings: Infinity manager setting definition

          is_dataset_service_enabled: Dataset Service enable flag for an organization

          is_internal: Is NVIDIA internal org or not

          is_quick_start_enabled: Quick Start enable flag for an organization

          is_registry_sse_enabled: If a server side encryption is enabled for private registry (models, resources)

          is_secrets_manager_service_enabled: Secrets Manager Service enable flag for an organization

          is_secure_credential_sharing_service_enabled: Secure Credential Sharing Service enable flag for an organization

          is_separate_influx_db_used: If a separate influx db used for an organization in Base Command Platform job
              telemetry

          org_owner: Org owner.

          org_owners: Org owners

          pec_name: product end customer name for enterprise(Fleet Command) product

          pec_sfdc_id: product end customer salesforce.com Id (external customer Id) for
              enterprise(Fleet Command) product

          repo_scan_settings: Repo scan setting definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/v3/admin/org/{org_name}",
            body=await async_maybe_transform(
                {
                    "alternate_contact": alternate_contact,
                    "company_name": company_name,
                    "description": description,
                    "display_name": display_name,
                    "idp_id": idp_id,
                    "infinity_manager_settings": infinity_manager_settings,
                    "is_dataset_service_enabled": is_dataset_service_enabled,
                    "is_internal": is_internal,
                    "is_quick_start_enabled": is_quick_start_enabled,
                    "is_registry_sse_enabled": is_registry_sse_enabled,
                    "is_secrets_manager_service_enabled": is_secrets_manager_service_enabled,
                    "is_secure_credential_sharing_service_enabled": is_secure_credential_sharing_service_enabled,
                    "is_separate_influx_db_used": is_separate_influx_db_used,
                    "org_owner": org_owner,
                    "org_owners": org_owners,
                    "pec_name": pec_name,
                    "pec_sfdc_id": pec_sfdc_id,
                    "product_enablements": product_enablements,
                    "product_subscriptions": product_subscriptions,
                    "repo_scan_settings": repo_scan_settings,
                    "type": type,
                },
                org_update_params.OrgUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.retrieve = to_custom_raw_response_wrapper(
            org.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            org.update,
            BinaryAPIResponse,
        )


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.retrieve = async_to_custom_raw_response_wrapper(
            org.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            org.update,
            AsyncBinaryAPIResponse,
        )


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.retrieve = to_custom_streamed_response_wrapper(
            org.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            org.update,
            StreamedBinaryAPIResponse,
        )


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.retrieve = async_to_custom_streamed_response_wrapper(
            org.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            org.update,
            AsyncStreamedBinaryAPIResponse,
        )
