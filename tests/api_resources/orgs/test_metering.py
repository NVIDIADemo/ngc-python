# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.shared import MeteringResultList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetering:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_all(self, client: Ngc) -> None:
        metering = client.orgs.metering.retrieve_all(
            org_name="org-name",
            q={},
        )
        assert_matches_type(MeteringResultList, metering, path=["response"])

    @parametrize
    def test_method_retrieve_all_with_all_params(self, client: Ngc) -> None:
        metering = client.orgs.metering.retrieve_all(
            org_name="org-name",
            q={
                "measurements": [
                    {
                        "fill": 0,
                        "from_date": "fromDate",
                        "group_by": ["string", "string", "string"],
                        "period_in_seconds": 0,
                        "to_date": "toDate",
                        "type": "EGX_GPU_UTILIZATION_DAILY",
                    },
                    {
                        "fill": 0,
                        "from_date": "fromDate",
                        "group_by": ["string", "string", "string"],
                        "period_in_seconds": 0,
                        "to_date": "toDate",
                        "type": "EGX_GPU_UTILIZATION_DAILY",
                    },
                    {
                        "fill": 0,
                        "from_date": "fromDate",
                        "group_by": ["string", "string", "string"],
                        "period_in_seconds": 0,
                        "to_date": "toDate",
                        "type": "EGX_GPU_UTILIZATION_DAILY",
                    },
                ]
            },
        )
        assert_matches_type(MeteringResultList, metering, path=["response"])

    @parametrize
    def test_raw_response_retrieve_all(self, client: Ngc) -> None:
        response = client.orgs.metering.with_raw_response.retrieve_all(
            org_name="org-name",
            q={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metering = response.parse()
        assert_matches_type(MeteringResultList, metering, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_all(self, client: Ngc) -> None:
        with client.orgs.metering.with_streaming_response.retrieve_all(
            org_name="org-name",
            q={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metering = response.parse()
            assert_matches_type(MeteringResultList, metering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_all(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.metering.with_raw_response.retrieve_all(
                org_name="",
                q={},
            )


class TestAsyncMetering:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncNgc) -> None:
        metering = await async_client.orgs.metering.retrieve_all(
            org_name="org-name",
            q={},
        )
        assert_matches_type(MeteringResultList, metering, path=["response"])

    @parametrize
    async def test_method_retrieve_all_with_all_params(self, async_client: AsyncNgc) -> None:
        metering = await async_client.orgs.metering.retrieve_all(
            org_name="org-name",
            q={
                "measurements": [
                    {
                        "fill": 0,
                        "from_date": "fromDate",
                        "group_by": ["string", "string", "string"],
                        "period_in_seconds": 0,
                        "to_date": "toDate",
                        "type": "EGX_GPU_UTILIZATION_DAILY",
                    },
                    {
                        "fill": 0,
                        "from_date": "fromDate",
                        "group_by": ["string", "string", "string"],
                        "period_in_seconds": 0,
                        "to_date": "toDate",
                        "type": "EGX_GPU_UTILIZATION_DAILY",
                    },
                    {
                        "fill": 0,
                        "from_date": "fromDate",
                        "group_by": ["string", "string", "string"],
                        "period_in_seconds": 0,
                        "to_date": "toDate",
                        "type": "EGX_GPU_UTILIZATION_DAILY",
                    },
                ]
            },
        )
        assert_matches_type(MeteringResultList, metering, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.metering.with_raw_response.retrieve_all(
            org_name="org-name",
            q={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metering = await response.parse()
        assert_matches_type(MeteringResultList, metering, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.metering.with_streaming_response.retrieve_all(
            org_name="org-name",
            q={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metering = await response.parse()
            assert_matches_type(MeteringResultList, metering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_all(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.metering.with_raw_response.retrieve_all(
                org_name="",
                q={},
            )
