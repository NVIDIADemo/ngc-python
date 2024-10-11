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


class TestOrg:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.super_admin_org_controllers.org.retrieve(
            "org-name",
        )
        assert org.is_closed
        assert org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = client.super_admin_org_controllers.org.with_raw_response.retrieve(
            "org-name",
        )

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert org.json() == {"foo": "bar"}
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.super_admin_org_controllers.org.with_streaming_response.retrieve(
            "org-name",
        ) as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, StreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.super_admin_org_controllers.org.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.super_admin_org_controllers.org.update(
            org_name="org-name",
        )
        assert org.is_closed
        assert org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.super_admin_org_controllers.org.update(
            org_name="org-name",
            alternate_contact={
                "email": "xxxxxx",
                "full_name": "fullName",
            },
            company_name="companyName",
            description="description",
            display_name="x",
            idp_id="idpId",
            infinity_manager_settings={
                "infinity_manager_enabled": True,
                "infinity_manager_enable_team_override": True,
            },
            is_dataset_service_enabled=True,
            is_internal=True,
            is_quick_start_enabled=True,
            is_registry_sse_enabled=True,
            is_secrets_manager_service_enabled=True,
            is_secure_credential_sharing_service_enabled=True,
            is_separate_influx_db_used=True,
            org_owner={
                "email": "email",
                "full_name": "x",
                "last_login_date": "lastLoginDate",
            },
            org_owners=[
                {
                    "email": "email",
                    "full_name": "x",
                    "last_login_date": "lastLoginDate",
                },
                {
                    "email": "email",
                    "full_name": "x",
                    "last_login_date": "lastLoginDate",
                },
                {
                    "email": "email",
                    "full_name": "x",
                    "last_login_date": "lastLoginDate",
                },
            ],
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
            repo_scan_settings={
                "repo_scan_allow_override": True,
                "repo_scan_by_default": True,
                "repo_scan_enabled": True,
                "repo_scan_enable_notifications": True,
                "repo_scan_enable_team_override": True,
                "repo_scan_show_results": True,
            },
            type="UNKNOWN",
        )
        assert org.is_closed
        assert org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = client.super_admin_org_controllers.org.with_raw_response.update(
            org_name="org-name",
        )

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert org.json() == {"foo": "bar"}
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.super_admin_org_controllers.org.with_streaming_response.update(
            org_name="org-name",
        ) as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, StreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.super_admin_org_controllers.org.with_raw_response.update(
                org_name="",
            )


class TestAsyncOrg:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.super_admin_org_controllers.org.retrieve(
            "org-name",
        )
        assert org.is_closed
        assert await org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = await async_client.super_admin_org_controllers.org.with_raw_response.retrieve(
            "org-name",
        )

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await org.json() == {"foo": "bar"}
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.super_admin_org_controllers.org.with_streaming_response.retrieve(
            "org-name",
        ) as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.super_admin_org_controllers.org.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.super_admin_org_controllers.org.update(
            org_name="org-name",
        )
        assert org.is_closed
        assert await org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.super_admin_org_controllers.org.update(
            org_name="org-name",
            alternate_contact={
                "email": "xxxxxx",
                "full_name": "fullName",
            },
            company_name="companyName",
            description="description",
            display_name="x",
            idp_id="idpId",
            infinity_manager_settings={
                "infinity_manager_enabled": True,
                "infinity_manager_enable_team_override": True,
            },
            is_dataset_service_enabled=True,
            is_internal=True,
            is_quick_start_enabled=True,
            is_registry_sse_enabled=True,
            is_secrets_manager_service_enabled=True,
            is_secure_credential_sharing_service_enabled=True,
            is_separate_influx_db_used=True,
            org_owner={
                "email": "email",
                "full_name": "x",
                "last_login_date": "lastLoginDate",
            },
            org_owners=[
                {
                    "email": "email",
                    "full_name": "x",
                    "last_login_date": "lastLoginDate",
                },
                {
                    "email": "email",
                    "full_name": "x",
                    "last_login_date": "lastLoginDate",
                },
                {
                    "email": "email",
                    "full_name": "x",
                    "last_login_date": "lastLoginDate",
                },
            ],
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
            repo_scan_settings={
                "repo_scan_allow_override": True,
                "repo_scan_by_default": True,
                "repo_scan_enabled": True,
                "repo_scan_enable_notifications": True,
                "repo_scan_enable_team_override": True,
                "repo_scan_show_results": True,
            },
            type="UNKNOWN",
        )
        assert org.is_closed
        assert await org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = await async_client.super_admin_org_controllers.org.with_raw_response.update(
            org_name="org-name",
        )

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await org.json() == {"foo": "bar"}
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.super_admin_org_controllers.org.with_streaming_response.update(
            org_name="org-name",
        ) as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.super_admin_org_controllers.org.with_raw_response.update(
                org_name="",
            )
