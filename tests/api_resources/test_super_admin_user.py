# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from ngc.types import SuperAdminUserCRMSyncResponse
from tests.utils import assert_matches_type
from ngc.types.shared import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuperAdminUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_crm_sync(self, client: Ngc) -> None:
        super_admin_user = client.super_admin_user.crm_sync(
            0,
        )
        assert_matches_type(SuperAdminUserCRMSyncResponse, super_admin_user, path=["response"])

    @parametrize
    def test_raw_response_crm_sync(self, client: Ngc) -> None:
        response = client.super_admin_user.with_raw_response.crm_sync(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        super_admin_user = response.parse()
        assert_matches_type(SuperAdminUserCRMSyncResponse, super_admin_user, path=["response"])

    @parametrize
    def test_streaming_response_crm_sync(self, client: Ngc) -> None:
        with client.super_admin_user.with_streaming_response.crm_sync(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            super_admin_user = response.parse()
            assert_matches_type(SuperAdminUserCRMSyncResponse, super_admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_migrate_deprecated_roles(self, client: Ngc) -> None:
        super_admin_user = client.super_admin_user.migrate_deprecated_roles(
            "id",
        )
        assert_matches_type(User, super_admin_user, path=["response"])

    @parametrize
    def test_raw_response_migrate_deprecated_roles(self, client: Ngc) -> None:
        response = client.super_admin_user.with_raw_response.migrate_deprecated_roles(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        super_admin_user = response.parse()
        assert_matches_type(User, super_admin_user, path=["response"])

    @parametrize
    def test_streaming_response_migrate_deprecated_roles(self, client: Ngc) -> None:
        with client.super_admin_user.with_streaming_response.migrate_deprecated_roles(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            super_admin_user = response.parse()
            assert_matches_type(User, super_admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_migrate_deprecated_roles(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.super_admin_user.with_raw_response.migrate_deprecated_roles(
                "",
            )


class TestAsyncSuperAdminUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_crm_sync(self, async_client: AsyncNgc) -> None:
        super_admin_user = await async_client.super_admin_user.crm_sync(
            0,
        )
        assert_matches_type(SuperAdminUserCRMSyncResponse, super_admin_user, path=["response"])

    @parametrize
    async def test_raw_response_crm_sync(self, async_client: AsyncNgc) -> None:
        response = await async_client.super_admin_user.with_raw_response.crm_sync(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        super_admin_user = await response.parse()
        assert_matches_type(SuperAdminUserCRMSyncResponse, super_admin_user, path=["response"])

    @parametrize
    async def test_streaming_response_crm_sync(self, async_client: AsyncNgc) -> None:
        async with async_client.super_admin_user.with_streaming_response.crm_sync(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            super_admin_user = await response.parse()
            assert_matches_type(SuperAdminUserCRMSyncResponse, super_admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_migrate_deprecated_roles(self, async_client: AsyncNgc) -> None:
        super_admin_user = await async_client.super_admin_user.migrate_deprecated_roles(
            "id",
        )
        assert_matches_type(User, super_admin_user, path=["response"])

    @parametrize
    async def test_raw_response_migrate_deprecated_roles(self, async_client: AsyncNgc) -> None:
        response = await async_client.super_admin_user.with_raw_response.migrate_deprecated_roles(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        super_admin_user = await response.parse()
        assert_matches_type(User, super_admin_user, path=["response"])

    @parametrize
    async def test_streaming_response_migrate_deprecated_roles(self, async_client: AsyncNgc) -> None:
        async with async_client.super_admin_user.with_streaming_response.migrate_deprecated_roles(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            super_admin_user = await response.parse()
            assert_matches_type(User, super_admin_user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_migrate_deprecated_roles(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.super_admin_user.with_raw_response.migrate_deprecated_roles(
                "",
            )
