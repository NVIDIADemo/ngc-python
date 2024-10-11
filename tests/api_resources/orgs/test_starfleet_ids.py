# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.shared import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStarfleetIDs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Ngc) -> None:
        starfleet_id = client.orgs.starfleet_ids.retrieve(
            starfleet_id="starfleet-id",
            org_name="org-name",
        )
        assert_matches_type(User, starfleet_id, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ngc) -> None:
        response = client.orgs.starfleet_ids.with_raw_response.retrieve(
            starfleet_id="starfleet-id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starfleet_id = response.parse()
        assert_matches_type(User, starfleet_id, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ngc) -> None:
        with client.orgs.starfleet_ids.with_streaming_response.retrieve(
            starfleet_id="starfleet-id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starfleet_id = response.parse()
            assert_matches_type(User, starfleet_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.starfleet_ids.with_raw_response.retrieve(
                starfleet_id="starfleet-id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `starfleet_id` but received ''"):
            client.orgs.starfleet_ids.with_raw_response.retrieve(
                starfleet_id="",
                org_name="org-name",
            )


class TestAsyncStarfleetIDs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNgc) -> None:
        starfleet_id = await async_client.orgs.starfleet_ids.retrieve(
            starfleet_id="starfleet-id",
            org_name="org-name",
        )
        assert_matches_type(User, starfleet_id, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.starfleet_ids.with_raw_response.retrieve(
            starfleet_id="starfleet-id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        starfleet_id = await response.parse()
        assert_matches_type(User, starfleet_id, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.starfleet_ids.with_streaming_response.retrieve(
            starfleet_id="starfleet-id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            starfleet_id = await response.parse()
            assert_matches_type(User, starfleet_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.starfleet_ids.with_raw_response.retrieve(
                starfleet_id="starfleet-id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `starfleet_id` but received ''"):
            await async_client.orgs.starfleet_ids.with_raw_response.retrieve(
                starfleet_id="",
                org_name="org-name",
            )
