# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from ngc.types import OrgInvitation
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV3Orgs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_validate(self, client: Ngc) -> None:
        v3_org = client.v3_orgs.validate(
            invitation_token="invitation_token",
        )
        assert_matches_type(OrgInvitation, v3_org, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Ngc) -> None:
        response = client.v3_orgs.with_raw_response.validate(
            invitation_token="invitation_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3_org = response.parse()
        assert_matches_type(OrgInvitation, v3_org, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Ngc) -> None:
        with client.v3_orgs.with_streaming_response.validate(
            invitation_token="invitation_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3_org = response.parse()
            assert_matches_type(OrgInvitation, v3_org, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV3Orgs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_validate(self, async_client: AsyncNgc) -> None:
        v3_org = await async_client.v3_orgs.validate(
            invitation_token="invitation_token",
        )
        assert_matches_type(OrgInvitation, v3_org, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncNgc) -> None:
        response = await async_client.v3_orgs.with_raw_response.validate(
            invitation_token="invitation_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3_org = await response.parse()
        assert_matches_type(OrgInvitation, v3_org, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncNgc) -> None:
        async with async_client.v3_orgs.with_streaming_response.validate(
            invitation_token="invitation_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3_org = await response.parse()
            assert_matches_type(OrgInvitation, v3_org, path=["response"])

        assert cast(Any, response.is_closed) is True
