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


class TestSwaggerResources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        swagger_resource = client.swagger_resources.create()
        assert swagger_resource.is_closed
        assert swagger_resource.json() == {"foo": "bar"}
        assert cast(Any, swagger_resource.is_closed) is True
        assert isinstance(swagger_resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        swagger_resource = client.swagger_resources.with_raw_response.create()

        assert swagger_resource.is_closed is True
        assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert swagger_resource.json() == {"foo": "bar"}
        assert isinstance(swagger_resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.swagger_resources.with_streaming_response.create() as swagger_resource:
            assert not swagger_resource.is_closed
            assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert swagger_resource.json() == {"foo": "bar"}
            assert cast(Any, swagger_resource.is_closed) is True
            assert isinstance(swagger_resource, StreamedBinaryAPIResponse)

        assert cast(Any, swagger_resource.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        swagger_resource = client.swagger_resources.update()
        assert swagger_resource.is_closed
        assert swagger_resource.json() == {"foo": "bar"}
        assert cast(Any, swagger_resource.is_closed) is True
        assert isinstance(swagger_resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        swagger_resource = client.swagger_resources.with_raw_response.update()

        assert swagger_resource.is_closed is True
        assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert swagger_resource.json() == {"foo": "bar"}
        assert isinstance(swagger_resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.swagger_resources.with_streaming_response.update() as swagger_resource:
            assert not swagger_resource.is_closed
            assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert swagger_resource.json() == {"foo": "bar"}
            assert cast(Any, swagger_resource.is_closed) is True
            assert isinstance(swagger_resource, StreamedBinaryAPIResponse)

        assert cast(Any, swagger_resource.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        swagger_resource = client.swagger_resources.delete()
        assert swagger_resource.is_closed
        assert swagger_resource.json() == {"foo": "bar"}
        assert cast(Any, swagger_resource.is_closed) is True
        assert isinstance(swagger_resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        swagger_resource = client.swagger_resources.with_raw_response.delete()

        assert swagger_resource.is_closed is True
        assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert swagger_resource.json() == {"foo": "bar"}
        assert isinstance(swagger_resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.swagger_resources.with_streaming_response.delete() as swagger_resource:
            assert not swagger_resource.is_closed
            assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert swagger_resource.json() == {"foo": "bar"}
            assert cast(Any, swagger_resource.is_closed) is True
            assert isinstance(swagger_resource, StreamedBinaryAPIResponse)

        assert cast(Any, swagger_resource.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        swagger_resource = client.swagger_resources.retrieve_all()
        assert swagger_resource.is_closed
        assert swagger_resource.json() == {"foo": "bar"}
        assert cast(Any, swagger_resource.is_closed) is True
        assert isinstance(swagger_resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        swagger_resource = client.swagger_resources.with_raw_response.retrieve_all()

        assert swagger_resource.is_closed is True
        assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert swagger_resource.json() == {"foo": "bar"}
        assert isinstance(swagger_resource, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_all(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.swagger_resources.with_streaming_response.retrieve_all() as swagger_resource:
            assert not swagger_resource.is_closed
            assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert swagger_resource.json() == {"foo": "bar"}
            assert cast(Any, swagger_resource.is_closed) is True
            assert isinstance(swagger_resource, StreamedBinaryAPIResponse)

        assert cast(Any, swagger_resource.is_closed) is True


class TestAsyncSwaggerResources:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        swagger_resource = await async_client.swagger_resources.create()
        assert swagger_resource.is_closed
        assert await swagger_resource.json() == {"foo": "bar"}
        assert cast(Any, swagger_resource.is_closed) is True
        assert isinstance(swagger_resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        swagger_resource = await async_client.swagger_resources.with_raw_response.create()

        assert swagger_resource.is_closed is True
        assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await swagger_resource.json() == {"foo": "bar"}
        assert isinstance(swagger_resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.swagger_resources.with_streaming_response.create() as swagger_resource:
            assert not swagger_resource.is_closed
            assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await swagger_resource.json() == {"foo": "bar"}
            assert cast(Any, swagger_resource.is_closed) is True
            assert isinstance(swagger_resource, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, swagger_resource.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        swagger_resource = await async_client.swagger_resources.update()
        assert swagger_resource.is_closed
        assert await swagger_resource.json() == {"foo": "bar"}
        assert cast(Any, swagger_resource.is_closed) is True
        assert isinstance(swagger_resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        swagger_resource = await async_client.swagger_resources.with_raw_response.update()

        assert swagger_resource.is_closed is True
        assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await swagger_resource.json() == {"foo": "bar"}
        assert isinstance(swagger_resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.swagger_resources.with_streaming_response.update() as swagger_resource:
            assert not swagger_resource.is_closed
            assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await swagger_resource.json() == {"foo": "bar"}
            assert cast(Any, swagger_resource.is_closed) is True
            assert isinstance(swagger_resource, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, swagger_resource.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        swagger_resource = await async_client.swagger_resources.delete()
        assert swagger_resource.is_closed
        assert await swagger_resource.json() == {"foo": "bar"}
        assert cast(Any, swagger_resource.is_closed) is True
        assert isinstance(swagger_resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        swagger_resource = await async_client.swagger_resources.with_raw_response.delete()

        assert swagger_resource.is_closed is True
        assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await swagger_resource.json() == {"foo": "bar"}
        assert isinstance(swagger_resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.swagger_resources.with_streaming_response.delete() as swagger_resource:
            assert not swagger_resource.is_closed
            assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await swagger_resource.json() == {"foo": "bar"}
            assert cast(Any, swagger_resource.is_closed) is True
            assert isinstance(swagger_resource, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, swagger_resource.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        swagger_resource = await async_client.swagger_resources.retrieve_all()
        assert swagger_resource.is_closed
        assert await swagger_resource.json() == {"foo": "bar"}
        assert cast(Any, swagger_resource.is_closed) is True
        assert isinstance(swagger_resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        swagger_resource = await async_client.swagger_resources.with_raw_response.retrieve_all()

        assert swagger_resource.is_closed is True
        assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await swagger_resource.json() == {"foo": "bar"}
        assert isinstance(swagger_resource, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_all(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.swagger_resources.with_streaming_response.retrieve_all() as swagger_resource:
            assert not swagger_resource.is_closed
            assert swagger_resource.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await swagger_resource.json() == {"foo": "bar"}
            assert cast(Any, swagger_resource.is_closed) is True
            assert isinstance(swagger_resource, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, swagger_resource.is_closed) is True
