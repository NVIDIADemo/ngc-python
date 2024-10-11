# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ngc import Ngc, AsyncNgc
from tests.utils import assert_matches_type
from ngc.pagination import SyncPageNumberUsers, AsyncPageNumberUsers
from ngc.types.orgs import (
    UserListResponse,
    UserDeleteResponse,
)
from ngc.types.shared import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ngc) -> None:
        user = client.orgs.users.create(
            org_name="org-name",
            email="xxxxxx",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Ngc) -> None:
        user = client.orgs.users.create(
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
        response = client.orgs.users.with_raw_response.create(
            org_name="org-name",
            email="xxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ngc) -> None:
        with client.orgs.users.with_streaming_response.create(
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
            client.orgs.users.with_raw_response.create(
                org_name="",
                email="xxxxxx",
            )

    @parametrize
    def test_method_list(self, client: Ngc) -> None:
        user = client.orgs.users.list(
            org_name="org-name",
        )
        assert_matches_type(SyncPageNumberUsers[UserListResponse], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Ngc) -> None:
        user = client.orgs.users.list(
            org_name="org-name",
            exclude_from_team="exclude-from-team",
            page_number=0,
            page_size=0,
            q={
                "fields": ["string", "string", "string"],
                "filters": [
                    {
                        "field": "field",
                        "value": "value",
                    },
                    {
                        "field": "field",
                        "value": "value",
                    },
                    {
                        "field": "field",
                        "value": "value",
                    },
                ],
                "group_by": "groupBy",
                "order_by": [
                    {
                        "field": "field",
                        "value": "ASC",
                    },
                    {
                        "field": "field",
                        "value": "ASC",
                    },
                    {
                        "field": "field",
                        "value": "ASC",
                    },
                ],
                "page": 0,
                "page_size": 0,
                "query": "query",
                "query_fields": ["string", "string", "string"],
                "scored_size": 0,
            },
        )
        assert_matches_type(SyncPageNumberUsers[UserListResponse], user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Ngc) -> None:
        response = client.orgs.users.with_raw_response.list(
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncPageNumberUsers[UserListResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Ngc) -> None:
        with client.orgs.users.with_streaming_response.list(
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncPageNumberUsers[UserListResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.users.with_raw_response.list(
                org_name="",
            )

    @parametrize
    def test_method_delete(self, client: Ngc) -> None:
        user = client.orgs.users.delete(
            id="id",
            org_name="org-name",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Ngc) -> None:
        user = client.orgs.users.delete(
            id="id",
            org_name="org-name",
            anonymize=True,
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Ngc) -> None:
        response = client.orgs.users.with_raw_response.delete(
            id="id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Ngc) -> None:
        with client.orgs.users.with_streaming_response.delete(
            id="id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.users.with_raw_response.delete(
                id="id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.orgs.users.with_raw_response.delete(
                id="",
                org_name="org-name",
            )

    @parametrize
    def test_method_add_role(self, client: Ngc) -> None:
        user = client.orgs.users.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_add_role(self, client: Ngc) -> None:
        response = client.orgs.users.with_raw_response.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            roles=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_add_role(self, client: Ngc) -> None:
        with client.orgs.users.with_streaming_response.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
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
            client.orgs.users.with_raw_response.add_role(
                user_email_or_id="user-email-or-id",
                org_name="",
                roles=["string", "string", "string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_email_or_id` but received ''"):
            client.orgs.users.with_raw_response.add_role(
                user_email_or_id="",
                org_name="org-name",
                roles=["string", "string", "string"],
            )

    @parametrize
    def test_method_remove_role(self, client: Ngc) -> None:
        user = client.orgs.users.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_remove_role_with_all_params(self, client: Ngc) -> None:
        user = client.orgs.users.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_remove_role(self, client: Ngc) -> None:
        response = client.orgs.users.with_raw_response.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_remove_role(self, client: Ngc) -> None:
        with client.orgs.users.with_streaming_response.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_role(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.users.with_raw_response.remove_role(
                user_email_or_id="user-email-or-id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_email_or_id` but received ''"):
            client.orgs.users.with_raw_response.remove_role(
                user_email_or_id="",
                org_name="org-name",
            )

    @parametrize
    def test_method_update_role(self, client: Ngc) -> None:
        user = client.orgs.users.update_role(
            id="id",
            org_name="org-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_update_role_with_all_params(self, client: Ngc) -> None:
        user = client.orgs.users.update_role(
            id="id",
            org_name="org-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_update_role(self, client: Ngc) -> None:
        response = client.orgs.users.with_raw_response.update_role(
            id="id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_update_role(self, client: Ngc) -> None:
        with client.orgs.users.with_streaming_response.update_role(
            id="id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_role(self, client: Ngc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            client.orgs.users.with_raw_response.update_role(
                id="id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.orgs.users.with_raw_response.update_role(
                id="",
                org_name="org-name",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.create(
            org_name="org-name",
            email="xxxxxx",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.create(
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
        response = await async_client.orgs.users.with_raw_response.create(
            org_name="org-name",
            email="xxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.users.with_streaming_response.create(
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
            await async_client.orgs.users.with_raw_response.create(
                org_name="",
                email="xxxxxx",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.list(
            org_name="org-name",
        )
        assert_matches_type(AsyncPageNumberUsers[UserListResponse], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.list(
            org_name="org-name",
            exclude_from_team="exclude-from-team",
            page_number=0,
            page_size=0,
            q={
                "fields": ["string", "string", "string"],
                "filters": [
                    {
                        "field": "field",
                        "value": "value",
                    },
                    {
                        "field": "field",
                        "value": "value",
                    },
                    {
                        "field": "field",
                        "value": "value",
                    },
                ],
                "group_by": "groupBy",
                "order_by": [
                    {
                        "field": "field",
                        "value": "ASC",
                    },
                    {
                        "field": "field",
                        "value": "ASC",
                    },
                    {
                        "field": "field",
                        "value": "ASC",
                    },
                ],
                "page": 0,
                "page_size": 0,
                "query": "query",
                "query_fields": ["string", "string", "string"],
                "scored_size": 0,
            },
        )
        assert_matches_type(AsyncPageNumberUsers[UserListResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.users.with_raw_response.list(
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncPageNumberUsers[UserListResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.users.with_streaming_response.list(
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncPageNumberUsers[UserListResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.users.with_raw_response.list(
                org_name="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.delete(
            id="id",
            org_name="org-name",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.delete(
            id="id",
            org_name="org-name",
            anonymize=True,
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.users.with_raw_response.delete(
            id="id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.users.with_streaming_response.delete(
            id="id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.users.with_raw_response.delete(
                id="id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.orgs.users.with_raw_response.delete(
                id="",
                org_name="org-name",
            )

    @parametrize
    async def test_method_add_role(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_add_role(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.users.with_raw_response.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            roles=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_add_role(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.users.with_streaming_response.add_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
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
            await async_client.orgs.users.with_raw_response.add_role(
                user_email_or_id="user-email-or-id",
                org_name="",
                roles=["string", "string", "string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_email_or_id` but received ''"):
            await async_client.orgs.users.with_raw_response.add_role(
                user_email_or_id="",
                org_name="org-name",
                roles=["string", "string", "string"],
            )

    @parametrize
    async def test_method_remove_role(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_remove_role_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_remove_role(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.users.with_raw_response.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_remove_role(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.users.with_streaming_response.remove_role(
            user_email_or_id="user-email-or-id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_role(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.users.with_raw_response.remove_role(
                user_email_or_id="user-email-or-id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_email_or_id` but received ''"):
            await async_client.orgs.users.with_raw_response.remove_role(
                user_email_or_id="",
                org_name="org-name",
            )

    @parametrize
    async def test_method_update_role(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.update_role(
            id="id",
            org_name="org-name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_update_role_with_all_params(self, async_client: AsyncNgc) -> None:
        user = await async_client.orgs.users.update_role(
            id="id",
            org_name="org-name",
            roles=["string", "string", "string"],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_update_role(self, async_client: AsyncNgc) -> None:
        response = await async_client.orgs.users.with_raw_response.update_role(
            id="id",
            org_name="org-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_update_role(self, async_client: AsyncNgc) -> None:
        async with async_client.orgs.users.with_streaming_response.update_role(
            id="id",
            org_name="org-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_role(self, async_client: AsyncNgc) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_name` but received ''"):
            await async_client.orgs.users.with_raw_response.update_role(
                id="id",
                org_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.orgs.users.with_raw_response.update_role(
                id="",
                org_name="org-name",
            )
