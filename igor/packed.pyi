from __future__ import annotations
from . import LOG as LOG
from .record import RECORD_TYPE as RECORD_TYPE
from .record.base import UnknownRecord as UnknownRecord, UnusedRecord as UnusedRecord
from .record.folder import (
    FolderEndRecord as FolderEndRecord,
    FolderStartRecord as FolderStartRecord,
)
from .record.variables import VariablesRecord as VariablesRecord
from .record.wave import WaveRecord as WaveRecord
from .struct import Field as Field, Structure as Structure
from _typeshed import Incomplete
from pathlib import Path
from typing import Callable
from typing import Any
from ._typing import RECORDS, BYTEORDER

PackedFileRecordHeader: Incomplete
PACKEDRECTYPE_MASK: int
SUPERCEDED_MASK: int

IGORDATAFOLDER = dict[
    str | bytes, WaveRecord | float | dict[str | bytes, IGORDATAFOLDER]
]

def load(
    filename: str | Path,
    strict: bool = ...,
    ignore_unknown: bool = ...,
    initial_byte_order: BYTEORDER = ...,
) -> tuple[RECORDS, dict[str, IGORDATAFOLDER]]: ...
def walk(
    filesystem: dict[str, IGORDATAFOLDER],
    callback: Callable[[Any], Any],
    dirpath: list[str | Path] | None = ...,
) -> None: ...
