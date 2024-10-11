# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.shared import User
from ngc.types.orgs.teams import UserDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Ngc) -> None:
        user = client.orgs.teams.users.delete(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Ngc) -> None:
        user = client.orgs.teams.users.delete(
            id="id",
            org_name="org-name",
            team_name="team-name",
            anonymize=True,
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Ngc) -> None:
        response = client.orgs.teams.users.with_raw_response.delete(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Ngc) -> None:
        with client.orgs.teams.users.with_streaming_response.delete(
            id="id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.teams.users.with_raw_response.delete(
                id="id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.orgs.teams.users.with_raw_response.delete(
                id="id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.orgs.teams.users.with_raw_response.delete(
                id="",
                org_name="org-name",
                team_name="team-name",
            )

    @parametrize
    def test_method_add_role(self, client: Ngc) -> None:
        user = client.orgs.teams.users.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_add_role(self, client: Ngc) -> None:
        response = client.orgs.teams.users.with_raw_response.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_add_role(self, client: Ngc) -> None:
        with client.orgs.teams.users.with_streaming_response.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_role(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.teams.users.with_raw_response.add_role(
                user_email_or_id="user-email-or-id",
                org_name="",
                team_name="team-name",
                roles=["string", "string", "string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.orgs.teams.users.with_raw_response.add_role(
                user_email_or_id="user-email-or-id",
                org_name="org-name",
                team_name="",
                roles=["string", "string", "string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_email_or_id` but received ''"):
            client.orgs.teams.users.with_raw_response.add_role(
                user_email_or_id="",
                org_name="org-name",
                team_name="team-name",
                roles=["string", "string", "string"],
            )

    @parametrize
    def test_method_remove_role(self, client: Ngc) -> None:
        user = client.orgs.teams.users.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_remove_role_with_all_params(self, client: Ngc) -> None:
        user = client.orgs.teams.users.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_remove_role(self, client: Ngc) -> None:
        response = client.orgs.teams.users.with_raw_response.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_remove_role(self, client: Ngc) -> None:
        with client.orgs.teams.users.with_streaming_response.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_role(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.teams.users.with_raw_response.remove_role(
                user_email_or_id="user-email-or-id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.orgs.teams.users.with_raw_response.remove_role(
                user_email_or_id="user-email-or-id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_email_or_id` but received ''"):
            client.orgs.teams.users.with_raw_response.remove_role(
                user_email_or_id="",
                org_name="org-name",
                team_name="team-name",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.teams.users.delete(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.teams.users.delete(
            id="id",
            org_name="org-name",
            team_name="team-name",
            anonymize=True,
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.teams.users.with_raw_response.delete(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.teams.users.with_streaming_response.delete(
            id="id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.delete(
                id="id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.delete(
                id="id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.delete(
                id="",
                org_name="org-name",
                team_name="team-name",
            )

    @parametrize
    async def test_method_add_role(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.teams.users.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_add_role(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.teams.users.with_raw_response.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_add_role(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.teams.users.with_streaming_response.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_role(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.add_role(
                user_email_or_id="user-email-or-id",
                org_name="",
                team_name="team-name",
                roles=["string", "string", "string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.add_role(
                user_email_or_id="user-email-or-id",
                org_name="org-name",
                team_name="",
                roles=["string", "string", "string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_email_or_id` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.add_role(
                user_email_or_id="",
                org_name="org-name",
                team_name="team-name",
                roles=["string", "string", "string"],
            )

    @parametrize
    async def test_method_remove_role(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.teams.users.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_remove_role_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.teams.users.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_remove_role(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.teams.users.with_raw_response.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_remove_role(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.teams.users.with_streaming_response.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_role(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.remove_role(
                user_email_or_id="user-email-or-id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.remove_role(
                user_email_or_id="user-email-or-id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_email_or_id` but received ''"):
            await async_client.orgs.teams.users.with_raw_response.remove_role(
                user_email_or_id="",
                org_name="org-name",
                team_name="team-name",
            )
