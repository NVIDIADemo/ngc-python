# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from ngc.types import UserRoleDefinitions
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_all(self, client: Ngc) -> None:
        role = client.roles.retrieve_all()
        assert_matches_type(UserRoleDefinitions, role, path=["response"])

    @parametrize
    def test_method_retrieve_all_with_all_params(self, client: Ngc) -> None:
        role = client.roles.retrieve_all(
            show_hidden=True,
        )
        assert_matches_type(UserRoleDefinitions, role, path=["response"])

    @parametrize
    def test_raw_response_retrieve_all(self, client: Ngc) -> None:
        response = client.roles.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(UserRoleDefinitions, role, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_all(self, client: Ngc) -> None:
        with client.roles.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(UserRoleDefinitions, role, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncNgc) -> None:
        role = await async_client.roles.retrieve_all()
        assert_matches_type(UserRoleDefinitions, role, path=["response"])

    @parametrize
    async def test_method_retrieve_all_with_all_params(self, async_client: AsyncNgc) -> None:
        role = await async_client.roles.retrieve_all(
            show_hidden=True,
        )
        assert_matches_type(UserRoleDefinitions, role, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncNgc) -> None:
        response = await async_client.roles.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(UserRoleDefinitions, role, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNgc) -> None:
        async with async_client.roles.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(UserRoleDefinitions, role, path=["response"])

        assert cast(Any, response.is_closed) is True
