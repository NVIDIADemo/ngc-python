# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.shared import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNcaInvitations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ngc) -> None:
        nca_invitation = client.orgs.teams.nca_invitations.create(
            team_name="team-name",
            org_name="org-name",
        )
        assert_matches_type(User, nca_invitation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Ngc) -> None:
        nca_invitation = client.orgs.teams.nca_invitations.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxxx",
            invitation_expiration_in=0,
            invite_as="ADMIN",
            message="message",
        )
        assert_matches_type(User, nca_invitation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ngc) -> None:
        response = client.orgs.teams.nca_invitations.with_raw_response.create(
            team_name="team-name",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nca_invitation = response.parse()
        assert_matches_type(User, nca_invitation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ngc) -> None:
        with client.orgs.teams.nca_invitations.with_streaming_response.create(
            team_name="team-name",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nca_invitation = response.parse()
            assert_matches_type(User, nca_invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.teams.nca_invitations.with_raw_response.create(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.orgs.teams.nca_invitations.with_raw_response.create(
                team_name="",
                org_name="org-name",
            )


class TestAsyncNcaInvitations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNgc) -> None:
        nca_invitation = await async_client.orgs.teams.nca_invitations.create(
            team_name="team-name",
            org_name="org-name",
        )
        assert_matches_type(User, nca_invitation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNgc) -> None:
        nca_invitation = await async_client.orgs.teams.nca_invitations.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxxx",
            invitation_expiration_in=0,
            invite_as="ADMIN",
            message="message",
        )
        assert_matches_type(User, nca_invitation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.teams.nca_invitations.with_raw_response.create(
            team_name="team-name",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nca_invitation = await response.parse()
        assert_matches_type(User, nca_invitation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.teams.nca_invitations.with_streaming_response.create(
            team_name="team-name",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nca_invitation = await response.parse()
            assert_matches_type(User, nca_invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.teams.nca_invitations.with_raw_response.create(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.orgs.teams.nca_invitations.with_raw_response.create(
                team_name="",
                org_name="org-name",
            )
