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


class TestSecurity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        security = client.swagger_resources.configuration.security.create()
        assert security.is_closed
        assert security.json() == {"foo": "bar"}
        assert cast(Any, security.is_closed) is True
        assert isinstance(security, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        security = client.swagger_resources.configuration.security.with_raw_response.create()

        assert security.is_closed is True
        assert security.http_request.headers.get("X-Stainless-Lang") == "python"
        assert security.json() == {"foo": "bar"}
        assert isinstance(security, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.swagger_resources.configuration.security.with_streaming_response.create() as security:
            assert not security.is_closed
            assert security.http_request.headers.get("X-Stainless-Lang") == "python"

            assert security.json() == {"foo": "bar"}
            assert cast(Any, security.is_closed) is True
            assert isinstance(security, StreamedBinaryAPIResponse)

        assert cast(Any, security.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        security = client.swagger_resources.configuration.security.retrieve()
        assert security.is_closed
        assert security.json() == {"foo": "bar"}
        assert cast(Any, security.is_closed) is True
        assert isinstance(security, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        security = client.swagger_resources.configuration.security.with_raw_response.retrieve()

        assert security.is_closed is True
        assert security.http_request.headers.get("X-Stainless-Lang") == "python"
        assert security.json() == {"foo": "bar"}
        assert isinstance(security, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.swagger_resources.configuration.security.with_streaming_response.retrieve() as security:
            assert not security.is_closed
            assert security.http_request.headers.get("X-Stainless-Lang") == "python"

            assert security.json() == {"foo": "bar"}
            assert cast(Any, security.is_closed) is True
            assert isinstance(security, StreamedBinaryAPIResponse)

        assert cast(Any, security.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        security = client.swagger_resources.configuration.security.update()
        assert security.is_closed
        assert security.json() == {"foo": "bar"}
        assert cast(Any, security.is_closed) is True
        assert isinstance(security, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        security = client.swagger_resources.configuration.security.with_raw_response.update()

        assert security.is_closed is True
        assert security.http_request.headers.get("X-Stainless-Lang") == "python"
        assert security.json() == {"foo": "bar"}
        assert isinstance(security, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.swagger_resources.configuration.security.with_streaming_response.update() as security:
            assert not security.is_closed
            assert security.http_request.headers.get("X-Stainless-Lang") == "python"

            assert security.json() == {"foo": "bar"}
            assert cast(Any, security.is_closed) is True
            assert isinstance(security, StreamedBinaryAPIResponse)

        assert cast(Any, security.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        security = client.swagger_resources.configuration.security.delete()
        assert security.is_closed
        assert security.json() == {"foo": "bar"}
        assert cast(Any, security.is_closed) is True
        assert isinstance(security, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        security = client.swagger_resources.configuration.security.with_raw_response.delete()

        assert security.is_closed is True
        assert security.http_request.headers.get("X-Stainless-Lang") == "python"
        assert security.json() == {"foo": "bar"}
        assert isinstance(security, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.swagger_resources.configuration.security.with_streaming_response.delete() as security:
            assert not security.is_closed
            assert security.http_request.headers.get("X-Stainless-Lang") == "python"

            assert security.json() == {"foo": "bar"}
            assert cast(Any, security.is_closed) is True
            assert isinstance(security, StreamedBinaryAPIResponse)

        assert cast(Any, security.is_closed) is True


class TestAsyncSecurity:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        security = await async_client.swagger_resources.configuration.security.create()
        assert security.is_closed
        assert await security.json() == {"foo": "bar"}
        assert cast(Any, security.is_closed) is True
        assert isinstance(security, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        security = await async_client.swagger_resources.configuration.security.with_raw_response.create()

        assert security.is_closed is True
        assert security.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await security.json() == {"foo": "bar"}
        assert isinstance(security, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.swagger_resources.configuration.security.with_streaming_response.create() as security:
            assert not security.is_closed
            assert security.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await security.json() == {"foo": "bar"}
            assert cast(Any, security.is_closed) is True
            assert isinstance(security, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, security.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        security = await async_client.swagger_resources.configuration.security.retrieve()
        assert security.is_closed
        assert await security.json() == {"foo": "bar"}
        assert cast(Any, security.is_closed) is True
        assert isinstance(security, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        security = await async_client.swagger_resources.configuration.security.with_raw_response.retrieve()

        assert security.is_closed is True
        assert security.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await security.json() == {"foo": "bar"}
        assert isinstance(security, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.swagger_resources.configuration.security.with_streaming_response.retrieve() as security:
            assert not security.is_closed
            assert security.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await security.json() == {"foo": "bar"}
            assert cast(Any, security.is_closed) is True
            assert isinstance(security, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, security.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        security = await async_client.swagger_resources.configuration.security.update()
        assert security.is_closed
        assert await security.json() == {"foo": "bar"}
        assert cast(Any, security.is_closed) is True
        assert isinstance(security, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        security = await async_client.swagger_resources.configuration.security.with_raw_response.update()

        assert security.is_closed is True
        assert security.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await security.json() == {"foo": "bar"}
        assert isinstance(security, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.swagger_resources.configuration.security.with_streaming_response.update() as security:
            assert not security.is_closed
            assert security.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await security.json() == {"foo": "bar"}
            assert cast(Any, security.is_closed) is True
            assert isinstance(security, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, security.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        security = await async_client.swagger_resources.configuration.security.delete()
        assert security.is_closed
        assert await security.json() == {"foo": "bar"}
        assert cast(Any, security.is_closed) is True
        assert isinstance(security, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        security = await async_client.swagger_resources.configuration.security.with_raw_response.delete()

        assert security.is_closed is True
        assert security.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await security.json() == {"foo": "bar"}
        assert isinstance(security, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/security").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.swagger_resources.configuration.security.with_streaming_response.delete() as security:
            assert not security.is_closed
            assert security.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await security.json() == {"foo": "bar"}
            assert cast(Any, security.is_closed) is True
            assert isinstance(security, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, security.is_closed) is True
