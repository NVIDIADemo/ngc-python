# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "MeteringResultList",
    "Measurement",
    "MeasurementSery",
    "MeasurementSeryTag",
    "MeasurementSeryValue",
    "RequestStatus",
]


class MeasurementSeryTag(BaseModel):
    tag_key: Optional[str] = FieldInfo(alias="tagKey", default=None)
    """key for the tag, ie)host, job_id, gpu_id"""

    tag_value: Optional[str] = FieldInfo(alias="tagValue", default=None)
    """value for the tag, ie)host=foo, job_id=bar, gpu_id=racecar"""


class MeasurementSeryValue(BaseModel):
    value: Optional[List[str]] = None
    """list of values, in the same order as columns"""


class MeasurementSery(BaseModel):
    columns: Optional[List[str]] = None
    """list of columns, in order, for the series."""

    name: Optional[str] = None
    """name for the measurement"""

    tags: Optional[List[MeasurementSeryTag]] = None
    """list of tags identifying the series."""

    values: Optional[List[MeasurementSeryValue]] = None
    """array of values, in the same order as the columns, for the series."""


class Measurement(BaseModel):
    series: Optional[List[MeasurementSery]] = None
    """array of series within a measurement"""


class RequestStatus(BaseModel):
    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)

    server_id: Optional[str] = FieldInfo(alias="serverId", default=None)

    status_code: Optional[
        Literal[
            "UNKNOWN",
            "SUCCESS",
            "UNAUTHORIZED",
            "PAYMENT_REQUIRED",
            "FORBIDDEN",
            "TIMEOUT",
            "EXISTS",
            "NOT_FOUND",
            "INTERNAL_ERROR",
            "INVALID_REQUEST",
            "INVALID_REQUEST_VERSION",
            "INVALID_REQUEST_DATA",
            "METHOD_NOT_ALLOWED",
            "CONFLICT",
            "UNPROCESSABLE_ENTITY",
            "TOO_MANY_REQUESTS",
            "INSUFFICIENT_STORAGE",
            "SERVICE_UNAVAILABLE",
            "PAYLOAD_TOO_LARGE",
            "NOT_ACCEPTABLE",
            "UNAVAILABLE_FOR_LEGAL_REASONS",
            "BAD_GATEWAY",
        ]
    ] = FieldInfo(alias="statusCode", default=None)
    """Describes response status reported by the server."""

    status_description: Optional[str] = FieldInfo(alias="statusDescription", default=None)


class MeteringResultList(BaseModel):
    measurements: Optional[List[Measurement]] = None

    request_status: Optional[RequestStatus] = FieldInfo(alias="requestStatus", default=None)
