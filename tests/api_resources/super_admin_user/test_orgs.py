# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.super_admin_user import OrgOrgOwnerBackfillResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrgs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_org_owner_backfill(self, client: Ngc) -> None:
        org = client.super_admin_user.orgs.org_owner_backfill(
            "org-name",
        )
        assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

    @parametrize
    def test_raw_response_org_owner_backfill(self, client: Ngc) -> None:
        response = client.super_admin_user.orgs.with_raw_response.org_owner_backfill(
            "org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

    @parametrize
    def test_streaming_response_org_owner_backfill(self, client: Ngc) -> None:
        with client.super_admin_user.orgs.with_streaming_response.org_owner_backfill(
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
            client.super_admin_user.orgs.with_raw_response.org_owner_backfill(
                "",
            )


class TestAsyncOrgs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_org_owner_backfill(self, async_client: AsyncNgc) -> None:
        org = await async_client.super_admin_user.orgs.org_owner_backfill(
            "org-name",
        )
        assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

    @parametrize
    async def test_raw_response_org_owner_backfill(self, async_client: AsyncNgc) -> None:
        response = await async_client.super_admin_user.orgs.with_raw_response.org_owner_backfill(
            "org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgOrgOwnerBackfillResponse, org, path=["response"])

    @parametrize
    async def test_streaming_response_org_owner_backfill(self, async_client: AsyncNgc) -> None:
        async with async_client.super_admin_user.orgs.with_streaming_response.org_owner_backfill(
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
            await async_client.super_admin_user.orgs.with_raw_response.org_owner_backfill(
                "",
            )
