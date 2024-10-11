# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.shared import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2AdminOrgTeamUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_role(self, client: Ngc) -> None:
        v2_admin_org_team_user = client.v2_admin_org_team_users.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(User, v2_admin_org_team_user, path=["response"])

    @parametrize
    def test_method_add_role_with_all_params(self, client: Ngc) -> None:
        v2_admin_org_team_user = client.v2_admin_org_team_users.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, v2_admin_org_team_user, path=["response"])

    @parametrize
    def test_raw_response_add_role(self, client: Ngc) -> None:
        response = client.v2_admin_org_team_users.with_raw_response.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_admin_org_team_user = response.parse()
        assert_matches_type(User, v2_admin_org_team_user, path=["response"])

    @parametrize
    def test_streaming_response_add_role(self, client: Ngc) -> None:
        with client.v2_admin_org_team_users.with_streaming_response.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_admin_org_team_user = response.parse()
            assert_matches_type(User, v2_admin_org_team_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_role(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.v2_admin_org_team_users.with_raw_response.add_role(
                id="id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.v2_admin_org_team_users.with_raw_response.add_role(
                id="id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v2_admin_org_team_users.with_raw_response.add_role(
                id="",
                org_name="org-name",
                team_name="team-name",
            )


class TestAsyncV2AdminOrgTeamUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_add_role(self, async_client: AsyncNgc) -> None:
        v2_admin_org_team_user = await async_client.v2_admin_org_team_users.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(User, v2_admin_org_team_user, path=["response"])

    @parametrize
    async def test_method_add_role_with_all_params(self, async_client: AsyncNgc) -> None:
        v2_admin_org_team_user = await async_client.v2_admin_org_team_users.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, v2_admin_org_team_user, path=["response"])

    @parametrize
    async def test_raw_response_add_role(self, async_client: AsyncNgc) -> None:
        response = await async_client.v2_admin_org_team_users.with_raw_response.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_admin_org_team_user = await response.parse()
        assert_matches_type(User, v2_admin_org_team_user, path=["response"])

    @parametrize
    async def test_streaming_response_add_role(self, async_client: AsyncNgc) -> None:
        async with async_client.v2_admin_org_team_users.with_streaming_response.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_admin_org_team_user = await response.parse()
            assert_matches_type(User, v2_admin_org_team_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_role(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.v2_admin_org_team_users.with_raw_response.add_role(
                id="id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.v2_admin_org_team_users.with_raw_response.add_role(
                id="id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v2_admin_org_team_users.with_raw_response.add_role(
                id="",
                org_name="org-name",
                team_name="team-name",
            )
