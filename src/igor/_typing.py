from __future__ import annotations

import numpy as np
from typing import TypedDict, TypeAlias, Literal
from numpy.typing import NDArray


from _typeshed import Incomplete
from .record.base import UnknownRecord
from .record.folder import FolderStartRecord
from .record.folder import FolderEndRecord
from .record.history import HistoryRecord
from .record.history import GetHistoryRecord
from .record.history import RecreationRecord
from .record.procedure import ProcedureRecord
from .record.wave import WaveRecord
from .record.variables import VariablesRecord

BYTEORDER = Literal[">", "<", "=", "@", "!", ""]


class WAVETYPE(TypedDict, total=False):
    binheader: dict[str, int | NDArray[np.int_]]
    waveheader: dict[
        str,
        str | bytes | float | NDArray[np.str_] | NDArray[np.int_] | NDArray[np.float_],
    ]
    wData: NDArray[np.float_] | NDArray[np.complex_]
    formula: bytes
    note: bytes
    data_units: bytes
    dimension_units: bytes
    labels: list[list[Incomplete]]
    sIndics: NDArray[np.float_]


class IBW(TypedDict, total=False):
    version: int
    wave: WAVETYPE


class PXP(TypedDict, total=False):
    pass


RECORDS: TypeAlias = list[
    UnknownRecord
    | VariablesRecord
    | HistoryRecord
    | WaveRecord
    | FolderStartRecord
    | FolderEndRecord
    | RecreationRecord
    | ProcedureRecord
    | GetHistoryRecord
]
