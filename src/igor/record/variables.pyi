from __future__ import annotations
from ..binarywave import DynamicStringField, NullStaticStringField
from ..struct import (
    DynamicField,
    DynamicStructure,
    Structure,
)
from .base import Record
from _typeshed import Incomplete
from .._typing import BYTEORDER

class ListedStaticStringField(NullStaticStringField):
    def post_unpack(self, parents: type, data: bytes) -> None: ...

class ListedDynamicStrDataField(DynamicStringField, ListedStaticStringField): ...

class DynamicVarDataField(DynamicField):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def pre_pack(self, parents: Incomplete, data: Incomplete) -> None: ...
    def post_unpack(self, parents: Incomplete, data: Incomplete) -> None: ...

class DynamicSysVarField(DynamicVarDataField): ...
class DynamicUserVarField(DynamicVarDataField): ...
class DynamicUserStrField(DynamicVarDataField): ...

class DynamicVarNumField(DynamicField):
    def post_unpack(self, parents: type, data: bytes) -> None: ...

class DynamicFormulaField(DynamicStringField): ...

VarHeader1: Structure
VarHeader2: Structure
UserStrVarRec1: DynamicStructure
UserStrVarRec2: DynamicStructure
VarNumRec: Structure
UserNumVarRec: DynamicStructure
UserDependentVarRec: DynamicStructure

class DynamicVarHeaderField(DynamicField):
    def pre_pack(self, parents: Incomplete, data: Incomplete) -> None: ...
    def post_unpack(self, parents: Incomplete, data: Incomplete) -> None: ...

Variables1: DynamicVarHeaderField
Variables2: DynamicStructure

class DynamicVersionField(DynamicField):
    def pre_pack(self, parents: Incomplete, byte_order: BYTEORDER) -> None: ...
    def post_unpack(self, parents: type, data: bytes) -> None: ...

VariablesRecordStructure: DynamicStructure

class VariablesRecord(Record):
    variables: dict[str, float | dict[str, float | dict[str, float]]]
    namespace: dict[str | bytes, float]

    def __init__(
        self,
        *args: dict[str, int] | bytes | BYTEORDER,
        **kwargs: dict[str, int] | bytes | BYTEORDER,
    ) -> None: ...
