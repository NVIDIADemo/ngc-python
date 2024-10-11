# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.me import UserKeyResponse
from ngc.types.shared import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Ngc) -> None:
        api_key = client.me.api_key.retrieve()
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Ngc) -> None:
        api_key = client.me.api_key.retrieve(
            org_name="org-name",
        )
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ngc) -> None:
        response = client.me.api_key.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ngc) -> None:
        with client.me.api_key.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(User, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Ngc) -> None:
        api_key = client.me.api_key.update()
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Ngc) -> None:
        api_key = client.me.api_key.update(
            has_email_opt_in=True,
            has_signed_ai_foundry_partnerships_eula=True,
            has_signed_base_command_eula=True,
            has_signed_base_command_manager_eula=True,
            has_signed_bio_ne_mo_eula=True,
            has_signed_container_publishing_eula=True,
            has_signed_cu_opt_eula=True,
            has_signed_earth2_eula=True,
            has_signed_egx_eula=True,
            has_signed_eula=True,
            has_signed_fleet_command_eula=True,
            has_signed_llm_eula=True,
            has_signed_nvaieeula=True,
            has_signed_nvidia_eula=True,
            has_signed_nvqceula=True,
            has_signed_omniverse_eula=True,
            has_signed_privacy_policy=True,
            has_signed_third_party_registry_share_eula=True,
            name="x",
            user_metadata={
                "company": "company",
                "company_url": "companyUrl",
                "country": "country",
                "first_name": "firstName",
                "industry": "industry",
                "interest": ["string", "string", "string"],
                "last_name": "lastName",
                "role": "role",
            },
        )
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Ngc) -> None:
        response = client.me.api_key.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Ngc) -> None:
        with client.me.api_key.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(User, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_api_key(self, client: Ngc) -> None:
        api_key = client.me.api_key.create_api_key()
        assert_matches_type(UserKeyResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_create_api_key(self, client: Ngc) -> None:
        response = client.me.api_key.with_raw_response.create_api_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(UserKeyResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_create_api_key(self, client: Ngc) -> None:
        with client.me.api_key.with_streaming_response.create_api_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(UserKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIKey:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNgc) -> None:
        api_key = await async_client.me.api_key.retrieve()
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncNgc) -> None:
        api_key = await async_client.me.api_key.retrieve(
            org_name="org-name",
        )
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNgc) -> None:
        response = await async_client.me.api_key.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNgc) -> None:
        async with async_client.me.api_key.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(User, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncNgc) -> None:
        api_key = await async_client.me.api_key.update()
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNgc) -> None:
        api_key = await async_client.me.api_key.update(
            has_email_opt_in=True,
            has_signed_ai_foundry_partnerships_eula=True,
            has_signed_base_command_eula=True,
            has_signed_base_command_manager_eula=True,
            has_signed_bio_ne_mo_eula=True,
            has_signed_container_publishing_eula=True,
            has_signed_cu_opt_eula=True,
            has_signed_earth2_eula=True,
            has_signed_egx_eula=True,
            has_signed_eula=True,
            has_signed_fleet_command_eula=True,
            has_signed_llm_eula=True,
            has_signed_nvaieeula=True,
            has_signed_nvidia_eula=True,
            has_signed_nvqceula=True,
            has_signed_omniverse_eula=True,
            has_signed_privacy_policy=True,
            has_signed_third_party_registry_share_eula=True,
            name="x",
            user_metadata={
                "company": "company",
                "company_url": "companyUrl",
                "country": "country",
                "first_name": "firstName",
                "industry": "industry",
                "interest": ["string", "string", "string"],
                "last_name": "lastName",
                "role": "role",
            },
        )
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNgc) -> None:
        response = await async_client.me.api_key.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(User, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNgc) -> None:
        async with async_client.me.api_key.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(User, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_api_key(self, async_client: AsyncNgc) -> None:
        api_key = await async_client.me.api_key.create_api_key()
        assert_matches_type(UserKeyResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_create_api_key(self, async_client: AsyncNgc) -> None:
        response = await async_client.me.api_key.with_raw_response.create_api_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(UserKeyResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_create_api_key(self, async_client: AsyncNgc) -> None:
        async with async_client.me.api_key.with_streaming_response.create_api_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(UserKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True
