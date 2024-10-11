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
from ngc.types.shared import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ngc) -> None:
        user = client.admin.orgs.teams.users.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxx",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Ngc) -> None:
        user = client.admin.orgs.teams.users.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxx",
            idp_id="idp-id",
            send_email=True,
            email_opt_in=True,
            eula_accepted=True,
            name="x",
            role_type="roleType",
            role_types=["string", "string", "string"],
            salesforce_contact_job_role="salesforceContactJobRole",
            user_metadata={
                "company": "company",
                "company_url": "companyUrl",
                "country": "country",
                "first_name": "firstName",
                "industry": "industry",
                "interest": ["string", "string", "string"],
                "last_name": "lastName",
                "role": "role",
            },
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ngc) -> None:
        response = client.admin.orgs.teams.users.with_raw_response.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ngc) -> None:
        with client.admin.orgs.teams.users.with_streaming_response.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.create(
                team_name="team-name",
                org_name="",
                email="xxxxxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.create(
                team_name="",
                org_name="org-name",
                email="xxxxxx",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        user = client.admin.orgs.teams.users.retrieve(
            team_name="team-name",
            org_name="org-name",
        )
        assert user.is_closed
        assert user.json() == {"foo": "bar"}
        assert cast(Any, user.is_closed) is True
        assert isinstance(user, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        user = client.admin.orgs.teams.users.with_raw_response.retrieve(
            team_name="team-name",
            org_name="org-name",
        )

        assert user.is_closed is True
        assert user.http_request.headers.get("X-Stainless-Lang") == "python"
        assert user.json() == {"foo": "bar"}
        assert isinstance(user, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.admin.orgs.teams.users.with_streaming_response.retrieve(
            team_name="team-name",
            org_name="org-name",
        ) as user:
            assert not user.is_closed
            assert user.http_request.headers.get("X-Stainless-Lang") == "python"

            assert user.json() == {"foo": "bar"}
            assert cast(Any, user.is_closed) is True
            assert isinstance(user, StreamedBinaryAPIResponse)

        assert cast(Any, user.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.retrieve(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.retrieve(
                team_name="",
                org_name="org-name",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        user = client.admin.orgs.teams.users.update(
            team_name="team-name",
            org_name="org-name",
        )
        assert user.is_closed
        assert user.json() == {"foo": "bar"}
        assert cast(Any, user.is_closed) is True
        assert isinstance(user, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        user = client.admin.orgs.teams.users.update(
            team_name="team-name",
            org_name="org-name",
            description="description",
            infinity_manager_settings={
                "infinity_manager_enabled": True,
                "infinity_manager_enable_team_override": True,
            },
            repo_scan_settings={
                "repo_scan_allow_override": True,
                "repo_scan_by_default": True,
                "repo_scan_enabled": True,
                "repo_scan_enable_notifications": True,
                "repo_scan_enable_team_override": True,
                "repo_scan_show_results": True,
            },
        )
        assert user.is_closed
        assert user.json() == {"foo": "bar"}
        assert cast(Any, user.is_closed) is True
        assert isinstance(user, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        user = client.admin.orgs.teams.users.with_raw_response.update(
            team_name="team-name",
            org_name="org-name",
        )

        assert user.is_closed is True
        assert user.http_request.headers.get("X-Stainless-Lang") == "python"
        assert user.json() == {"foo": "bar"}
        assert isinstance(user, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.admin.orgs.teams.users.with_streaming_response.update(
            team_name="team-name",
            org_name="org-name",
        ) as user:
            assert not user.is_closed
            assert user.http_request.headers.get("X-Stainless-Lang") == "python"

            assert user.json() == {"foo": "bar"}
            assert cast(Any, user.is_closed) is True
            assert isinstance(user, StreamedBinaryAPIResponse)

        assert cast(Any, user.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.update(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.update(
                team_name="",
                org_name="org-name",
            )

    @parametrize
    def test_method_add(self, client: Ngc) -> None:
        user = client.admin.orgs.teams.users.add(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Ngc) -> None:
        user = client.admin.orgs.teams.users.add(
            id="id",
            org_name="org-name",
            team_name="team-name",
            user_role_defaults_to_registry_read="user role, defaults to REGISTRY_READ",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Ngc) -> None:
        response = client.admin.orgs.teams.users.with_raw_response.add(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Ngc) -> None:
        with client.admin.orgs.teams.users.with_streaming_response.add(
            id="id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.add(
                id="id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.add(
                id="id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.add(
                id="",
                org_name="org-name",
                team_name="team-name",
            )

    @parametrize
    def test_method_add_role(self, client: Ngc) -> None:
        user = client.admin.orgs.teams.users.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_add_role_with_all_params(self, client: Ngc) -> None:
        user = client.admin.orgs.teams.users.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_add_role(self, client: Ngc) -> None:
        response = client.admin.orgs.teams.users.with_raw_response.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_add_role(self, client: Ngc) -> None:
        with client.admin.orgs.teams.users.with_streaming_response.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_role(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.add_role(
                id="id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.add_role(
                id="id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.admin.orgs.teams.users.with_raw_response.add_role(
                id="",
                org_name="org-name",
                team_name="team-name",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNgc) -> None:
        user = await async_client.admin.orgs.teams.users.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxx",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.admin.orgs.teams.users.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxx",
            idp_id="idp-id",
            send_email=True,
            email_opt_in=True,
            eula_accepted=True,
            name="x",
            role_type="roleType",
            role_types=["string", "string", "string"],
            salesforce_contact_job_role="salesforceContactJobRole",
            user_metadata={
                "company": "company",
                "company_url": "companyUrl",
                "country": "country",
                "first_name": "firstName",
                "industry": "industry",
                "interest": ["string", "string", "string"],
                "last_name": "lastName",
                "role": "role",
            },
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNgc) -> None:
        response = await async_client.admin.orgs.teams.users.with_raw_response.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNgc) -> None:
        async with async_client.admin.orgs.teams.users.with_streaming_response.create(
            team_name="team-name",
            org_name="org-name",
            email="xxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.create(
                team_name="team-name",
                org_name="",
                email="xxxxxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.create(
                team_name="",
                org_name="org-name",
                email="xxxxxx",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        user = await async_client.admin.orgs.teams.users.retrieve(
            team_name="team-name",
            org_name="org-name",
        )
        assert user.is_closed
        assert await user.json() == {"foo": "bar"}
        assert cast(Any, user.is_closed) is True
        assert isinstance(user, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        user = await async_client.admin.orgs.teams.users.with_raw_response.retrieve(
            team_name="team-name",
            org_name="org-name",
        )

        assert user.is_closed is True
        assert user.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await user.json() == {"foo": "bar"}
        assert isinstance(user, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.admin.orgs.teams.users.with_streaming_response.retrieve(
            team_name="team-name",
            org_name="org-name",
        ) as user:
            assert not user.is_closed
            assert user.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await user.json() == {"foo": "bar"}
            assert cast(Any, user.is_closed) is True
            assert isinstance(user, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, user.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.retrieve(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.retrieve(
                team_name="",
                org_name="org-name",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        user = await async_client.admin.orgs.teams.users.update(
            team_name="team-name",
            org_name="org-name",
        )
        assert user.is_closed
        assert await user.json() == {"foo": "bar"}
        assert cast(Any, user.is_closed) is True
        assert isinstance(user, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        user = await async_client.admin.orgs.teams.users.update(
            team_name="team-name",
            org_name="org-name",
            description="description",
            infinity_manager_settings={
                "infinity_manager_enabled": True,
                "infinity_manager_enable_team_override": True,
            },
            repo_scan_settings={
                "repo_scan_allow_override": True,
                "repo_scan_by_default": True,
                "repo_scan_enabled": True,
                "repo_scan_enable_notifications": True,
                "repo_scan_enable_team_override": True,
                "repo_scan_show_results": True,
            },
        )
        assert user.is_closed
        assert await user.json() == {"foo": "bar"}
        assert cast(Any, user.is_closed) is True
        assert isinstance(user, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        user = await async_client.admin.orgs.teams.users.with_raw_response.update(
            team_name="team-name",
            org_name="org-name",
        )

        assert user.is_closed is True
        assert user.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await user.json() == {"foo": "bar"}
        assert isinstance(user, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.admin.orgs.teams.users.with_streaming_response.update(
            team_name="team-name",
            org_name="org-name",
        ) as user:
            assert not user.is_closed
            assert user.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await user.json() == {"foo": "bar"}
            assert cast(Any, user.is_closed) is True
            assert isinstance(user, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, user.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.update(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.update(
                team_name="",
                org_name="org-name",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncNgc) -> None:
        user = await async_client.admin.orgs.teams.users.add(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.admin.orgs.teams.users.add(
            id="id",
            org_name="org-name",
            team_name="team-name",
            user_role_defaults_to_registry_read="user role, defaults to REGISTRY_READ",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncNgc) -> None:
        response = await async_client.admin.orgs.teams.users.with_raw_response.add(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncNgc) -> None:
        async with async_client.admin.orgs.teams.users.with_streaming_response.add(
            id="id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.add(
                id="id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.add(
                id="id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.add(
                id="",
                org_name="org-name",
                team_name="team-name",
            )

    @parametrize
    async def test_method_add_role(self, async_client: AsyncNgc) -> None:
        user = await async_client.admin.orgs.teams.users.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_add_role_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.admin.orgs.teams.users.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_add_role(self, async_client: AsyncNgc) -> None:
        response = await async_client.admin.orgs.teams.users.with_raw_response.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_add_role(self, async_client: AsyncNgc) -> None:
        async with async_client.admin.orgs.teams.users.with_streaming_response.add_role(
            id="id",
            org_name="org-name",
            team_name="team-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_role(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.add_role(
                id="id",
                org_name="",
                team_name="team-name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.add_role(
                id="id",
                org_name="org-name",
                team_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.admin.orgs.teams.users.with_raw_response.add_role(
                id="",
                org_name="org-name",
                team_name="team-name",
            )
