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


class TestUi:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        ui = client.swagger_resources.configuration.ui.create()
        assert ui.is_closed
        assert ui.json() == {"foo": "bar"}
        assert cast(Any, ui.is_closed) is True
        assert isinstance(ui, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        ui = client.swagger_resources.configuration.ui.with_raw_response.create()

        assert ui.is_closed is True
        assert ui.http_request.headers.get("X-Stainless-Lang") == "python"
        assert ui.json() == {"foo": "bar"}
        assert isinstance(ui, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.swagger_resources.configuration.ui.with_streaming_response.create() as ui:
            assert not ui.is_closed
            assert ui.http_request.headers.get("X-Stainless-Lang") == "python"

            assert ui.json() == {"foo": "bar"}
            assert cast(Any, ui.is_closed) is True
            assert isinstance(ui, StreamedBinaryAPIResponse)

        assert cast(Any, ui.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        ui = client.swagger_resources.configuration.ui.retrieve()
        assert ui.is_closed
        assert ui.json() == {"foo": "bar"}
        assert cast(Any, ui.is_closed) is True
        assert isinstance(ui, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        ui = client.swagger_resources.configuration.ui.with_raw_response.retrieve()

        assert ui.is_closed is True
        assert ui.http_request.headers.get("X-Stainless-Lang") == "python"
        assert ui.json() == {"foo": "bar"}
        assert isinstance(ui, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.swagger_resources.configuration.ui.with_streaming_response.retrieve() as ui:
            assert not ui.is_closed
            assert ui.http_request.headers.get("X-Stainless-Lang") == "python"

            assert ui.json() == {"foo": "bar"}
            assert cast(Any, ui.is_closed) is True
            assert isinstance(ui, StreamedBinaryAPIResponse)

        assert cast(Any, ui.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        ui = client.swagger_resources.configuration.ui.update()
        assert ui.is_closed
        assert ui.json() == {"foo": "bar"}
        assert cast(Any, ui.is_closed) is True
        assert isinstance(ui, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        ui = client.swagger_resources.configuration.ui.with_raw_response.update()

        assert ui.is_closed is True
        assert ui.http_request.headers.get("X-Stainless-Lang") == "python"
        assert ui.json() == {"foo": "bar"}
        assert isinstance(ui, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.swagger_resources.configuration.ui.with_streaming_response.update() as ui:
            assert not ui.is_closed
            assert ui.http_request.headers.get("X-Stainless-Lang") == "python"

            assert ui.json() == {"foo": "bar"}
            assert cast(Any, ui.is_closed) is True
            assert isinstance(ui, StreamedBinaryAPIResponse)

        assert cast(Any, ui.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        ui = client.swagger_resources.configuration.ui.delete()
        assert ui.is_closed
        assert ui.json() == {"foo": "bar"}
        assert cast(Any, ui.is_closed) is True
        assert isinstance(ui, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        ui = client.swagger_resources.configuration.ui.with_raw_response.delete()

        assert ui.is_closed is True
        assert ui.http_request.headers.get("X-Stainless-Lang") == "python"
        assert ui.json() == {"foo": "bar"}
        assert isinstance(ui, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_delete(self, client: Ngc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.swagger_resources.configuration.ui.with_streaming_response.delete() as ui:
            assert not ui.is_closed
            assert ui.http_request.headers.get("X-Stainless-Lang") == "python"

            assert ui.json() == {"foo": "bar"}
            assert cast(Any, ui.is_closed) is True
            assert isinstance(ui, StreamedBinaryAPIResponse)

        assert cast(Any, ui.is_closed) is True


class TestAsyncUi:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        ui = await async_client.swagger_resources.configuration.ui.create()
        assert ui.is_closed
        assert await ui.json() == {"foo": "bar"}
        assert cast(Any, ui.is_closed) is True
        assert isinstance(ui, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        ui = await async_client.swagger_resources.configuration.ui.with_raw_response.create()

        assert ui.is_closed is True
        assert ui.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await ui.json() == {"foo": "bar"}
        assert isinstance(ui, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.post("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.swagger_resources.configuration.ui.with_streaming_response.create() as ui:
            assert not ui.is_closed
            assert ui.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await ui.json() == {"foo": "bar"}
            assert cast(Any, ui.is_closed) is True
            assert isinstance(ui, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, ui.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        ui = await async_client.swagger_resources.configuration.ui.retrieve()
        assert ui.is_closed
        assert await ui.json() == {"foo": "bar"}
        assert cast(Any, ui.is_closed) is True
        assert isinstance(ui, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        ui = await async_client.swagger_resources.configuration.ui.with_raw_response.retrieve()

        assert ui.is_closed is True
        assert ui.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await ui.json() == {"foo": "bar"}
        assert isinstance(ui, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.get("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.swagger_resources.configuration.ui.with_streaming_response.retrieve() as ui:
            assert not ui.is_closed
            assert ui.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await ui.json() == {"foo": "bar"}
            assert cast(Any, ui.is_closed) is True
            assert isinstance(ui, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, ui.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        ui = await async_client.swagger_resources.configuration.ui.update()
        assert ui.is_closed
        assert await ui.json() == {"foo": "bar"}
        assert cast(Any, ui.is_closed) is True
        assert isinstance(ui, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        ui = await async_client.swagger_resources.configuration.ui.with_raw_response.update()

        assert ui.is_closed is True
        assert ui.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await ui.json() == {"foo": "bar"}
        assert isinstance(ui, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.patch("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.swagger_resources.configuration.ui.with_streaming_response.update() as ui:
            assert not ui.is_closed
            assert ui.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await ui.json() == {"foo": "bar"}
            assert cast(Any, ui.is_closed) is True
            assert isinstance(ui, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, ui.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        ui = await async_client.swagger_resources.configuration.ui.delete()
        assert ui.is_closed
        assert await ui.json() == {"foo": "bar"}
        assert cast(Any, ui.is_closed) is True
        assert isinstance(ui, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        ui = await async_client.swagger_resources.configuration.ui.with_raw_response.delete()

        assert ui.is_closed is True
        assert ui.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await ui.json() == {"foo": "bar"}
        assert isinstance(ui, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_delete(self, async_client: AsyncNgc, respx_mock: MockRouter) -> None:
        respx_mock.delete("/swagger-resources/configuration/ui").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.swagger_resources.configuration.ui.with_streaming_response.delete() as ui:
            assert not ui.is_closed
            assert ui.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await ui.json() == {"foo": "bar"}
            assert cast(Any, ui.is_closed) is True
            assert isinstance(ui, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, ui.is_closed) is True
