# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.me import api_key_update_params, api_key_retrieve_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.user import User
from ...types.me.user_key_response import UserKeyResponse

__all__ = ["APIKeyResource", "AsyncAPIKeyResource"]


class APIKeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return APIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return APIKeyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        org_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        What am I?

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/users/me",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"org_name": org_name}, api_key_retrieve_params.APIKeyRetrieveParams),
            ),
            cast_to=User,
        )

    def update(
        self,
        *,
        has_email_opt_in: bool | NotGiven = NOT_GIVEN,
        has_signed_ai_foundry_partnerships_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_base_command_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_base_command_manager_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_bio_ne_mo_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_container_publishing_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_cu_opt_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_earth2_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_egx_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_fleet_command_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_llm_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_nvaieeula: bool | NotGiven = NOT_GIVEN,
        has_signed_nvidia_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_nvqceula: bool | NotGiven = NOT_GIVEN,
        has_signed_omniverse_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_privacy_policy: bool | NotGiven = NOT_GIVEN,
        has_signed_third_party_registry_share_eula: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        user_metadata: api_key_update_params.UserMetadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Edit current user profile

        Args:
          has_email_opt_in: indicates if user has opt in to nvidia emails

          has_signed_ai_foundry_partnerships_eula: indicates if user has accepted AI Foundry Partnerships End User License
              Agreement.

          has_signed_base_command_eula: indicates if user has accepted Base Command EULA

          has_signed_base_command_manager_eula: indicates if user has accepted Base Command Manager End User License Agreement.

          has_signed_bio_ne_mo_eula: indicates if user has accepted BioNeMo End User License Agreement.

          has_signed_container_publishing_eula: indicates if user has accepted container publishing eula

          has_signed_cu_opt_eula: indicates if user has accepted CuOpt End User License Agreement.

          has_signed_earth2_eula: indicates if user has accepted Earth-2 End User License Agreement.

          has_signed_egx_eula: indicates if user has accepted EGX EULA

          has_signed_eula: indicates if user has accepted NGC EULA

          has_signed_fleet_command_eula: indicates if user has accepted Fleet Command End User License Agreement.

          has_signed_llm_eula: indicates if user has accepted LLM End User License Agreement.

          has_signed_nvaieeula: indicates if user has accepted Fleet Command End User License Agreement.

          has_signed_nvidia_eula: indicates if user has accepted NVIDIA EULA

          has_signed_nvqceula: indicates if user has accepted Nvidia Quantum Cloud End User License Agreement.

          has_signed_omniverse_eula: indicates if user has accepted Omniverse End User License Agreement.

          has_signed_privacy_policy: indicates if the user has signed the Privacy Policy

          has_signed_third_party_registry_share_eula: indicates if user has consented to share their registration info with other
              parties

          name: user name

          user_metadata: Metadata information about the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v2/users/me",
            body=maybe_transform(
                {
                    "has_email_opt_in": has_email_opt_in,
                    "has_signed_ai_foundry_partnerships_eula": has_signed_ai_foundry_partnerships_eula,
                    "has_signed_base_command_eula": has_signed_base_command_eula,
                    "has_signed_base_command_manager_eula": has_signed_base_command_manager_eula,
                    "has_signed_bio_ne_mo_eula": has_signed_bio_ne_mo_eula,
                    "has_signed_container_publishing_eula": has_signed_container_publishing_eula,
                    "has_signed_cu_opt_eula": has_signed_cu_opt_eula,
                    "has_signed_earth2_eula": has_signed_earth2_eula,
                    "has_signed_egx_eula": has_signed_egx_eula,
                    "has_signed_eula": has_signed_eula,
                    "has_signed_fleet_command_eula": has_signed_fleet_command_eula,
                    "has_signed_llm_eula": has_signed_llm_eula,
                    "has_signed_nvaieeula": has_signed_nvaieeula,
                    "has_signed_nvidia_eula": has_signed_nvidia_eula,
                    "has_signed_nvqceula": has_signed_nvqceula,
                    "has_signed_omniverse_eula": has_signed_omniverse_eula,
                    "has_signed_privacy_policy": has_signed_privacy_policy,
                    "has_signed_third_party_registry_share_eula": has_signed_third_party_registry_share_eula,
                    "name": name,
                    "user_metadata": user_metadata,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def create_api_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserKeyResponse:
        """Generate API Key"""
        return self._post(
            "/v2/users/me/api-key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserKeyResponse,
        )


class AsyncAPIKeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NVIDIADemo/ngc-python#with_streaming_response
        """
        return AsyncAPIKeyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        org_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        What am I?

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/users/me",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"org_name": org_name}, api_key_retrieve_params.APIKeyRetrieveParams),
            ),
            cast_to=User,
        )

    async def update(
        self,
        *,
        has_email_opt_in: bool | NotGiven = NOT_GIVEN,
        has_signed_ai_foundry_partnerships_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_base_command_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_base_command_manager_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_bio_ne_mo_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_container_publishing_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_cu_opt_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_earth2_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_egx_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_fleet_command_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_llm_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_nvaieeula: bool | NotGiven = NOT_GIVEN,
        has_signed_nvidia_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_nvqceula: bool | NotGiven = NOT_GIVEN,
        has_signed_omniverse_eula: bool | NotGiven = NOT_GIVEN,
        has_signed_privacy_policy: bool | NotGiven = NOT_GIVEN,
        has_signed_third_party_registry_share_eula: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        user_metadata: api_key_update_params.UserMetadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Edit current user profile

        Args:
          has_email_opt_in: indicates if user has opt in to nvidia emails

          has_signed_ai_foundry_partnerships_eula: indicates if user has accepted AI Foundry Partnerships End User License
              Agreement.

          has_signed_base_command_eula: indicates if user has accepted Base Command EULA

          has_signed_base_command_manager_eula: indicates if user has accepted Base Command Manager End User License Agreement.

          has_signed_bio_ne_mo_eula: indicates if user has accepted BioNeMo End User License Agreement.

          has_signed_container_publishing_eula: indicates if user has accepted container publishing eula

          has_signed_cu_opt_eula: indicates if user has accepted CuOpt End User License Agreement.

          has_signed_earth2_eula: indicates if user has accepted Earth-2 End User License Agreement.

          has_signed_egx_eula: indicates if user has accepted EGX EULA

          has_signed_eula: indicates if user has accepted NGC EULA

          has_signed_fleet_command_eula: indicates if user has accepted Fleet Command End User License Agreement.

          has_signed_llm_eula: indicates if user has accepted LLM End User License Agreement.

          has_signed_nvaieeula: indicates if user has accepted Fleet Command End User License Agreement.

          has_signed_nvidia_eula: indicates if user has accepted NVIDIA EULA

          has_signed_nvqceula: indicates if user has accepted Nvidia Quantum Cloud End User License Agreement.

          has_signed_omniverse_eula: indicates if user has accepted Omniverse End User License Agreement.

          has_signed_privacy_policy: indicates if the user has signed the Privacy Policy

          has_signed_third_party_registry_share_eula: indicates if user has consented to share their registration info with other
              parties

          name: user name

          user_metadata: Metadata information about the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v2/users/me",
            body=await async_maybe_transform(
                {
                    "has_email_opt_in": has_email_opt_in,
                    "has_signed_ai_foundry_partnerships_eula": has_signed_ai_foundry_partnerships_eula,
                    "has_signed_base_command_eula": has_signed_base_command_eula,
                    "has_signed_base_command_manager_eula": has_signed_base_command_manager_eula,
                    "has_signed_bio_ne_mo_eula": has_signed_bio_ne_mo_eula,
                    "has_signed_container_publishing_eula": has_signed_container_publishing_eula,
                    "has_signed_cu_opt_eula": has_signed_cu_opt_eula,
                    "has_signed_earth2_eula": has_signed_earth2_eula,
                    "has_signed_egx_eula": has_signed_egx_eula,
                    "has_signed_eula": has_signed_eula,
                    "has_signed_fleet_command_eula": has_signed_fleet_command_eula,
                    "has_signed_llm_eula": has_signed_llm_eula,
                    "has_signed_nvaieeula": has_signed_nvaieeula,
                    "has_signed_nvidia_eula": has_signed_nvidia_eula,
                    "has_signed_nvqceula": has_signed_nvqceula,
                    "has_signed_omniverse_eula": has_signed_omniverse_eula,
                    "has_signed_privacy_policy": has_signed_privacy_policy,
                    "has_signed_third_party_registry_share_eula": has_signed_third_party_registry_share_eula,
                    "name": name,
                    "user_metadata": user_metadata,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def create_api_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserKeyResponse:
        """Generate API Key"""
        return await self._post(
            "/v2/users/me/api-key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserKeyResponse,
        )


class APIKeyResourceWithRawResponse:
    def __init__(self, api_key: APIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = to_raw_response_wrapper(
            api_key.retrieve,
        )
        self.update = to_raw_response_wrapper(
            api_key.update,
        )
        self.create_api_key = to_raw_response_wrapper(
            api_key.create_api_key,
        )


class AsyncAPIKeyResourceWithRawResponse:
    def __init__(self, api_key: AsyncAPIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = async_to_raw_response_wrapper(
            api_key.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            api_key.update,
        )
        self.create_api_key = async_to_raw_response_wrapper(
            api_key.create_api_key,
        )


class APIKeyResourceWithStreamingResponse:
    def __init__(self, api_key: APIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = to_streamed_response_wrapper(
            api_key.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            api_key.update,
        )
        self.create_api_key = to_streamed_response_wrapper(
            api_key.create_api_key,
        )


class AsyncAPIKeyResourceWithStreamingResponse:
    def __init__(self, api_key: AsyncAPIKeyResource) -> None:
        self._api_key = api_key

        self.retrieve = async_to_streamed_response_wrapper(
            api_key.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            api_key.update,
        )
        self.create_api_key = async_to_streamed_response_wrapper(
            api_key.create_api_key,
        )
