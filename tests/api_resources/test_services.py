# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from ngc.types import ServiceVersionResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_version(self, client: Ngc) -> None:
        service = client.services.version()
        assert_matches_type(ServiceVersionResponse, service, path=["response"])

    @parametrize
    def test_method_version_with_all_params(self, client: Ngc) -> None:
        service = client.services.version(
            package="package",
            repo="repo",
        )
        assert_matches_type(ServiceVersionResponse, service, path=["response"])

    @parametrize
    def test_raw_response_version(self, client: Ngc) -> None:
        response = client.services.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceVersionResponse, service, path=["response"])

    @parametrize
    def test_streaming_response_version(self, client: Ngc) -> None:
        with client.services.with_streaming_response.version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceVersionResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_version(self, async_client: AsyncNgc) -> None:
        service = await async_client.services.version()
        assert_matches_type(ServiceVersionResponse, service, path=["response"])

    @parametrize
    async def test_method_version_with_all_params(self, async_client: AsyncNgc) -> None:
        service = await async_client.services.version(
            package="package",
            repo="repo",
        )
        assert_matches_type(ServiceVersionResponse, service, path=["response"])

    @parametrize
    async def test_raw_response_version(self, async_client: AsyncNgc) -> None:
        response = await async_client.services.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceVersionResponse, service, path=["response"])

    @parametrize
    async def test_streaming_response_version(self, async_client: AsyncNgc) -> None:
        async with async_client.services.with_streaming_response.version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceVersionResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True
