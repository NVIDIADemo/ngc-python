# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.user import User

__all__ = ["V3OrgsUsersResource", "AsyncV3OrgsUsersResource"]


class V3OrgsUsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V3OrgsUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return V3OrgsUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3OrgsUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return V3OrgsUsersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        user_email_or_id: str,
        *,
        org_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Get info and role/invitation in an org by email or id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return self._get(
            f"/v3/orgs/{org_name}/users/{user_email_or_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AsyncV3OrgsUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV3OrgsUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV3OrgsUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3OrgsUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncV3OrgsUsersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        user_email_or_id: str,
        *,
        org_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Get info and role/invitation in an org by email or id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_name:
            raise ValueError(f"Expected a non-empty value for `org_name` but received {org_name!r}")
        if not user_email_or_id:
            raise ValueError(f"Expected a non-empty value for `user_email_or_id` but received {user_email_or_id!r}")
        return await self._get(
            f"/v3/orgs/{org_name}/users/{user_email_or_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class V3OrgsUsersResourceWithRawResponse:
    def __init__(self, v3_orgs_users: V3OrgsUsersResource) -> None:
        self._v3_orgs_users = v3_orgs_users

        self.retrieve = to_raw_response_wrapper(
            v3_orgs_users.retrieve,
        )


class AsyncV3OrgsUsersResourceWithRawResponse:
    def __init__(self, v3_orgs_users: AsyncV3OrgsUsersResource) -> None:
        self._v3_orgs_users = v3_orgs_users

        self.retrieve = async_to_raw_response_wrapper(
            v3_orgs_users.retrieve,
        )


class V3OrgsUsersResourceWithStreamingResponse:
    def __init__(self, v3_orgs_users: V3OrgsUsersResource) -> None:
        self._v3_orgs_users = v3_orgs_users

        self.retrieve = to_streamed_response_wrapper(
            v3_orgs_users.retrieve,
        )


class AsyncV3OrgsUsersResourceWithStreamingResponse:
    def __init__(self, v3_orgs_users: AsyncV3OrgsUsersResource) -> None:
        self._v3_orgs_users = v3_orgs_users

        self.retrieve = async_to_streamed_response_wrapper(
            v3_orgs_users.retrieve,
        )
