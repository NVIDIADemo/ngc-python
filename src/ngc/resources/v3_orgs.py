# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import v3_org_validate_params
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
from ..types.org_invitation import OrgInvitation

__all__ = ["V3OrgsResource", "AsyncV3OrgsResource"]


class V3OrgsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V3OrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return V3OrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3OrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return V3OrgsResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        invitation_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgInvitation:
        """
        Validate org creation from proto org

        Args:
          invitation_token: JWT that contains org owner email and proto org identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/orgs/proto-org/validate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"invitation_token": invitation_token}, v3_org_validate_params.V3OrgValidateParams
                ),
            ),
            cast_to=OrgInvitation,
        )


class AsyncV3OrgsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV3OrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV3OrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3OrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncV3OrgsResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        invitation_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgInvitation:
        """
        Validate org creation from proto org

        Args:
          invitation_token: JWT that contains org owner email and proto org identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/orgs/proto-org/validate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"invitation_token": invitation_token}, v3_org_validate_params.V3OrgValidateParams
                ),
            ),
            cast_to=OrgInvitation,
        )


class V3OrgsResourceWithRawResponse:
    def __init__(self, v3_orgs: V3OrgsResource) -> None:
        self._v3_orgs = v3_orgs

        self.validate = to_raw_response_wrapper(
            v3_orgs.validate,
        )


class AsyncV3OrgsResourceWithRawResponse:
    def __init__(self, v3_orgs: AsyncV3OrgsResource) -> None:
        self._v3_orgs = v3_orgs

        self.validate = async_to_raw_response_wrapper(
            v3_orgs.validate,
        )


class V3OrgsResourceWithStreamingResponse:
    def __init__(self, v3_orgs: V3OrgsResource) -> None:
        self._v3_orgs = v3_orgs

        self.validate = to_streamed_response_wrapper(
            v3_orgs.validate,
        )


class AsyncV3OrgsResourceWithStreamingResponse:
    def __init__(self, v3_orgs: AsyncV3OrgsResource) -> None:
        self._v3_orgs = v3_orgs

        self.validate = async_to_streamed_response_wrapper(
            v3_orgs.validate,
        )
