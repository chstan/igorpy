from __future__ import annotations

import struct
from collections.abc import Generator
from typing import BinaryIO

import numpy as np
from _typeshed import Incomplete
from numpy.typing import NDArray

from igor.binarywave import (
    DynamicDataUnitsField,
    DynamicDependencyFormulaField,
    DynamicDimensionUnitsField,
    DynamicLabelsField,
    DynamicStringIndicesDataField,
    DynamicWaveDataField1,
    DynamicWaveDataField5,
    DynamicWaveNoteField,
    NullStaticStringField,
)

from ._typing import BYTEORDER, IBW


class Field:
    format: str | Structure
    name: str
    default: int
    help: str
    count: int
    array: bool

    def __init__(
        self,
        format: str | Structure,
        name: str,
        default: int | None = ...,
        help: str | None = ...,
        count: int = ...,
        array: bool = ...,
    ) -> None:
        ...

    item_count: int
    structure_count: int
    arg_count: int

    def setup(self) -> None:
        ...

    def indexes(self) -> Generator[int, None, None]:
        ...

    def pack_data(
        self,
        data: list[dict[str, complex | NDArray[np.complex_]]]
        | dict[str, complex | NDArray[np.complex_]]
        | None = ...,
    ) -> Generator[Incomplete, None, None]:
        ...

    def pack_item(
        self, item: Incomplete | None = ...
    ) -> Generator[Incomplete, None, None]:
        ...

    def unpack_data(self, data: bytes):
        ...

    def unpack_item(self, item):
        ...


class DynamicField(Field):
    def pre_pack(self, parents: type, data: bytes) -> None:
        ...

    def pre_unpack(self, parents: type, data: bytes) -> None:
        ...

    def post_unpack(self, parents: type, data: bytes) -> None:
        ...


class Structure(struct.Struct):
    name: str
    fields: list[
        Field
        | NullStaticStringField
        | DynamicWaveDataField1
        | DynamicWaveNoteField
        | DynamicDependencyFormulaField
        | DynamicWaveDataField5
        | DynamicDependencyFormulaField
        | DynamicWaveNoteField
        | DynamicDataUnitsField
        | DynamicDimensionUnitsField
        | DynamicLabelsField
        | DynamicStringIndicesDataField
    ]
    byte_order: BYTEORDER

    def __init__(
        self, name: str, fields: list[Field], byte_order: BYTEORDER = ...
    ) -> None:
        ...

    def setup(self) -> None:
        ...

    def set_byte_order(self, byte_order: BYTEORDER) -> None:
        ...

    def get_format(self) -> str:
        ...

    def sub_format(self) -> Generator[Incomplete, None, None]:
        ...

    def pack(self, data: dict):
        ...

    def pack_into(self, buffer, offset: int = ..., data: bytes = ...):
        ...

    def unpack(self, *args, **kwargs):
        ...

    def unpack_from(self, buffer, offset: int = ..., *args, **kwargs):
        ...

    def get_field(self, name: str):
        ...


class DebuggingStream:
    stream: BinaryIO

    def __init__(self, stream: BinaryIO) -> None:
        ...

    def read(self, size: int):
        ...


class DynamicStructure(Structure):
    def pack(self, data: dict) -> bytearray:
        ...

    def pack_into(self, buffer, offset: int = ..., data: bytes = ...) -> None:
        ...

    def unpack_stream(
        self,
        stream: BinaryIO,
        parents: type | None = ...,
        data: dict | None = ...,
        d: Incomplete | None = ...,
    ) -> IBW:
        ...

    def unpack(self, string):
        ...

    def unpack_from(self, buffer, offset: int = ..., *args, **kwargs):
        ...
