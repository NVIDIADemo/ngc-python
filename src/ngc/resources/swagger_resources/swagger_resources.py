# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .configuration import (
    ConfigurationResource,
    AsyncConfigurationResource,
    ConfigurationResourceWithRawResponse,
    AsyncConfigurationResourceWithRawResponse,
    ConfigurationResourceWithStreamingResponse,
    AsyncConfigurationResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .configuration.configuration import ConfigurationResource, AsyncConfigurationResource

__all__ = ["SwaggerResourcesResource", "AsyncSwaggerResourcesResource"]


class SwaggerResourcesResource(SyncAPIResource):
    @cached_property
    def configuration(self) -> ConfigurationResource:
        return ConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> SwaggerResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return SwaggerResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SwaggerResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return SwaggerResourcesResourceWithStreamingResponse(self)

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
            "/swagger-resources",
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
            "/swagger-resources",
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
            "/swagger-resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def retrieve_all(
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
            "/swagger-resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSwaggerResourcesResource(AsyncAPIResource):
    @cached_property
    def configuration(self) -> AsyncConfigurationResource:
        return AsyncConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSwaggerResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSwaggerResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSwaggerResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncSwaggerResourcesResourceWithStreamingResponse(self)

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
            "/swagger-resources",
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
            "/swagger-resources",
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
            "/swagger-resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def retrieve_all(
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
            "/swagger-resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SwaggerResourcesResourceWithRawResponse:
    def __init__(self, swagger_resources: SwaggerResourcesResource) -> None:
        self._swagger_resources = swagger_resources

        self.create = to_custom_raw_response_wrapper(
            swagger_resources.create,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            swagger_resources.update,
            BinaryAPIResponse,
        )
        self.delete = to_custom_raw_response_wrapper(
            swagger_resources.delete,
            BinaryAPIResponse,
        )
        self.retrieve_all = to_custom_raw_response_wrapper(
            swagger_resources.retrieve_all,
            BinaryAPIResponse,
        )

    @cached_property
    def configuration(self) -> ConfigurationResourceWithRawResponse:
        return ConfigurationResourceWithRawResponse(self._swagger_resources.configuration)


class AsyncSwaggerResourcesResourceWithRawResponse:
    def __init__(self, swagger_resources: AsyncSwaggerResourcesResource) -> None:
        self._swagger_resources = swagger_resources

        self.create = async_to_custom_raw_response_wrapper(
            swagger_resources.create,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            swagger_resources.update,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_custom_raw_response_wrapper(
            swagger_resources.delete,
            AsyncBinaryAPIResponse,
        )
        self.retrieve_all = async_to_custom_raw_response_wrapper(
            swagger_resources.retrieve_all,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithRawResponse:
        return AsyncConfigurationResourceWithRawResponse(self._swagger_resources.configuration)


class SwaggerResourcesResourceWithStreamingResponse:
    def __init__(self, swagger_resources: SwaggerResourcesResource) -> None:
        self._swagger_resources = swagger_resources

        self.create = to_custom_streamed_response_wrapper(
            swagger_resources.create,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            swagger_resources.update,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_custom_streamed_response_wrapper(
            swagger_resources.delete,
            StreamedBinaryAPIResponse,
        )
        self.retrieve_all = to_custom_streamed_response_wrapper(
            swagger_resources.retrieve_all,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def configuration(self) -> ConfigurationResourceWithStreamingResponse:
        return ConfigurationResourceWithStreamingResponse(self._swagger_resources.configuration)


class AsyncSwaggerResourcesResourceWithStreamingResponse:
    def __init__(self, swagger_resources: AsyncSwaggerResourcesResource) -> None:
        self._swagger_resources = swagger_resources

        self.create = async_to_custom_streamed_response_wrapper(
            swagger_resources.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            swagger_resources.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_custom_streamed_response_wrapper(
            swagger_resources.delete,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retrieve_all = async_to_custom_streamed_response_wrapper(
            swagger_resources.retrieve_all,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithStreamingResponse:
        return AsyncConfigurationResourceWithStreamingResponse(self._swagger_resources.configuration)
