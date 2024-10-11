# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from ngc import Ngc, AsyncNgc
from ngc._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/entitlements").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        entitlement = client.admin.entitlements.retrieve_all()
        assert entitlement.is_closed
        assert entitlement.json() == {"foo": "bar"}
        assert cast(Any, entitlement.is_closed) is True
        assert isinstance(entitlement, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_all_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/entitlements").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        entitlement = client.admin.entitlements.retrieve_all(
            is_paid_subscription=True,
            product_name="product-name",
        )
        assert entitlement.is_closed
        assert entitlement.json() == {"foo": "bar"}
        assert cast(Any, entitlement.is_closed) is True
        assert isinstance(entitlement, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/entitlements").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        entitlement = client.admin.entitlements.with_raw_response.retrieve_all()

        assert entitlement.is_closed is True
        assert entitlement.http_request.headers.get("X-Stainless-Lang") == "python"
        assert entitlement.json() == {"foo": "bar"}
        assert isinstance(entitlement, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/entitlements").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.admin.entitlements.with_streaming_response.retrieve_all() as entitlement:
            assert not entitlement.is_closed
            assert entitlement.http_request.headers.get("X-Stainless-Lang") == "python"

            assert entitlement.json() == {"foo": "bar"}
            assert cast(Any, entitlement.is_closed) is True
            assert isinstance(entitlement, StreamedBinaryAPIResponse)

        assert cast(Any, entitlement.is_closed) is True


class TestAsyncEntitlements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/entitlements").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        entitlement = await async_client.admin.entitlements.retrieve_all()
        assert entitlement.is_closed
        assert await entitlement.json() == {"foo": "bar"}
        assert cast(Any, entitlement.is_closed) is True
        assert isinstance(entitlement, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_all_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/entitlements").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        entitlement = await async_client.admin.entitlements.retrieve_all(
            is_paid_subscription=True,
            product_name="product-name",
        )
        assert entitlement.is_closed
        assert await entitlement.json() == {"foo": "bar"}
        assert cast(Any, entitlement.is_closed) is True
        assert isinstance(entitlement, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/entitlements").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        entitlement = await async_client.admin.entitlements.with_raw_response.retrieve_all()

        assert entitlement.is_closed is True
        assert entitlement.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await entitlement.json() == {"foo": "bar"}
        assert isinstance(entitlement, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/entitlements").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.admin.entitlements.with_streaming_response.retrieve_all() as entitlement:
            assert not entitlement.is_closed
            assert entitlement.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await entitlement.json() == {"foo": "bar"}
            assert cast(Any, entitlement.is_closed) is True
            assert isinstance(entitlement, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, entitlement.is_closed) is True
