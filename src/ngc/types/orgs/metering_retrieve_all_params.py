# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MeteringRetrieveAllParams", "Q", "QMeasurement"]


class MeteringRetrieveAllParams(TypedDict, total=False):
    q: Required[Q]
    """request params for getting metering usage"""


class QMeasurement(TypedDict, total=False):
    fill: float
    """
    this replaces all null values in an output stream with a non-null value that is
    provided.
    """

    from_date: Annotated[str, PropertyInfo(alias="fromDate")]
    """end time range for the data, in ISO formate, yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"""

    group_by: Annotated[List[str], PropertyInfo(alias="groupBy")]
    """group by specific tags"""

    period_in_seconds: Annotated[float, PropertyInfo(alias="periodInSeconds")]
    """time period to aggregate the data over with, in seconds.

    If none provided, raw data will be returned.
    """

    to_date: Annotated[str, PropertyInfo(alias="toDate")]
    """start time range for the data, in ISO formate, yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"""

    type: Literal[
        "EGX_GPU_UTILIZATION_DAILY",
        "FLEET_COMMAND_GPU_UTILIZATION_DAILY",
        "EGX_LOG_STORAGE_UTILIZATION_DAILY",
        "FLEET_COMMAND_LOG_STORAGE_UTILIZATION_DAILY",
        "REGISTRY_STORAGE_UTILIZATION_DAILY",
        "EGX_GPU_UTILIZATION_MONTHLY",
        "FLEET_COMMAND_GPU_UTILIZATION_MONTHLY",
        "EGX_LOG_STORAGE_UTILIZATION_MONTHLY",
        "FLEET_COMMAND_LOG_STORAGE_UTILIZATION_MONTHLY",
        "REGISTRY_STORAGE_UTILIZATION_MONTHLY",
    ]


class Q(TypedDict, total=False):
    measurements: Iterable[QMeasurement]
