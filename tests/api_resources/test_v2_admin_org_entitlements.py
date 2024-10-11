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


class TestV2AdminOrgEntitlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/entitlements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_entitlement = client.v2_admin_org_entitlements.retrieve_all(
            org_name="org-name",
        )
        assert v2_admin_org_entitlement.is_closed
        assert v2_admin_org_entitlement.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_entitlement.is_closed) is True
        assert isinstance(v2_admin_org_entitlement, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_all_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/entitlements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_entitlement = client.v2_admin_org_entitlements.retrieve_all(
            org_name="org-name",
            is_paid_subscription=True,
            product_name="product-name",
        )
        assert v2_admin_org_entitlement.is_closed
        assert v2_admin_org_entitlement.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_entitlement.is_closed) is True
        assert isinstance(v2_admin_org_entitlement, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/entitlements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        v2_admin_org_entitlement = client.v2_admin_org_entitlements.with_raw_response.retrieve_all(
            org_name="org-name",
        )

        assert v2_admin_org_entitlement.is_closed is True
        assert v2_admin_org_entitlement.http_request.headers.get("X-Stainless-Lang") == "python"
        assert v2_admin_org_entitlement.json() == {"foo": "bar"}
        assert isinstance(v2_admin_org_entitlement, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/entitlements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.v2_admin_org_entitlements.with_streaming_response.retrieve_all(
            org_name="org-name",
        ) as v2_admin_org_entitlement:
            assert not v2_admin_org_entitlement.is_closed
            assert v2_admin_org_entitlement.http_request.headers.get("X-Stainless-Lang") == "python"

            assert v2_admin_org_entitlement.json() == {"foo": "bar"}
            assert cast(Any, v2_admin_org_entitlement.is_closed) is True
            assert isinstance(v2_admin_org_entitlement, StreamedBinaryAPIResponse)

        assert cast(Any, v2_admin_org_entitlement.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve_all(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.v2_admin_org_entitlements.with_raw_response.retrieve_all(
                org_name="",
            )


class TestAsyncV2AdminOrgEntitlements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/entitlements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_entitlement = await async_client.v2_admin_org_entitlements.retrieve_all(
            org_name="org-name",
        )
        assert v2_admin_org_entitlement.is_closed
        assert await v2_admin_org_entitlement.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_entitlement.is_closed) is True
        assert isinstance(v2_admin_org_entitlement, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_all_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/entitlements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_entitlement = await async_client.v2_admin_org_entitlements.retrieve_all(
            org_name="org-name",
            is_paid_subscription=True,
            product_name="product-name",
        )
        assert v2_admin_org_entitlement.is_closed
        assert await v2_admin_org_entitlement.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_entitlement.is_closed) is True
        assert isinstance(v2_admin_org_entitlement, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/entitlements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        v2_admin_org_entitlement = await async_client.v2_admin_org_entitlements.with_raw_response.retrieve_all(
            org_name="org-name",
        )

        assert v2_admin_org_entitlement.is_closed is True
        assert v2_admin_org_entitlement.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await v2_admin_org_entitlement.json() == {"foo": "bar"}
        assert isinstance(v2_admin_org_entitlement, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/entitlements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.v2_admin_org_entitlements.with_streaming_response.retrieve_all(
            org_name="org-name",
        ) as v2_admin_org_entitlement:
            assert not v2_admin_org_entitlement.is_closed
            assert v2_admin_org_entitlement.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await v2_admin_org_entitlement.json() == {"foo": "bar"}
            assert cast(Any, v2_admin_org_entitlement.is_closed) is True
            assert isinstance(v2_admin_org_entitlement, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, v2_admin_org_entitlement.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve_all(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.v2_admin_org_entitlements.with_raw_response.retrieve_all(
                org_name="",
            )
