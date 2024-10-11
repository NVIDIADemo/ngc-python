# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["GpupeakRetrieveAllParams", "TheToDateInISO8601FormatIncludingTimeZoneInformationYyyyMmDdTHhMmSS"]


class GpupeakRetrieveAllParams(TypedDict, total=False):
    the_to_date_in_iso_8601_format_including_time_zone_information_yyyy_mm_dd_t_hh_mm_ss: Annotated[
        TheToDateInISO8601FormatIncludingTimeZoneInformationYyyyMmDdTHhMmSS,
        PropertyInfo(alias="The to date in ISO 8601 format including time zone information (yyyy-MM-dd'T'HH:mm:ss"),
    ]


class TheToDateInISO8601FormatIncludingTimeZoneInformationYyyyMmDdTHhMmSS(TypedDict, total=False):
    sssz: Annotated[Union[str, datetime], PropertyInfo(alias="SSSZ)", format="iso8601")]
