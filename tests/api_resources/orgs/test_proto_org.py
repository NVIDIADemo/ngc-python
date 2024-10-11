# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from ngc.types import OrgResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProtoOrg:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ngc) -> None:
        proto_org = client.orgs.proto_org.create()
        assert_matches_type(OrgResponse, proto_org, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Ngc) -> None:
        proto_org = client.orgs.proto_org.create(
            country="country",
            description="description",
            display_name="x",
            initiator="initiator",
            is_internal=True,
            name="xx",
            nca_id="ncaId",
            nca_number="ncaNumber",
            org_owner={
                "email": "email",
                "full_name": "x",
                "idp_id": "idpId",
                "starfleet_id": "starfleetId",
            },
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
            proto_org_id="protoOrgId",
            salesforce_account_industry="salesforceAccountIndustry",
            send_email=True,
            type="UNKNOWN",
        )
        assert_matches_type(OrgResponse, proto_org, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ngc) -> None:
        response = client.orgs.proto_org.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proto_org = response.parse()
        assert_matches_type(OrgResponse, proto_org, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ngc) -> None:
        with client.orgs.proto_org.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proto_org = response.parse()
            assert_matches_type(OrgResponse, proto_org, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProtoOrg:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNgc) -> None:
        proto_org = await async_client.orgs.proto_org.create()
        assert_matches_type(OrgResponse, proto_org, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNgc) -> None:
        proto_org = await async_client.orgs.proto_org.create(
            country="country",
            description="description",
            display_name="x",
            initiator="initiator",
            is_internal=True,
            name="xx",
            nca_id="ncaId",
            nca_number="ncaNumber",
            org_owner={
                "email": "email",
                "full_name": "x",
                "idp_id": "idpId",
                "starfleet_id": "starfleetId",
            },
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
            proto_org_id="protoOrgId",
            salesforce_account_industry="salesforceAccountIndustry",
            send_email=True,
            type="UNKNOWN",
        )
        assert_matches_type(OrgResponse, proto_org, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.proto_org.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proto_org = await response.parse()
        assert_matches_type(OrgResponse, proto_org, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.proto_org.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proto_org = await response.parse()
            assert_matches_type(OrgResponse, proto_org, path=["response"])

        assert cast(Any, response.is_closed) is True
