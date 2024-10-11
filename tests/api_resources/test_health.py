# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.shared import Health

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_all(self, client: Ngc) -> None:
        health = client.health.retrieve_all()
        assert_matches_type(Health, health, path=["response"])

    @parametrize
    def test_raw_response_retrieve_all(self, client: Ngc) -> None:
        response = client.health.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert_matches_type(Health, health, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_all(self, client: Ngc) -> None:
        with client.health.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert_matches_type(Health, health, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHealth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncNgc) -> None:
        health = await async_client.health.retrieve_all()
        assert_matches_type(Health, health, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncNgc) -> None:
        response = await async_client.health.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert_matches_type(Health, health, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNgc) -> None:
        async with async_client.health.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert_matches_type(Health, health, path=["response"])

        assert cast(Any, response.is_closed) is True
