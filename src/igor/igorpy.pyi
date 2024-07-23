from __future__ import annotations
import re

from _typeshed import Incomplete

from .binarywave import MAXDIMS
from .packed import load
from .record.base import UnknownRecord
from .record.folder import FolderEndRecord, FolderStartRecord
from .record.history import GetHistoryRecord, HistoryRecord, RecreationRecord
from .record.packedfile import PackedFileRecord
from .record.procedure import ProcedureRecord
from .record.variables import VariablesRecord
from .record.wave import WaveRecord

ENCODING: str
PYKEYWORDS: set[str]
PYID: re.Pattern


def valid_identifier(s):
    ...


class IgorObject:
    ...


class Variables(IgorObject):
    sysvar: Incomplete
    uservar: Incomplete
    userstr: Incomplete
    depvar: Incomplete
    depstr: Incomplete

    def __init__(self, record) -> None:
        ...

    def format(self, indent: int = ...):
        ...


class History(IgorObject):
    data: Incomplete

    def __init__(self, data) -> None:
        ...

    def format(self, indent: int = ...):
        ...


class Wave(IgorObject):
    name: Incomplete
    data: Incomplete
    fs: Incomplete
    fstop: Incomplete
    fsbottom: Incomplete
    data_units: Incomplete
    axis_units: Incomplete
    axis: Incomplete
    formula: Incomplete
    notes: Incomplete

    def __init__(self, record) -> None:
        ...

    def format(self, indent: int = ...):
        ...

    def __array__(self):
        ...


class Recreation(IgorObject):
    data: Incomplete

    def __init__(self, data) -> None:
        ...

    def format(self, indent: int = ...):
        ...


class Procedure(IgorObject):
    data: Incomplete

    def __init__(self, data) -> None:
        ...

    def format(self, indent: int = ...):
        ...


class GetHistory(IgorObject):
    data: Incomplete

    def __init__(self, data) -> None:
        ...

    def format(self, indent: int = ...):
        ...


class PackedFile(IgorObject):
    data: Incomplete

    def __init__(self, data) -> None:
        ...

    def format(self, indent: int = ...):
        ...


class Unknown(IgorObject):
    data: Incomplete
    type: Incomplete

    def __init__(self, data, type) -> None:
        ...

    def format(self, indent: int = ...):
        ...


class Folder(IgorObject):
    name: Incomplete
    path: Incomplete
    children: Incomplete

    def __init__(self, path) -> None:
        ...

    def __getitem__(self, key):
        ...

    def append(self, record) -> None:
        ...

    def format(self, indent: int = ...):
        ...


def loads(s, **kwargs):
    ...
