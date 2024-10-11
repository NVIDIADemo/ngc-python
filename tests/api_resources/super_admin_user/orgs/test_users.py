# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.types.shared import User
from ngc.types.super_admin_user.orgs import UserRemoveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ngc) -> None:
        user = client.super_admin_user.orgs.users.create(
            org_name="org-name",
            email="xxxxxx",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Ngc) -> None:
        user = client.super_admin_user.orgs.users.create(
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
        response = client.super_admin_user.orgs.users.with_raw_response.create(
            org_name="org-name",
            email="xxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ngc) -> None:
        with client.super_admin_user.orgs.users.with_streaming_response.create(
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
            client.super_admin_user.orgs.users.with_raw_response.create(
                org_name="",
                email="xxxxxx",
            )

    @parametrize
    def test_method_add(self, client: Ngc) -> None:
        user = client.super_admin_user.orgs.users.add(
            id="id",
            org_name="org-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Ngc) -> None:
        user = client.super_admin_user.orgs.users.add(
            id="id",
            org_name="org-name",
            user_role_defaults_to_registry_read="user role, defaults to REGISTRY_READ",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Ngc) -> None:
        response = client.super_admin_user.orgs.users.with_raw_response.add(
            id="id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Ngc) -> None:
        with client.super_admin_user.orgs.users.with_streaming_response.add(
            id="id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.super_admin_user.orgs.users.with_raw_response.add(
                id="id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.super_admin_user.orgs.users.with_raw_response.add(
                id="",
                org_name="org-name",
            )

    @parametrize
    def test_method_remove(self, client: Ngc) -> None:
        user = client.super_admin_user.orgs.users.remove(
            id="id",
            org_name="org-name",
        )
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Ngc) -> None:
        response = client.super_admin_user.orgs.users.with_raw_response.remove(
            id="id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Ngc) -> None:
        with client.super_admin_user.orgs.users.with_streaming_response.remove(
            id="id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRemoveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.super_admin_user.orgs.users.with_raw_response.remove(
                id="id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.super_admin_user.orgs.users.with_raw_response.remove(
                id="",
                org_name="org-name",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNgc) -> None:
        user = await async_client.super_admin_user.orgs.users.create(
            org_name="org-name",
            email="xxxxxx",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.super_admin_user.orgs.users.create(
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
        response = await async_client.super_admin_user.orgs.users.with_raw_response.create(
            org_name="org-name",
            email="xxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNgc) -> None:
        async with async_client.super_admin_user.orgs.users.with_streaming_response.create(
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
            await async_client.super_admin_user.orgs.users.with_raw_response.create(
                org_name="",
                email="xxxxxx",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncNgc) -> None:
        user = await async_client.super_admin_user.orgs.users.add(
            id="id",
            org_name="org-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.super_admin_user.orgs.users.add(
            id="id",
            org_name="org-name",
            user_role_defaults_to_registry_read="user role, defaults to REGISTRY_READ",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncNgc) -> None:
        response = await async_client.super_admin_user.orgs.users.with_raw_response.add(
            id="id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncNgc) -> None:
        async with async_client.super_admin_user.orgs.users.with_streaming_response.add(
            id="id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.super_admin_user.orgs.users.with_raw_response.add(
                id="id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.super_admin_user.orgs.users.with_raw_response.add(
                id="",
                org_name="org-name",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncNgc) -> None:
        user = await async_client.super_admin_user.orgs.users.remove(
            id="id",
            org_name="org-name",
        )
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncNgc) -> None:
        response = await async_client.super_admin_user.orgs.users.with_raw_response.remove(
            id="id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncNgc) -> None:
        async with async_client.super_admin_user.orgs.users.with_streaming_response.remove(
            id="id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRemoveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.super_admin_user.orgs.users.with_raw_response.remove(
                id="id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.super_admin_user.orgs.users.with_raw_response.remove(
                id="",
                org_name="org-name",
            )
