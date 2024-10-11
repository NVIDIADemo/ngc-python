# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["SecurityResource", "AsyncSecurityResource"]


class SecurityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return SecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return SecurityResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/swagger-resources/configuration/security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/swagger-resources/configuration/security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            "/swagger-resources/configuration/security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/swagger-resources/configuration/security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSecurityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncSecurityResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/swagger-resources/configuration/security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/swagger-resources/configuration/security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            "/swagger-resources/configuration/security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/swagger-resources/configuration/security",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SecurityResourceWithRawResponse:
    def __init__(self, security: SecurityResource) -> None:
        self._security = security

        self.create = to_custom_raw_response_wrapper(
            security.create,
            BinaryAPIResponse,
        )
        self.retrieve = to_custom_raw_response_wrapper(
            security.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            security.update,
            BinaryAPIResponse,
        )
        self.delete = to_custom_raw_response_wrapper(
            security.delete,
            BinaryAPIResponse,
        )


class AsyncSecurityResourceWithRawResponse:
    def __init__(self, security: AsyncSecurityResource) -> None:
        self._security = security

        self.create = async_to_custom_raw_response_wrapper(
            security.create,
            AsyncBinaryAPIResponse,
        )
        self.retrieve = async_to_custom_raw_response_wrapper(
            security.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            security.update,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_custom_raw_response_wrapper(
            security.delete,
            AsyncBinaryAPIResponse,
        )


class SecurityResourceWithStreamingResponse:
    def __init__(self, security: SecurityResource) -> None:
        self._security = security

        self.create = to_custom_streamed_response_wrapper(
            security.create,
            StreamedBinaryAPIResponse,
        )
        self.retrieve = to_custom_streamed_response_wrapper(
            security.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            security.update,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_custom_streamed_response_wrapper(
            security.delete,
            StreamedBinaryAPIResponse,
        )


class AsyncSecurityResourceWithStreamingResponse:
    def __init__(self, security: AsyncSecurityResource) -> None:
        self._security = security

        self.create = async_to_custom_streamed_response_wrapper(
            security.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retrieve = async_to_custom_streamed_response_wrapper(
            security.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            security.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_custom_streamed_response_wrapper(
            security.delete,
            AsyncStreamedBinaryAPIResponse,
        )
