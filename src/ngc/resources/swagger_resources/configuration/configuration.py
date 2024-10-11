# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ui import (
    UiResource,
    AsyncUiResource,
    UiResourceWithRawResponse,
    AsyncUiResourceWithRawResponse,
    UiResourceWithStreamingResponse,
    AsyncUiResourceWithStreamingResponse,
)
from .security import (
    SecurityResource,
    AsyncSecurityResource,
    SecurityResourceWithRawResponse,
    AsyncSecurityResourceWithRawResponse,
    SecurityResourceWithStreamingResponse,
    AsyncSecurityResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ConfigurationResource", "AsyncConfigurationResource"]


class ConfigurationResource(SyncAPIResource):
    @cached_property
    def ui(self) -> UiResource:
        return UiResource(self._client)

    @cached_property
    def security(self) -> SecurityResource:
        return SecurityResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return ConfigurationResourceWithStreamingResponse(self)


class AsyncConfigurationResource(AsyncAPIResource):
    @cached_property
    def ui(self) -> AsyncUiResource:
        return AsyncUiResource(self._client)

    @cached_property
    def security(self) -> AsyncSecurityResource:
        return AsyncSecurityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncConfigurationResourceWithStreamingResponse(self)


class ConfigurationResourceWithRawResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

    @cached_property
    def ui(self) -> UiResourceWithRawResponse:
        return UiResourceWithRawResponse(self._configuration.ui)

    @cached_property
    def security(self) -> SecurityResourceWithRawResponse:
        return SecurityResourceWithRawResponse(self._configuration.security)


class AsyncConfigurationResourceWithRawResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

    @cached_property
    def ui(self) -> AsyncUiResourceWithRawResponse:
        return AsyncUiResourceWithRawResponse(self._configuration.ui)

    @cached_property
    def security(self) -> AsyncSecurityResourceWithRawResponse:
        return AsyncSecurityResourceWithRawResponse(self._configuration.security)


class ConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

    @cached_property
    def ui(self) -> UiResourceWithStreamingResponse:
        return UiResourceWithStreamingResponse(self._configuration.ui)

    @cached_property
    def security(self) -> SecurityResourceWithStreamingResponse:
        return SecurityResourceWithStreamingResponse(self._configuration.security)


class AsyncConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

    @cached_property
    def ui(self) -> AsyncUiResourceWithStreamingResponse:
        return AsyncUiResourceWithStreamingResponse(self._configuration.ui)

    @cached_property
    def security(self) -> AsyncSecurityResourceWithStreamingResponse:
        return AsyncSecurityResourceWithStreamingResponse(self._configuration.security)
