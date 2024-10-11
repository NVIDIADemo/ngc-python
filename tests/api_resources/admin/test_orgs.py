# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from ngc.types.admin import (
    OrgValidateResponse,
    OrgOrgOwnerBackfillResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrgs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.admin.orgs.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        )
        assert org.is_closed
        assert org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.admin.orgs.create(
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
        assert org.is_closed
        assert org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = client.admin.orgs.with_raw_response.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        )

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert org.json() == {"foo": "bar"}
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.admin.orgs.with_streaming_response.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        ) as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, StreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.admin.orgs.retrieve(
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

        org = client.admin.orgs.with_raw_response.retrieve(
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
        with client.admin.orgs.with_streaming_response.retrieve(
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
            client.admin.orgs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.admin.orgs.update(
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
        org = client.admin.orgs.update(
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

        org = client.admin.orgs.with_raw_response.update(
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
        with client.admin.orgs.with_streaming_response.update(
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
            client.admin.orgs.with_raw_response.update(
                org_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_backfill_orgs_to_kratos(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.admin.orgs.backfill_orgs_to_kratos()
        assert org.is_closed
        assert org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_backfill_orgs_to_kratos(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = client.admin.orgs.with_raw_response.backfill_orgs_to_kratos()

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert org.json() == {"foo": "bar"}
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_backfill_orgs_to_kratos(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.admin.orgs.with_streaming_response.backfill_orgs_to_kratos() as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, StreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_enable(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.admin.orgs.enable(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        )
        assert org.is_closed
        assert org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_enable_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = client.admin.orgs.enable(
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
        assert org.is_closed
        assert org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_enable(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = client.admin.orgs.with_raw_response.enable(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        )

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert org.json() == {"foo": "bar"}
        assert isinstance(org, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_enable(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.admin.orgs.with_streaming_response.enable(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        ) as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, StreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_enable(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.admin.orgs.with_raw_response.enable(
                org_name="",
                create_subscription=True,
                product_enablement={
                    "product_name": "productName",
                    "type": "NGC_ADMIN_EVAL",
                },
            )

    @parametrize
    def test_method_org_owner_backfill(self, client: Ngc) -> None:
        org = client.admin.orgs.org_owner_backfill(
            "org-name",
        )
        assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

    @parametrize
    def test_raw_response_org_owner_backfill(self, client: Ngc) -> None:
        response = client.admin.orgs.with_raw_response.org_owner_backfill(
            "org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

    @parametrize
    def test_streaming_response_org_owner_backfill(self, client: Ngc) -> None:
        with client.admin.orgs.with_streaming_response.org_owner_backfill(
            "org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_org_owner_backfill(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.admin.orgs.with_raw_response.org_owner_backfill(
                "",
            )

    @parametrize
    def test_method_validate(self, client: Ngc) -> None:
        org = client.admin.orgs.validate(
            invitation_token="invitation_token",
        )
        assert_matches_type(OrgValidateResponse, org, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Ngc) -> None:
        response = client.admin.orgs.with_raw_response.validate(
            invitation_token="invitation_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgValidateResponse, org, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Ngc) -> None:
        with client.admin.orgs.with_streaming_response.validate(
            invitation_token="invitation_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgValidateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrgs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.admin.orgs.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        )
        assert org.is_closed
        assert await org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.admin.orgs.create(
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
        assert org.is_closed
        assert await org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = await async_client.admin.orgs.with_raw_response.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        )

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await org.json() == {"foo": "bar"}
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/orgs").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.admin.orgs.with_streaming_response.create(
            org_owner={
                "email": "email",
                "full_name": "x",
            },
        ) as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.admin.orgs.retrieve(
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

        org = await async_client.admin.orgs.with_raw_response.retrieve(
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
        async with async_client.admin.orgs.with_streaming_response.retrieve(
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
            await async_client.admin.orgs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v3/admin/org/org-name").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.admin.orgs.update(
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
        org = await async_client.admin.orgs.update(
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

        org = await async_client.admin.orgs.with_raw_response.update(
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
        async with async_client.admin.orgs.with_streaming_response.update(
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
            await async_client.admin.orgs.with_raw_response.update(
                org_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_backfill_orgs_to_kratos(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.admin.orgs.backfill_orgs_to_kratos()
        assert org.is_closed
        assert await org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_backfill_orgs_to_kratos(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = await async_client.admin.orgs.with_raw_response.backfill_orgs_to_kratos()

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await org.json() == {"foo": "bar"}
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_backfill_orgs_to_kratos(
        self, async_client: AsyncNgc, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/v2/admin/backfill-orgs-to-kratos").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.admin.orgs.with_streaming_response.backfill_orgs_to_kratos() as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_enable(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.admin.orgs.enable(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        )
        assert org.is_closed
        assert await org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_enable_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        org = await async_client.admin.orgs.enable(
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
        assert org.is_closed
        assert await org.json() == {"foo": "bar"}
        assert cast(Any, org.is_closed) is True
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_enable(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        org = await async_client.admin.orgs.with_raw_response.enable(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        )

        assert org.is_closed is True
        assert org.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await org.json() == {"foo": "bar"}
        assert isinstance(org, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_enable(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/v2/admin/org/org-name/enablement").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.admin.orgs.with_streaming_response.enable(
            org_name="org-name",
            create_subscription=True,
            product_enablement={
                "product_name": "productName",
                "type": "NGC_ADMIN_EVAL",
            },
        ) as org:
            assert not org.is_closed
            assert org.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await org.json() == {"foo": "bar"}
            assert cast(Any, org.is_closed) is True
            assert isinstance(org, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, org.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_enable(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.admin.orgs.with_raw_response.enable(
                org_name="",
                create_subscription=True,
                product_enablement={
                    "product_name": "productName",
                    "type": "NGC_ADMIN_EVAL",
                },
            )

    @parametrize
    async def test_method_org_owner_backfill(self, async_client: AsyncNgc) -> None:
        org = await async_client.admin.orgs.org_owner_backfill(
            "org-name",
        )
        assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

    @parametrize
    async def test_raw_response_org_owner_backfill(self, async_client: AsyncNgc) -> None:
        response = await async_client.admin.orgs.with_raw_response.org_owner_backfill(
            "org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

    @parametrize
    async def test_streaming_response_org_owner_backfill(self, async_client: AsyncNgc) -> None:
        async with async_client.admin.orgs.with_streaming_response.org_owner_backfill(
            "org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_org_owner_backfill(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.admin.orgs.with_raw_response.org_owner_backfill(
                "",
            )

    @parametrize
    async def test_method_validate(self, async_client: AsyncNgc) -> None:
        org = await async_client.admin.orgs.validate(
            invitation_token="invitation_token",
        )
        assert_matches_type(OrgValidateResponse, org, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncNgc) -> None:
        response = await async_client.admin.orgs.with_raw_response.validate(
            invitation_token="invitation_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgValidateResponse, org, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncNgc) -> None:
        async with async_client.admin.orgs.with_streaming_response.validate(
            invitation_token="invitation_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgValidateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True
