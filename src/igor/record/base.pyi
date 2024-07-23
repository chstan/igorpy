from __future__ import annotations

from .._typing import BYTEORDER

class Record:
    header: dict[str, int]
    data: bytes
    byte_order: BYTEORDER | None

    def __init__(
        self,
        header: dict[str, int],
        data: bytes,
        byte_order: BYTEORDER = ...,
    ) -> None: ...

class UnknownRecord(Record): ...
class UnusedRecord(Record): ...

class TextRecord(Record):
    text: bytes
    null_terminated_text: str

    def __init__(
        self,
        *args: dict[str, int] | bytes | BYTEORDER,
        **kwargs: dict[str, int] | bytes | BYTEORDER,
    ) -> None: ...
