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


class TestSuperAdminOrgControllers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_backfill_orgs_to_kratos(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        super_admin_org_controller = client.super_admin_org_controllers.backfill_orgs_to_kratos()
        assert super_admin_org_controller.is_closed
        assert super_admin_org_controller.json() == {"foo": "bar"}
        assert cast(Any, super_admin_org_controller.is_closed) is True
        assert isinstance(super_admin_org_controller, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_backfill_orgs_to_kratos(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        super_admin_org_controller = client.super_admin_org_controllers.with_raw_response.backfill_orgs_to_kratos()

        assert super_admin_org_controller.is_closed is True
        assert super_admin_org_controller.http_request.headers.get("X-Stainless-Lang") == "python"
        assert super_admin_org_controller.json() == {"foo": "bar"}
        assert isinstance(super_admin_org_controller, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_backfill_orgs_to_kratos(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.super_admin_org_controllers.with_streaming_response.backfill_orgs_to_kratos() as super_admin_org_controller:
            assert not super_admin_org_controller.is_closed
            assert super_admin_org_controller.http_request.headers.get("X-Stainless-Lang") == "python"

            assert super_admin_org_controller.json() == {"foo": "bar"}
            assert cast(Any, super_admin_org_controller.is_closed) is True
            assert isinstance(super_admin_org_controller, StreamedBinaryAPIResponse)

        assert cast(Any, super_admin_org_controller.is_closed) is True


class TestAsyncSuperAdminOrgControllers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_backfill_orgs_to_kratos(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        super_admin_org_controller = await async_client.super_admin_org_controllers.backfill_orgs_to_kratos()
        assert super_admin_org_controller.is_closed
        assert await super_admin_org_controller.json() == {"foo": "bar"}
        assert cast(Any, super_admin_org_controller.is_closed) is True
        assert isinstance(super_admin_org_controller, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_backfill_orgs_to_kratos(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        super_admin_org_controller = (
            await async_client.super_admin_org_controllers.with_raw_response.backfill_orgs_to_kratos()
        )

        assert super_admin_org_controller.is_closed is True
        assert super_admin_org_controller.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await super_admin_org_controller.json() == {"foo": "bar"}
        assert isinstance(super_admin_org_controller, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_backfill_orgs_to_kratos(
        self, async_client: AsyncNgc, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.super_admin_org_controllers.with_streaming_response.backfill_orgs_to_kratos() as super_admin_org_controller:
            assert not super_admin_org_controller.is_closed
            assert super_admin_org_controller.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await super_admin_org_controller.json() == {"foo": "bar"}
            assert cast(Any, super_admin_org_controller.is_closed) is True
            assert isinstance(super_admin_org_controller, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, super_admin_org_controller.is_closed) is True
