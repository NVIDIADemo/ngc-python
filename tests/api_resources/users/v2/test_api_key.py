# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.users.v2 import UserKeyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ngc) -> None:
        api_key = client.users.v2.api_key.create()
        assert_matches_type(UserKeyResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ngc) -> None:
        response = client.users.v2.api_key.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(UserKeyResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ngc) -> None:
        with client.users.v2.api_key.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(UserKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIKey:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNgc) -> None:
        api_key = await async_client.users.v2.api_key.create()
        assert_matches_type(UserKeyResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNgc) -> None:
        response = await async_client.users.v2.api_key.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(UserKeyResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNgc) -> None:
        async with async_client.users.v2.api_key.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(UserKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True
