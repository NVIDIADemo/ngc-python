# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrgValidateParams"]


class OrgValidateParams(TypedDict, total=False):
    invitation_token: Required[str]
    """JWT that contains org owner email and proto org identifier"""
