# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import NgcError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Ngc",
    "AsyncNgc",
    "Client",
    "AsyncClient",
]


class Ngc(SyncAPIClient):
    orgs: resources.OrgsResource
    me: resources.MeResource
    admin: resources.AdminResource
    users_management: resources.UsersManagementResource
    services: resources.ServicesResource
    roles: resources.RolesResource
    public_keys: resources.PublicKeysResource
    health: resources.HealthResource
    swagger_resources: resources.SwaggerResourcesResource
    with_raw_response: NgcWithRawResponse
    with_streaming_response: NgcWithStreamedResponse

    # client options
    auth_token: str

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ngc client instance.

        This automatically infers the `auth_token` argument from the `NVCF_AUTH_TOKEN` environment variable if it is not provided.
        """
        if auth_token is None:
            auth_token = os.environ.get("NVCF_AUTH_TOKEN")
        if auth_token is None:
            raise NgcError(
                "The auth_token client option must be set either by passing auth_token to the client or by setting the NVCF_AUTH_TOKEN environment variable"
            )
        self.auth_token = auth_token

        if base_url is None:
            base_url = os.environ.get("NGC_BASE_URL")
        if base_url is None:
            base_url = f"https://api.ngc.nvidia.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.orgs = resources.OrgsResource(self)
        self.me = resources.MeResource(self)
        self.admin = resources.AdminResource(self)
        self.users_management = resources.UsersManagementResource(self)
        self.services = resources.ServicesResource(self)
        self.roles = resources.RolesResource(self)
        self.public_keys = resources.PublicKeysResource(self)
        self.health = resources.HealthResource(self)
        self.swagger_resources = resources.SwaggerResourcesResource(self)
        self.with_raw_response = NgcWithRawResponse(self)
        self.with_streaming_response = NgcWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncNgc(AsyncAPIClient):
    orgs: resources.AsyncOrgsResource
    me: resources.AsyncMeResource
    admin: resources.AsyncAdminResource
    users_management: resources.AsyncUsersManagementResource
    services: resources.AsyncServicesResource
    roles: resources.AsyncRolesResource
    public_keys: resources.AsyncPublicKeysResource
    health: resources.AsyncHealthResource
    swagger_resources: resources.AsyncSwaggerResourcesResource
    with_raw_response: AsyncNgcWithRawResponse
    with_streaming_response: AsyncNgcWithStreamedResponse

    # client options
    auth_token: str

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async ngc client instance.

        This automatically infers the `auth_token` argument from the `NVCF_AUTH_TOKEN` environment variable if it is not provided.
        """
        if auth_token is None:
            auth_token = os.environ.get("NVCF_AUTH_TOKEN")
        if auth_token is None:
            raise NgcError(
                "The auth_token client option must be set either by passing auth_token to the client or by setting the NVCF_AUTH_TOKEN environment variable"
            )
        self.auth_token = auth_token

        if base_url is None:
            base_url = os.environ.get("NGC_BASE_URL")
        if base_url is None:
            base_url = f"https://api.ngc.nvidia.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.orgs = resources.AsyncOrgsResource(self)
        self.me = resources.AsyncMeResource(self)
        self.admin = resources.AsyncAdminResource(self)
        self.users_management = resources.AsyncUsersManagementResource(self)
        self.services = resources.AsyncServicesResource(self)
        self.roles = resources.AsyncRolesResource(self)
        self.public_keys = resources.AsyncPublicKeysResource(self)
        self.health = resources.AsyncHealthResource(self)
        self.swagger_resources = resources.AsyncSwaggerResourcesResource(self)
        self.with_raw_response = AsyncNgcWithRawResponse(self)
        self.with_streaming_response = AsyncNgcWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class NgcWithRawResponse:
    def __init__(self, client: Ngc) -> None:
        self.orgs = resources.OrgsResourceWithRawResponse(client.orgs)
        self.me = resources.MeResourceWithRawResponse(client.me)
        self.admin = resources.AdminResourceWithRawResponse(client.admin)
        self.users_management = resources.UsersManagementResourceWithRawResponse(client.users_management)
        self.services = resources.ServicesResourceWithRawResponse(client.services)
        self.roles = resources.RolesResourceWithRawResponse(client.roles)
        self.public_keys = resources.PublicKeysResourceWithRawResponse(client.public_keys)
        self.health = resources.HealthResourceWithRawResponse(client.health)
        self.swagger_resources = resources.SwaggerResourcesResourceWithRawResponse(client.swagger_resources)


class AsyncNgcWithRawResponse:
    def __init__(self, client: AsyncNgc) -> None:
        self.orgs = resources.AsyncOrgsResourceWithRawResponse(client.orgs)
        self.me = resources.AsyncMeResourceWithRawResponse(client.me)
        self.admin = resources.AsyncAdminResourceWithRawResponse(client.admin)
        self.users_management = resources.AsyncUsersManagementResourceWithRawResponse(client.users_management)
        self.services = resources.AsyncServicesResourceWithRawResponse(client.services)
        self.roles = resources.AsyncRolesResourceWithRawResponse(client.roles)
        self.public_keys = resources.AsyncPublicKeysResourceWithRawResponse(client.public_keys)
        self.health = resources.AsyncHealthResourceWithRawResponse(client.health)
        self.swagger_resources = resources.AsyncSwaggerResourcesResourceWithRawResponse(client.swagger_resources)


class NgcWithStreamedResponse:
    def __init__(self, client: Ngc) -> None:
        self.orgs = resources.OrgsResourceWithStreamingResponse(client.orgs)
        self.me = resources.MeResourceWithStreamingResponse(client.me)
        self.admin = resources.AdminResourceWithStreamingResponse(client.admin)
        self.users_management = resources.UsersManagementResourceWithStreamingResponse(client.users_management)
        self.services = resources.ServicesResourceWithStreamingResponse(client.services)
        self.roles = resources.RolesResourceWithStreamingResponse(client.roles)
        self.public_keys = resources.PublicKeysResourceWithStreamingResponse(client.public_keys)
        self.health = resources.HealthResourceWithStreamingResponse(client.health)
        self.swagger_resources = resources.SwaggerResourcesResourceWithStreamingResponse(client.swagger_resources)


class AsyncNgcWithStreamedResponse:
    def __init__(self, client: AsyncNgc) -> None:
        self.orgs = resources.AsyncOrgsResourceWithStreamingResponse(client.orgs)
        self.me = resources.AsyncMeResourceWithStreamingResponse(client.me)
        self.admin = resources.AsyncAdminResourceWithStreamingResponse(client.admin)
        self.users_management = resources.AsyncUsersManagementResourceWithStreamingResponse(client.users_management)
        self.services = resources.AsyncServicesResourceWithStreamingResponse(client.services)
        self.roles = resources.AsyncRolesResourceWithStreamingResponse(client.roles)
        self.public_keys = resources.AsyncPublicKeysResourceWithStreamingResponse(client.public_keys)
        self.health = resources.AsyncHealthResourceWithStreamingResponse(client.health)
        self.swagger_resources = resources.AsyncSwaggerResourcesResourceWithStreamingResponse(client.swagger_resources)


Client = Ngc

AsyncClient = AsyncNgc
