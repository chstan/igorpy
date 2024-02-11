from __future__ import annotations
from .base import Record as Record
from .._typing import IBW, BYTEORDER

class WaveRecord(Record):
    wave: IBW

    def __init__(
        self,
        *args: dict[str, int] | bytes | BYTEORDER,
        **kwargs: dict[str, int] | bytes | BYTEORDER,
    ) -> None: ...
