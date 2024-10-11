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


class TestV2AdminOrgTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_team = client.v2_admin_org_teams.retrieve(
            team_name="team-name",
            org_name="org-name",
        )
        assert v2_admin_org_team.is_closed
        assert v2_admin_org_team.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_team.is_closed) is True
        assert isinstance(v2_admin_org_team, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        v2_admin_org_team = client.v2_admin_org_teams.with_raw_response.retrieve(
            team_name="team-name",
            org_name="org-name",
        )

        assert v2_admin_org_team.is_closed is True
        assert v2_admin_org_team.http_request.headers.get("X-Stainless-Lang") == "python"
        assert v2_admin_org_team.json() == {"foo": "bar"}
        assert isinstance(v2_admin_org_team, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.v2_admin_org_teams.with_streaming_response.retrieve(
            team_name="team-name",
            org_name="org-name",
        ) as v2_admin_org_team:
            assert not v2_admin_org_team.is_closed
            assert v2_admin_org_team.http_request.headers.get("X-Stainless-Lang") == "python"

            assert v2_admin_org_team.json() == {"foo": "bar"}
            assert cast(Any, v2_admin_org_team.is_closed) is True
            assert isinstance(v2_admin_org_team, StreamedBinaryAPIResponse)

        assert cast(Any, v2_admin_org_team.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.v2_admin_org_teams.with_raw_response.retrieve(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.v2_admin_org_teams.with_raw_response.retrieve(
                team_name="",
                org_name="org-name",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_team = client.v2_admin_org_teams.update(
            team_name="team-name",
            org_name="org-name",
        )
        assert v2_admin_org_team.is_closed
        assert v2_admin_org_team.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_team.is_closed) is True
        assert isinstance(v2_admin_org_team, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_team = client.v2_admin_org_teams.update(
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
        assert v2_admin_org_team.is_closed
        assert v2_admin_org_team.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_team.is_closed) is True
        assert isinstance(v2_admin_org_team, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        v2_admin_org_team = client.v2_admin_org_teams.with_raw_response.update(
            team_name="team-name",
            org_name="org-name",
        )

        assert v2_admin_org_team.is_closed is True
        assert v2_admin_org_team.http_request.headers.get("X-Stainless-Lang") == "python"
        assert v2_admin_org_team.json() == {"foo": "bar"}
        assert isinstance(v2_admin_org_team, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.v2_admin_org_teams.with_streaming_response.update(
            team_name="team-name",
            org_name="org-name",
        ) as v2_admin_org_team:
            assert not v2_admin_org_team.is_closed
            assert v2_admin_org_team.http_request.headers.get("X-Stainless-Lang") == "python"

            assert v2_admin_org_team.json() == {"foo": "bar"}
            assert cast(Any, v2_admin_org_team.is_closed) is True
            assert isinstance(v2_admin_org_team, StreamedBinaryAPIResponse)

        assert cast(Any, v2_admin_org_team.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.v2_admin_org_teams.with_raw_response.update(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            client.v2_admin_org_teams.with_raw_response.update(
                team_name="",
                org_name="org-name",
            )


class TestAsyncV2AdminOrgTeams:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_team = await async_client.v2_admin_org_teams.retrieve(
            team_name="team-name",
            org_name="org-name",
        )
        assert v2_admin_org_team.is_closed
        assert await v2_admin_org_team.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_team.is_closed) is True
        assert isinstance(v2_admin_org_team, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        v2_admin_org_team = await async_client.v2_admin_org_teams.with_raw_response.retrieve(
            team_name="team-name",
            org_name="org-name",
        )

        assert v2_admin_org_team.is_closed is True
        assert v2_admin_org_team.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await v2_admin_org_team.json() == {"foo": "bar"}
        assert isinstance(v2_admin_org_team, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.v2_admin_org_teams.with_streaming_response.retrieve(
            team_name="team-name",
            org_name="org-name",
        ) as v2_admin_org_team:
            assert not v2_admin_org_team.is_closed
            assert v2_admin_org_team.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await v2_admin_org_team.json() == {"foo": "bar"}
            assert cast(Any, v2_admin_org_team.is_closed) is True
            assert isinstance(v2_admin_org_team, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, v2_admin_org_team.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.v2_admin_org_teams.with_raw_response.retrieve(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.v2_admin_org_teams.with_raw_response.retrieve(
                team_name="",
                org_name="org-name",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_team = await async_client.v2_admin_org_teams.update(
            team_name="team-name",
            org_name="org-name",
        )
        assert v2_admin_org_team.is_closed
        assert await v2_admin_org_team.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_team.is_closed) is True
        assert isinstance(v2_admin_org_team, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        v2_admin_org_team = await async_client.v2_admin_org_teams.update(
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
        assert v2_admin_org_team.is_closed
        assert await v2_admin_org_team.json() == {"foo": "bar"}
        assert cast(Any, v2_admin_org_team.is_closed) is True
        assert isinstance(v2_admin_org_team, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        v2_admin_org_team = await async_client.v2_admin_org_teams.with_raw_response.update(
            team_name="team-name",
            org_name="org-name",
        )

        assert v2_admin_org_team.is_closed is True
        assert v2_admin_org_team.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await v2_admin_org_team.json() == {"foo": "bar"}
        assert isinstance(v2_admin_org_team, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/v2/admin/org/org-name/teams/team-name").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.v2_admin_org_teams.with_streaming_response.update(
            team_name="team-name",
            org_name="org-name",
        ) as v2_admin_org_team:
            assert not v2_admin_org_team.is_closed
            assert v2_admin_org_team.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await v2_admin_org_team.json() == {"foo": "bar"}
            assert cast(Any, v2_admin_org_team.is_closed) is True
            assert isinstance(v2_admin_org_team, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, v2_admin_org_team.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.v2_admin_org_teams.with_raw_response.update(
                team_name="team-name",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_name` but received ''"):
            await async_client.v2_admin_org_teams.with_raw_response.update(
                team_name="",
                org_name="org-name",
            )
