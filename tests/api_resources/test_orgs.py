# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from ngc.types import OrgResponse, OrgListResponse
from tests.utils import assert_matches_type
from ngc.pagination import SyncPageNumberOrganizations, AsyncPageNumberOrganizations

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrgs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ngc) -> None:
        org = client.orgs.create()
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Ngc) -> None:
        org = client.orgs.create(
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
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ngc) -> None:
        response = client.orgs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ngc) -> None:
        with client.orgs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Ngc) -> None:
        org = client.orgs.retrieve(
            "org-name",
        )
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ngc) -> None:
        response = client.orgs.with_raw_response.retrieve(
            "org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ngc) -> None:
        with client.orgs.with_streaming_response.retrieve(
            "org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Ngc) -> None:
        org = client.orgs.update(
            org_name="org-name",
        )
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Ngc) -> None:
        org = client.orgs.update(
            org_name="org-name",
            description="description",
            display_name="x",
        )
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Ngc) -> None:
        response = client.orgs.with_raw_response.update(
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Ngc) -> None:
        with client.orgs.with_streaming_response.update(
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.with_raw_response.update(
                org_name="",
            )

    @parametrize
    def test_method_list(self, client: Ngc) -> None:
        org = client.orgs.list()
        assert_matches_type(SyncPageNumberOrganizations[OrgListResponse], org, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Ngc) -> None:
        org = client.orgs.list(
            filter_using_org_display_name="Filter using org display name",
            filter_using_org_name="Filter using org name",
            filter_using_org_owner_email="Filter using org owner email",
            filter_using_org_owner_name="Filter using org owner name",
            filter_using_pec_id="Filter using PEC ID",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncPageNumberOrganizations[OrgListResponse], org, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Ngc) -> None:
        response = client.orgs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(SyncPageNumberOrganizations[OrgListResponse], org, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Ngc) -> None:
        with client.orgs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(SyncPageNumberOrganizations[OrgListResponse], org, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrgs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNgc) -> None:
        org = await async_client.orgs.create()
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNgc) -> None:
        org = await async_client.orgs.create(
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
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNgc) -> None:
        org = await async_client.orgs.retrieve(
            "org-name",
        )
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.with_raw_response.retrieve(
            "org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.with_streaming_response.retrieve(
            "org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncNgc) -> None:
        org = await async_client.orgs.update(
            org_name="org-name",
        )
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNgc) -> None:
        org = await async_client.orgs.update(
            org_name="org-name",
            description="description",
            display_name="x",
        )
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.with_raw_response.update(
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgResponse, org, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.with_streaming_response.update(
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.with_raw_response.update(
                org_name="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncNgc) -> None:
        org = await async_client.orgs.list()
        assert_matches_type(AsyncPageNumberOrganizations[OrgListResponse], org, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNgc) -> None:
        org = await async_client.orgs.list(
            filter_using_org_display_name="Filter using org display name",
            filter_using_org_name="Filter using org name",
            filter_using_org_owner_email="Filter using org owner email",
            filter_using_org_owner_name="Filter using org owner name",
            filter_using_pec_id="Filter using PEC ID",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncPageNumberOrganizations[OrgListResponse], org, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(AsyncPageNumberOrganizations[OrgListResponse], org, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(AsyncPageNumberOrganizations[OrgListResponse], org, path=["response"])

        assert cast(Any, response.is_closed) is True
