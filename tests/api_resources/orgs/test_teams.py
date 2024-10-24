# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.pagination import SyncPageNumberTeams, AsyncPageNumberTeams
from ngc.types.shared import Team

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Ngc) -> None:
        team = client.orgs.teams.list(
            org_name="org-name",
        )
        assert_matches_type(SyncPageNumberTeams[Team], team, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Ngc) -> None:
        team = client.orgs.teams.list(
            org_name="org-name",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncPageNumberTeams[Team], team, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Ngc) -> None:
        response = client.orgs.teams.with_raw_response.list(
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(SyncPageNumberTeams[Team], team, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Ngc) -> None:
        with client.orgs.teams.with_streaming_response.list(
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(SyncPageNumberTeams[Team], team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.teams.with_raw_response.list(
                org_name="",
            )


class TestAsyncTeams:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncNgc) -> None:
        team = await async_client.orgs.teams.list(
            org_name="org-name",
        )
        assert_matches_type(AsyncPageNumberTeams[Team], team, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNgc) -> None:
        team = await async_client.orgs.teams.list(
            org_name="org-name",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncPageNumberTeams[Team], team, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.teams.with_raw_response.list(
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(AsyncPageNumberTeams[Team], team, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.teams.with_streaming_response.list(
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(AsyncPageNumberTeams[Team], team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.teams.with_raw_response.list(
                org_name="",
            )
