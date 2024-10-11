# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from ngc._utils import parse_datetime
from tests.utils import assert_matches_type
from ngc.types.shared import MeteringResultList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGpupeak:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_all(self, client: Ngc) -> None:
        gpupeak = client.orgs.metering.gpupeak.retrieve_all(
            org_name="org-name",
        )
        assert_matches_type(MeteringResultList, gpupeak, path=["response"])

    @parametrize
    def test_method_retrieve_all_with_all_params(self, client: Ngc) -> None:
        gpupeak = client.orgs.metering.gpupeak.retrieve_all(
            org_name="org-name",
            the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss={
                "sssz": parse_datetime("2019-12-27T18:11:19.117Z")
            },
        )
        assert_matches_type(MeteringResultList, gpupeak, path=["response"])

    @parametrize
    def test_raw_response_retrieve_all(self, client: Ngc) -> None:
        response = client.orgs.metering.gpupeak.with_raw_response.retrieve_all(
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpupeak = response.parse()
        assert_matches_type(MeteringResultList, gpupeak, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_all(self, client: Ngc) -> None:
        with client.orgs.metering.gpupeak.with_streaming_response.retrieve_all(
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpupeak = response.parse()
            assert_matches_type(MeteringResultList, gpupeak, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_all(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.metering.gpupeak.with_raw_response.retrieve_all(
                org_name="",
            )


class TestAsyncGpupeak:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncNgc) -> None:
        gpupeak = await async_client.orgs.metering.gpupeak.retrieve_all(
            org_name="org-name",
        )
        assert_matches_type(MeteringResultList, gpupeak, path=["response"])

    @parametrize
    async def test_method_retrieve_all_with_all_params(self, async_client: AsyncNgc) -> None:
        gpupeak = await async_client.orgs.metering.gpupeak.retrieve_all(
            org_name="org-name",
            the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss={
                "sssz": parse_datetime("2019-12-27T18:11:19.117Z")
            },
        )
        assert_matches_type(MeteringResultList, gpupeak, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.metering.gpupeak.with_raw_response.retrieve_all(
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpupeak = await response.parse()
        assert_matches_type(MeteringResultList, gpupeak, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.metering.gpupeak.with_streaming_response.retrieve_all(
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpupeak = await response.parse()
            assert_matches_type(MeteringResultList, gpupeak, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_all(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.metering.gpupeak.with_raw_response.retrieve_all(
                org_name="",
            )
