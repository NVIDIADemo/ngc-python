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

__all__ = ["UiResource", "AsyncUiResource"]


class UiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return UiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return UiResourceWithStreamingResponse(self)

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
            "/swagger-resources/configuration/ui",
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
            "/swagger-resources/configuration/ui",
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
            "/swagger-resources/configuration/ui",
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
            "/swagger-resources/configuration/ui",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncUiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncUiResourceWithStreamingResponse(self)

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
            "/swagger-resources/configuration/ui",
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
            "/swagger-resources/configuration/ui",
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
            "/swagger-resources/configuration/ui",
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
            "/swagger-resources/configuration/ui",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class UiResourceWithRawResponse:
    def __init__(self, ui: UiResource) -> None:
        self._ui = ui

        self.create = to_custom_raw_response_wrapper(
            ui.create,
            BinaryAPIResponse,
        )
        self.retrieve = to_custom_raw_response_wrapper(
            ui.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            ui.update,
            BinaryAPIResponse,
        )
        self.delete = to_custom_raw_response_wrapper(
            ui.delete,
            BinaryAPIResponse,
        )


class AsyncUiResourceWithRawResponse:
    def __init__(self, ui: AsyncUiResource) -> None:
        self._ui = ui

        self.create = async_to_custom_raw_response_wrapper(
            ui.create,
            AsyncBinaryAPIResponse,
        )
        self.retrieve = async_to_custom_raw_response_wrapper(
            ui.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            ui.update,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_custom_raw_response_wrapper(
            ui.delete,
            AsyncBinaryAPIResponse,
        )


class UiResourceWithStreamingResponse:
    def __init__(self, ui: UiResource) -> None:
        self._ui = ui

        self.create = to_custom_streamed_response_wrapper(
            ui.create,
            StreamedBinaryAPIResponse,
        )
        self.retrieve = to_custom_streamed_response_wrapper(
            ui.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            ui.update,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_custom_streamed_response_wrapper(
            ui.delete,
            StreamedBinaryAPIResponse,
        )


class AsyncUiResourceWithStreamingResponse:
    def __init__(self, ui: AsyncUiResource) -> None:
        self._ui = ui

        self.create = async_to_custom_streamed_response_wrapper(
            ui.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retrieve = async_to_custom_streamed_response_wrapper(
            ui.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            ui.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_custom_streamed_response_wrapper(
            ui.delete,
            AsyncStreamedBinaryAPIResponse,
        )
