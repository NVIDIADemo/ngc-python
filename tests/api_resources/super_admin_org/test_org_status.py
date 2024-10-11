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


class TestOrgStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org_status = client.super_admin_org.org_status.create(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        )
        assert org_status.is_closed
        assert org_status.json() == {"foo": "bar"}
        assert cast(Any, org_status.is_closed) is True
        assert isinstance(org_status, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org_status = client.super_admin_org.org_status.create(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
                "expiration_date": "expirationDate",
                "po_details": [
                    {
                        "entitlement_id": "entitlementId",
                        "pk_id": "pkId",
                    },
                    {
                        "entitlement_id": "entitlementId",
                        "pk_id": "pkId",
                    },
                    {
                        "entitlement_id": "entitlementId",
                        "pk_id": "pkId",
                    },
                ],
            },
        )
        assert org_status.is_closed
        assert org_status.json() == {"foo": "bar"}
        assert cast(Any, org_status.is_closed) is True
        assert isinstance(org_status, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org_status = client.super_admin_org.org_status.with_raw_response.create(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        )

        assert org_status.is_closed is True
        assert org_status.http_request.headers.get("X-Stainless-Lang") == "python"
        assert org_status.json() == {"foo": "bar"}
        assert isinstance(org_status, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.super_admin_org.org_status.with_streaming_response.create(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        ) as org_status:
            assert not org_status.is_closed
            assert org_status.http_request.headers.get("X-Stainless-Lang") == "python"

            assert org_status.json() == {"foo": "bar"}
            assert cast(Any, org_status.is_closed) is True
            assert isinstance(org_status, StreamedBinaryAPIResponse)

        assert cast(Any, org_status.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.super_admin_org.org_status.with_raw_response.create(
                org_name="",
                create_subscription=True,
                product_enablement={
                    "product_name": "productName",
                    "type": "NGC_ADMIN_EVAL",
                },
            )


class TestAsyncOrgStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org_status = await async_client.super_admin_org.org_status.create(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        )
        assert org_status.is_closed
        assert await org_status.json() == {"foo": "bar"}
        assert cast(Any, org_status.is_closed) is True
        assert isinstance(org_status, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org_status = await async_client.super_admin_org.org_status.create(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
                "expiration_date": "expirationDate",
                "po_details": [
                    {
                        "entitlement_id": "entitlementId",
                        "pk_id": "pkId",
                    },
                    {
                        "entitlement_id": "entitlementId",
                        "pk_id": "pkId",
                    },
                    {
                        "entitlement_id": "entitlementId",
                        "pk_id": "pkId",
                    },
                ],
            },
        )
        assert org_status.is_closed
        assert await org_status.json() == {"foo": "bar"}
        assert cast(Any, org_status.is_closed) is True
        assert isinstance(org_status, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org_status = await async_client.super_admin_org.org_status.with_raw_response.create(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        )

        assert org_status.is_closed is True
        assert org_status.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await org_status.json() == {"foo": "bar"}
        assert isinstance(org_status, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.super_admin_org.org_status.with_streaming_response.create(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        ) as org_status:
            assert not org_status.is_closed
            assert org_status.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await org_status.json() == {"foo": "bar"}
            assert cast(Any, org_status.is_closed) is True
            assert isinstance(org_status, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, org_status.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.super_admin_org.org_status.with_raw_response.create(
                org_name="",
                create_subscription=True,
                product_enablement={
                    "product_name": "productName",
                    "type": "NGC_ADMIN_EVAL",
                },
            )
