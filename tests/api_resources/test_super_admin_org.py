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


class TestSuperAdminOrg:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        super_admin_org = client.super_admin_org.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        )
        assert super_admin_org.is_closed
        assert super_admin_org.json() == {"foo": "bar"}
        assert cast(Any, super_admin_org.is_closed) is True
        assert isinstance(super_admin_org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        super_admin_org = client.super_admin_org.create(
            org_owner={
                "email": "email",
                "full_name": "x",
                "last_login_date": "lastLoginDate",
            },
            country="country",
            description="description",
            display_name="x",
            idp_id="idpId",
            is_internal=True,
            name="xx",
            pec_name="pecName",
            pec_sfdc_id="pecSfdcId",
            product_enablements=[
                {
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
                {
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
                {
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
            ],
            product_subscriptions=[
                {
                    "product_name": "productName",
                    "id": "id",
                    "ems_entitlement_type": "EMS_EVAL",
                    "expiration_date": "expirationDate",
                    "start_date": "startDate",
                    "type": "NGC_ADMIN_EVAL",
                },
                {
                    "product_name": "productName",
                    "id": "id",
                    "ems_entitlement_type": "EMS_EVAL",
                    "expiration_date": "expirationDate",
                    "start_date": "startDate",
                    "type": "NGC_ADMIN_EVAL",
                },
                {
                    "product_name": "productName",
                    "id": "id",
                    "ems_entitlement_type": "EMS_EVAL",
                    "expiration_date": "expirationDate",
                    "start_date": "startDate",
                    "type": "NGC_ADMIN_EVAL",
                },
            ],
            salesforce_account_industry="salesforceAccountIndustry",
            send_email=True,
            type="UNKNOWN",
        )
        assert super_admin_org.is_closed
        assert super_admin_org.json() == {"foo": "bar"}
        assert cast(Any, super_admin_org.is_closed) is True
        assert isinstance(super_admin_org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        super_admin_org = client.super_admin_org.with_raw_response.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        )

        assert super_admin_org.is_closed is True
        assert super_admin_org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert super_admin_org.json() == {"foo": "bar"}
        assert isinstance(super_admin_org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.super_admin_org.with_streaming_response.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        ) as super_admin_org:
            assert not super_admin_org.is_closed
            assert super_admin_org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert super_admin_org.json() == {"foo": "bar"}
            assert cast(Any, super_admin_org.is_closed) is True
            assert isinstance(super_admin_org, StreamedBinaryAPIResponse)

        assert cast(Any, super_admin_org.is_closed) is True


class TestAsyncSuperAdminOrg:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        super_admin_org = await async_client.super_admin_org.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        )
        assert super_admin_org.is_closed
        assert await super_admin_org.json() == {"foo": "bar"}
        assert cast(Any, super_admin_org.is_closed) is True
        assert isinstance(super_admin_org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        super_admin_org = await async_client.super_admin_org.create(
            org_owner={
                "email": "email",
                "full_name": "x",
                "last_login_date": "lastLoginDate",
            },
            country="country",
            description="description",
            display_name="x",
            idp_id="idpId",
            is_internal=True,
            name="xx",
            pec_name="pecName",
            pec_sfdc_id="pecSfdcId",
            product_enablements=[
                {
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
                {
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
                {
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
            ],
            product_subscriptions=[
                {
                    "product_name": "productName",
                    "id": "id",
                    "ems_entitlement_type": "EMS_EVAL",
                    "expiration_date": "expirationDate",
                    "start_date": "startDate",
                    "type": "NGC_ADMIN_EVAL",
                },
                {
                    "product_name": "productName",
                    "id": "id",
                    "ems_entitlement_type": "EMS_EVAL",
                    "expiration_date": "expirationDate",
                    "start_date": "startDate",
                    "type": "NGC_ADMIN_EVAL",
                },
                {
                    "product_name": "productName",
                    "id": "id",
                    "ems_entitlement_type": "EMS_EVAL",
                    "expiration_date": "expirationDate",
                    "start_date": "startDate",
                    "type": "NGC_ADMIN_EVAL",
                },
            ],
            salesforce_account_industry="salesforceAccountIndustry",
            send_email=True,
            type="UNKNOWN",
        )
        assert super_admin_org.is_closed
        assert await super_admin_org.json() == {"foo": "bar"}
        assert cast(Any, super_admin_org.is_closed) is True
        assert isinstance(super_admin_org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        super_admin_org = await async_client.super_admin_org.with_raw_response.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        )

        assert super_admin_org.is_closed is True
        assert super_admin_org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await super_admin_org.json() == {"foo": "bar"}
        assert isinstance(super_admin_org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.super_admin_org.with_streaming_response.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        ) as super_admin_org:
            assert not super_admin_org.is_closed
            assert super_admin_org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await super_admin_org.json() == {"foo": "bar"}
            assert cast(Any, super_admin_org.is_closed) is True
            assert isinstance(super_admin_org, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, super_admin_org.is_closed) is True
