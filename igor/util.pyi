from __future__ import annotations
from _typeshed import Incomplete
from ._typing import BYTEORDER


def hex_bytes(buffer: Incomplete, spaces: int | None = ...) -> str:
    ...


def assert_null(buffer: Incomplete, strict: bool = ...) -> None:
    ...


def byte_order(needToReorderBytes: bool) -> BYTEORDER:
    ...


def need_to_reorder_bytes(version: int) -> bool:
    ...


def checksum(
    buffer: Incomplete, byte_order: BYTEORDER, oldcksum: int, numbytes: int
) -> int:
    ...
