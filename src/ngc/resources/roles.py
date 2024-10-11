# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import role_retrieve_all_params
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
from ..types.user_role_definitions import UserRoleDefinitions

__all__ = ["RolesResource", "AsyncRolesResource"]


class RolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return RolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return RolesResourceWithStreamingResponse(self)

    def retrieve_all(
        self,
        *,
        show_hidden: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRoleDefinitions:
        """
        List of roles in NGC and their scopes

        Args:
          show_hidden: flag indicate if hidden roles should be included

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"show_hidden": show_hidden}, role_retrieve_all_params.RoleRetrieveAllParams),
            ),
            cast_to=UserRoleDefinitions,
        )


class AsyncRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncRolesResourceWithStreamingResponse(self)

    async def retrieve_all(
        self,
        *,
        show_hidden: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRoleDefinitions:
        """
        List of roles in NGC and their scopes

        Args:
          show_hidden: flag indicate if hidden roles should be included

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"show_hidden": show_hidden}, role_retrieve_all_params.RoleRetrieveAllParams
                ),
            ),
            cast_to=UserRoleDefinitions,
        )


class RolesResourceWithRawResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.retrieve_all = to_raw_response_wrapper(
            roles.retrieve_all,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.retrieve_all = async_to_raw_response_wrapper(
            roles.retrieve_all,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.retrieve_all = to_streamed_response_wrapper(
            roles.retrieve_all,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.retrieve_all = async_to_streamed_response_wrapper(
            roles.retrieve_all,
        )
