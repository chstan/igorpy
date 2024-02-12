from __future__ import annotations
from typing import BinaryIO, NoReturn
from . import LOG as LOG
from .struct import DynamicField, DynamicStructure, Structure
from _typeshed import Incomplete
from pathlib import Path
from numpy.typing import DTypeLike
from ._typing import IBW, BYTEORDER

complexInt8: DTypeLike
complexInt16: DTypeLike
complexInt32: DTypeLike
complexUInt8: DTypeLike
complexUInt16: DTypeLike
complexUInt32: DTypeLike


class StaticStringField(DynamicField):
    def __init__(
        self, *args: str | Structure | int, **kwargs: str | int | bool
    ) -> None:
        ...

    def post_unpack(self, parents: type, data: bytes) -> None:
        ...


class NullStaticStringField(StaticStringField):
    ...


TYPE_TABLE: dict[int, DTypeLike]
MAXDIMS: int
BinHeader1: Structure
BinHeader2: Structure
BinHeader3: Structure
BinHeader5: Structure
MAX_WAVE_NAME2: int
MAX_WAVE_NAME5: int
MAX_UNIT_CHARS: int
WaveHeader2: DynamicStructure
WaveHeader5: DynamicStructure


class DynamicWaveDataField1(DynamicField):
    def pre_pack(self, parents: type, data: bytes) -> None:
        ...

    count: Incomplete
    data_size: Incomplete
    shape: Incomplete
    dtype: Incomplete

    def pre_unpack(self, parents: type, data: bytes) -> None:
        ...

    def unpack(self, stream: BinaryIO):
        ...


class DynamicWaveDataField5(DynamicWaveDataField1):
    ...


class DynamicStringField(StaticStringField):
    counts: Incomplete
    count: Incomplete

    def pre_unpack(self, parents: type, data: bytes) -> None:
        ...


class DynamicWaveNoteField(DynamicStringField):
    ...


class DynamicDependencyFormulaField(DynamicStringField):
    ...


class DynamicDataUnitsField(DynamicStringField):
    ...


class DynamicDimensionUnitsField(DynamicStringField):
    ...


class DynamicLabelsField(DynamicStringField):
    def post_unpack(self, parents: type, data: bytes) -> None:
        ...


class DynamicStringIndicesDataField(DynamicField):
    def pre_pack(self, parents: type, data: bytes) -> None:
        ...

    string_indices_size: Incomplete
    count: Incomplete

    def pre_unpack(self, parents: type, data: bytes) -> None:
        ...

    def post_unpack(self, parents: type, data: bytes) -> None:
        ...


class DynamicVersionField(DynamicField):
    def pre_pack(self, parents: type, byte_order: BYTEORDER) -> NoReturn:
        ...

    def post_unpack(self, parents: type, data: bytes):
        ...


class DynamicWaveField(DynamicField):
    def post_unpack(self, parents: type, data: bytes) -> None:
        ...


Wave1: DynamicStructure
Wave2: DynamicStructure
Wave3: DynamicStructure
Wave5: DynamicStructure
Wave: DynamicStructure


def load(filename: str | Path) -> IBW:
    ...


def save(filename: str) -> None:
    ...
