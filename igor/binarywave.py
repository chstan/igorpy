# Copyright (C) 2010-2012 W. Trevor King <wking@tremily.us>
#
# This file is part of igor.
#
# igor is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# igor is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with igor.  If not, see <http://www.gnu.org/licenses/>.

# Memo not essential diff

"Read IGOR Binary Wave files into Numpy arrays."

# Based on WaveMetric's Technical Note 003, "Igor Binary Format"
#   ftp://ftp.wavemetrics.net/IgorPro/Technical_Notes/TN003.zip
# From ftp://ftp.wavemetrics.net/IgorPro/Technical_Notes/TN000.txt
#   We place no restrictions on copying Technical Notes, with the
#   exception that you cannot resell them. So read, enjoy, and
#   share. We hope IGOR Technical Notes will provide you with lots of
#   valuable information while you are developing IGOR applications.


import numpy as np

from . import LOG
from .struct import Structure
from .struct import DynamicStructure
from .struct import DynamicField
from .struct import Field
from .util import byte_order
from .util import need_to_reorder_bytes as _need_to_reorder_bytes
from .util import checksum


# Numpy doesn't support complex integers by default, see
#   http://mail.python.org/pipermail/python-dev/2002-April/022408.html
#   http://mail.scipy.org/pipermail/numpy-discussion/2007-October/029447.html
# So we roll our own types.  See
#   http://docs.scipy.org/doc/numpy/user/basics.rec.html
#   http://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.html
complexInt8 = np.dtype([("real", np.int8), ("imag", np.int8)])
complexInt16 = np.dtype([("real", np.int16), ("imag", np.int16)])
complexInt32 = np.dtype([("real", np.int32), ("imag", np.int32)])
complexUInt8 = np.dtype([("real", np.uint8), ("imag", np.uint8)])
complexUInt16 = np.dtype([("real", np.uint16), ("imag", np.uint16)])
complexUInt32 = np.dtype([("real", np.uint32), ("imag", np.uint32)])


class StaticStringField(DynamicField):
    _null_terminated = False
    _array_size_field = None

    def __init__(self, *args, **kwargs):
        if "array" not in kwargs:
            kwargs["array"] = True
        super().__init__(*args, **kwargs)

    def post_unpack(self, parents, data):
        wave_structure = parents[-1]
        wave_data = self._get_structure_data(parents, data, wave_structure)
        d = self._normalize_string(wave_data[self.name])
        wave_data[self.name] = d

    def _normalize_string(self, d):
        if isinstance(d, bytes):
            pass
        elif hasattr(d, "tobytes"):
            d = d.tobytes()
        elif hasattr(d, "tostring"):  # Python 2 compatibility
            d = d.tostring()
        else:
            d = b"".join(d)
        if self._array_size_field:
            start = 0
            strings = []
            for count in self.counts:
                end = start + count
                if end > start:
                    strings.append(d[start:end])
                    if self._null_terminated:
                        strings[-1] = strings[-1].split(b"\x00", 1)[0]
                    start = end
        elif self._null_terminated:
            d = d.split(b"\x00", 1)[0]
        return d


class NullStaticStringField(StaticStringField):
    _null_terminated = True


# Begin IGOR constants and typedefs from IgorBin.h

# From IgorMath.h
TYPE_TABLE = {  # (key: integer flag, value: numpy dtype)
    0: None,  # Text wave, not handled in ReadWave.c
    1: complex,  # NT_CMPLX, makes number complex.
    2: np.float32,  # NT_FP32, 32 bit fp numbers.
    3: np.complex64,
    4: np.float64,  # NT_FP64, 64 bit fp numbers.
    5: np.complex128,
    8: np.int8,  # NT_I8, 8 bit signed integer. Requires Igor Pro
    # 2.0 or later.
    9: complexInt8,
    0x10: np.int16,  # NT_I16, 16 bit integer numbers. Requires Igor
    # Pro 2.0 or later.
    0x11: complexInt16,
    0x20: np.int32,  # NT_I32, 32 bit integer numbers. Requires Igor
    # Pro 2.0 or later.
    0x21: complexInt32,
    #   0x40:None,        # NT_UNSIGNED, Makes above signed integers
    #                     # unsigned. Requires Igor Pro 3.0 or later.
    0x48: np.uint8,
    0x49: complexUInt8,
    0x50: np.uint16,
    0x51: complexUInt16,
    0x60: np.uint32,
    0x61: complexUInt32,
}

# From wave.h
MAXDIMS = 4

# From binary.h
BinHeader1 = Structure(  # `version` field pulled out into Wave
    name="BinHeader1",
    fields=[
        Field(
            "l",
            "wfmSize",
            help="The size of the WaveHeader2 data structure plus the wave data plus 16 bytes of padding.",
        ),
        Field("h", "checksum", help="Checksum over this header and the wave header."),
    ],
)

BinHeader2 = Structure(  # `version` field pulled out into Wave
    name="BinHeader2",
    fields=[
        Field(
            "l",
            "wfmSize",
            help="The size of the WaveHeader2 data structure plus the wave data plus 16 bytes of padding.",
        ),
        Field("l", "noteSize", help="The size of the note text."),
        Field("l", "pictSize", default=0, help="Reserved. Write zero. Ignore on read."),
        Field("h", "checksum", help="Checksum over this header and the wave header."),
    ],
)

BinHeader3 = Structure(  # `version` field pulled out into Wave
    name="BinHeader3",
    fields=[
        Field(
            "l",
            "wfmSize",
            help="The size of the WaveHeader2 data structure plus the wave data plus 16 bytes of padding.",
        ),
        Field("l", "noteSize", help="The size of the note text."),
        Field("l", "formulaSize", help="The size of the dependency formula, if any."),
        Field("l", "pictSize", default=0, help="Reserved. Write zero. Ignore on read."),
        Field("h", "checksum", help="Checksum over this header and the wave header."),
    ],
)

BinHeader5 = Structure(  # `version` field pulled out into Wave
    name="BinHeader5",
    fields=[
        Field("h", "checksum", help="Checksum over this header and the wave header."),
        Field(
            "l",
            "wfmSize",
            help="The size of the WaveHeader5 data structure plus the wave data.",
        ),
        Field("l", "formulaSize", help="The size of the dependency formula, if any."),
        Field("l", "noteSize", help="The size of the note text."),
        Field("l", "dataEUnitsSize", help="The size of optional extended data units."),
        Field(
            "l",
            "dimEUnitsSize",
            help="The size of optional extended dimension units.",
            count=MAXDIMS,
            array=True,
        ),
        Field(
            "l",
            "dimLabelsSize",
            help="The size of optional dimension labels.",
            count=MAXDIMS,
            array=True,
        ),
        Field(
            "l",
            "sIndicesSize",
            help="The size of string indices if this is a text wave.",
        ),
        Field(
            "l", "optionsSize1", default=0, help="Reserved. Write zero. Ignore on read."
        ),
        Field(
            "l", "optionsSize2", default=0, help="Reserved. Write zero. Ignore on read."
        ),
    ],
)


# From wave.h
MAX_WAVE_NAME2 = 18  # Maximum length of wave name in version 1 and 2
# files. Does not include the trailing null.
MAX_WAVE_NAME5 = 31  # Maximum length of wave name in version 5
# files. Does not include the trailing null.
MAX_UNIT_CHARS = 3

# Header to an array of waveform data.

# `wData` field pulled out into DynamicWaveDataField1
WaveHeader2 = DynamicStructure(
    name="WaveHeader2",
    fields=[
        Field("h", "type", help="See types (e.g. NT_FP64) above. Zero for text waves."),
        Field(
            "P",
            "next",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        NullStaticStringField(
            "c",
            "bname",
            help="Name of wave plus trailing null.",
            count=MAX_WAVE_NAME2 + 2,
        ),
        Field("h", "whVersion", default=0, help="Write 0. Ignore on read."),
        Field(
            "h",
            "srcFldr",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "P",
            "fileName",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "c",
            "dataUnits",
            default=0,
            help="Natural data units go here - null if none.",
            count=MAX_UNIT_CHARS + 1,
            array=True,
        ),
        Field(
            "c",
            "xUnits",
            default=0,
            help="Natural x-axis units go here - null if none.",
            count=MAX_UNIT_CHARS + 1,
            array=True,
        ),
        Field("l", "npnts", help="Number of data points in wave."),
        Field(
            "h",
            "aModified",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field("d", "hsA", help="X value for point p = hsA*p + hsB"),
        Field("d", "hsB", help="X value for point p = hsA*p + hsB"),
        Field(
            "h",
            "wModified",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "h",
            "swModified",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field("h", "fsValid", help="True if full scale values have meaning."),
        Field(
            "d", "topFullScale", help="The min full scale value for wave."
        ),  # sic, 'min' should probably be 'max'
        Field("d", "botFullScale", help="The min full scale value for wave."),
        Field(
            "c",
            "useBits",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field("c", "kindBits", default=0, help="Reserved. Write zero. Ignore on read."),
        Field(
            "P",
            "formula",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "l",
            "depID",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "L",
            "creationDate",
            help="DateTime of creation.  Not used in version 1 files.",
        ),
        Field(
            "c",
            "wUnused",
            default=0,
            help="Reserved. Write zero. Ignore on read.",
            count=2,
            array=True,
        ),
        Field("L", "modDate", help="DateTime of last modification."),
        Field(
            "P", "waveNoteH", help="Used in memory only. Write zero. Ignore on read."
        ),
    ],
)

# `sIndices` pointer unset (use Wave5_data['sIndices'] instead).  This
# field is filled in by DynamicStringIndicesDataField.
# `wData` field pulled out into DynamicWaveDataField5
WaveHeader5 = DynamicStructure(
    name="WaveHeader5",
    fields=[
        Field("P", "next", help="link to next wave in linked list."),
        Field("L", "creationDate", help="DateTime of creation."),
        Field("L", "modDate", help="DateTime of last modification."),
        Field(
            "l",
            "npnts",
            help="Total number of points (multiply dimensions up to first zero).",
        ),
        Field("h", "type", help="See types (e.g. NT_FP64) above. Zero for text waves."),
        Field("h", "dLock", default=0, help="Reserved. Write zero. Ignore on read."),
        Field(
            "c",
            "whpad1",
            default=0,
            help="Reserved. Write zero. Ignore on read.",
            count=6,
            array=True,
        ),
        Field("h", "whVersion", default=1, help="Write 1. Ignore on read."),
        NullStaticStringField(
            "c",
            "bname",
            help="Name of wave plus trailing null.",
            count=MAX_WAVE_NAME5 + 1,
        ),
        Field("l", "whpad2", default=0, help="Reserved. Write zero. Ignore on read."),
        Field(
            "P",
            "dFolder",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        # Dimensioning info. [0] == rows, [1] == cols etc
        Field(
            "l",
            "nDim",
            help="Number of of items in a dimension -- 0 means no data.",
            count=MAXDIMS,
            array=True,
        ),
        Field(
            "d",
            "sfA",
            help="Index value for element e of dimension d = sfA[d]*e + sfB[d].",
            count=MAXDIMS,
            array=True,
        ),
        Field(
            "d",
            "sfB",
            help="Index value for element e of dimension d = sfA[d]*e + sfB[d].",
            count=MAXDIMS,
            array=True,
        ),
        # SI units
        Field(
            "c",
            "dataUnits",
            default=0,
            help="Natural data units go here - null if none.",
            count=MAX_UNIT_CHARS + 1,
            array=True,
        ),
        Field(
            "c",
            "dimUnits",
            default=0,
            help="Natural dimension units go here - null if none.",
            count=(MAXDIMS, MAX_UNIT_CHARS + 1),
            array=True,
        ),
        Field("h", "fsValid", help="TRUE if full scale values have meaning."),
        Field("h", "whpad3", default=0, help="Reserved. Write zero. Ignore on read."),
        Field(
            "d", "topFullScale", help="The max and max full scale value for wave"
        ),  # sic, probably "max and min"
        Field(
            "d", "botFullScale", help="The max and max full scale value for wave."
        ),  # sic, probably "max and min"
        Field(
            "P",
            "dataEUnits",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "P",
            "dimEUnits",
            default=0,
            help="Used in memory only. Write zero.  Ignore on read.",
            count=MAXDIMS,
            array=True,
        ),
        Field(
            "P",
            "dimLabels",
            default=0,
            help="Used in memory only. Write zero.  Ignore on read.",
            count=MAXDIMS,
            array=True,
        ),
        Field(
            "P",
            "waveNoteH",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "l",
            "whUnused",
            default=0,
            help="Reserved. Write zero. Ignore on read.",
            count=16,
            array=True,
        ),
        # The following stuff is considered private to Igor.
        Field(
            "h",
            "aModified",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "h",
            "wModified",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "h",
            "swModified",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "c",
            "useBits",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field("c", "kindBits", default=0, help="Reserved. Write zero. Ignore on read."),
        Field(
            "P",
            "formula",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "l",
            "depID",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field("h", "whpad4", default=0, help="Reserved. Write zero. Ignore on read."),
        Field(
            "h",
            "srcFldr",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "P",
            "fileName",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
        Field(
            "P",
            "sIndices",
            default=0,
            help="Used in memory only. Write zero. Ignore on read.",
        ),
    ],
)


class DynamicWaveDataField1(DynamicField):
    def pre_pack(self, parents, data):
        raise NotImplementedError()

    def pre_unpack(self, parents, data):
        parents[0]
        wave_structure = parents[-1]
        wave_header_structure = wave_structure.fields[1].format
        wave_data = self._get_structure_data(parents, data, wave_structure)
        version = data["version"]
        bin_header = wave_data["bin_header"]
        wave_header = wave_data["wave_header"]

        self.count = wave_header["npnts"]
        self.data_size = self._get_size(bin_header, wave_header_structure.size)

        type_ = TYPE_TABLE.get(wave_header["type"], None)
        if type_:
            self.shape = self._get_shape(bin_header, wave_header)
        else:  # text wave
            type_ = np.dtype("S1")
            self.shape = (self.data_size,)
        # dtype() wrapping to avoid numpy.generic and
        # getset_descriptor issues with the builtin numpy types
        # (e.g. int32).  It has no effect on our local complex
        # integers.
        self.dtype = np.dtype(type_).newbyteorder(wave_structure.byte_order)
        if (
            version == 3
            and self.count > 0
            and bin_header["formulaSize"] > 0
            and self.data_size == 0
        ):
            """From TN003:

            Igor Pro 2.00 included support for dependency formulae. If
            a wave was governed by a dependency formula then the
            actual wave data was not written to disk for that wave,
            because on loading the wave Igor could recalculate the
            data. However,this prevented the wave from being loaded
            into an experiment other than the original
            experiment. Consequently, in a version of Igor Pro 3.0x,
            we changed it so that the wave data was written even if
            the wave was governed by a dependency formula. When
            reading a binary wave file, you can detect that the wave
            file does not contain the wave data by examining the
            wfmSize, formulaSize and npnts fields. If npnts is greater
            than zero and formulaSize is greater than zero and
            the waveDataSize as calculated above is zero, then this is
            a file governed by a dependency formula that was written
            without the actual wave data.
            """
            self.shape = (0,)
        elif TYPE_TABLE.get(wave_header["type"], None) is not None:
            assert self.data_size == self.count * self.dtype.itemsize, (
                self.data_size,
                self.count,
                self.dtype.itemsize,
                self.dtype,
            )
        else:
            assert self.data_size >= 0, (
                bin_header["wfmSize"],
                wave_header_structure.size,
            )

    def _get_size(self, bin_header, wave_header_size):
        return bin_header["wfmSize"] - wave_header_size - 16

    def _get_shape(self, bin_header, wave_header):
        return (self.count,)

    def unpack(self, stream):
        data_b = stream.read(self.data_size)
        try:
            data = np.ndarray(
                shape=self.shape,
                dtype=self.dtype,
                buffer=data_b,
                order="F",
            )
        except:
            LOG.error(f"could not reshape data from {self.shape} to {data_b}")
            raise
        return data


class DynamicWaveDataField5(DynamicWaveDataField1):
    "Adds support for multidimensional data."

    def _get_size(self, bin_header, wave_header_size):
        return bin_header["wfmSize"] - wave_header_size

    def _get_shape(self, bin_header, wave_header):
        return [n for n in wave_header["nDim"] if n > 0] or (0,)


# End IGOR constants and typedefs from IgorBin.h


class DynamicStringField(StaticStringField):
    _size_field = None

    def pre_unpack(self, parents, data):
        size = self._get_size_data(parents, data)
        if self._array_size_field:
            self.counts = size
            self.count = sum(self.counts)
        else:
            self.count = size
        self.setup()

    def _get_size_data(self, parents, data):
        wave_structure = parents[-1]
        wave_data = self._get_structure_data(parents, data, wave_structure)
        bin_header = wave_data["bin_header"]
        return bin_header[self._size_field]


class DynamicWaveNoteField(DynamicStringField):
    _size_field = "noteSize"


class DynamicDependencyFormulaField(DynamicStringField):
    """Optional wave dependency formula

    Excerpted from TN003:

    A wave has a dependency formula if it has been bound by a
    statement such as "wave0 := sin(x)". In this example, the
    dependency formula is "sin(x)". The formula is stored with
    no trailing null byte.
    """

    _size_field = "formulaSize"
    # Except when it is stored with a trailing null byte :p.  See, for
    # example, test/data/mac-version3Dependent.ibw.
    _null_terminated = True


class DynamicDataUnitsField(DynamicStringField):
    """Optional extended data units data

    Excerpted from TN003:

    dataUnits - Present in versions 1, 2, 3, 5. The dataUnits field
      stores the units for the data represented by the wave. It is a C
      string terminated with a null character. This field supports
      units of 0 to 3 bytes. In version 1, 2 and 3 files, longer units
      can not be represented. In version 5 files, longer units can be
      stored using the optional extended data units section of the
      file.
    """

    _size_field = "dataEUnitsSize"


class DynamicDimensionUnitsField(DynamicStringField):
    """Optional extended dimension units data

    Excerpted from TN003:

    xUnits - Present in versions 1, 2, 3. The xUnits field stores the
      X units for a wave. It is a C string terminated with a null
      character.  This field supports units of 0 to 3 bytes. In
      version 1, 2 and 3 files, longer units can not be represented.

    dimUnits - Present in version 5 only. This field is an array of 4
      strings, one for each possible wave dimension. Each string
      supports units of 0 to 3 bytes. Longer units can be stored using
      the optional extended dimension units section of the file.
    """

    _size_field = "dimEUnitsSize"
    _array_size_field = True


class DynamicLabelsField(DynamicStringField):
    """Optional dimension label data

    From TN003:

    If the wave has dimension labels for dimension d then the
    dimLabelsSize[d] field of the BinHeader5 structure will be
    non-zero.

    A wave will have dimension labels if a SetDimLabel command has
    been executed on it.

    A 3 point 1D wave has 4 dimension labels. The first dimension
    label is the label for the dimension as a whole. The next three
    dimension labels are the labels for rows 0, 1, and 2. When Igor
    writes dimension labels to disk, it writes each dimension label as
    a C string (null-terminated) in a field of 32 bytes.
    """

    _size_field = "dimLabelsSize"
    _array_size_field = True

    def post_unpack(self, parents, data):
        wave_structure = parents[-1]
        wave_data = self._get_structure_data(parents, data, wave_structure)
        bin_header = wave_data["bin_header"]
        d = wave_data[self.name]
        dim_labels = []
        start = 0
        for size in bin_header[self._size_field]:
            end = start + size
            if end > start:
                dim_data = d[start:end]
                chunks = []
                for i in range(size // 32):
                    chunks.append(dim_data[32 * i : 32 * (i + 1)])
                labels = [b""]
                for chunk in chunks:
                    labels[-1] = labels[-1] + b"".join(chunk)
                    if b"\x00" in chunk:
                        labels.append(b"")
                labels.pop(-1)
                start = end
            else:
                labels = []
            dim_labels.append(labels)
        wave_data[self.name] = dim_labels


class DynamicStringIndicesDataField(DynamicField):
    """String indices used for text waves only"""

    def pre_pack(self, parents, data):
        raise NotImplementedError()

    def pre_unpack(self, parents, data):
        wave_structure = parents[-1]
        wave_data = self._get_structure_data(parents, data, wave_structure)
        bin_header = wave_data["bin_header"]
        wave_header = wave_data["wave_header"]
        self.string_indices_size = bin_header["sIndicesSize"]
        self.count = self.string_indices_size // 4
        if self.count:  # make sure we're in a text wave
            assert TYPE_TABLE[wave_header["type"]] is None, wave_header
        self.setup()

    def post_unpack(self, parents, data):
        if not self.count:
            return
        wave_structure = parents[-1]
        wave_data = self._get_structure_data(parents, data, wave_structure)
        wave_header = wave_data["wave_header"]
        wdata = wave_data["wData"]
        strings = []
        start = 0
        for i, offset in enumerate(wave_data["sIndices"]):
            if offset > start:
                chars = wdata[start:offset]
                strings.append(b"".join(chars))
                start = offset
            elif offset == start:
                strings.append(b"")
            else:
                raise ValueError((offset, wave_data["sIndices"]))
        wdata = np.array(strings)
        shape = [n for n in wave_header["nDim"] if n > 0] or (0,)
        try:
            wdata = wdata.reshape(shape)
        except ValueError:
            LOG.error(f"could not reshape strings from {shape} to {wdata.shape}")
            raise
        wave_data["wData"] = wdata


class DynamicVersionField(DynamicField):
    def pre_pack(self, parents, byte_order):
        raise NotImplementedError()

    def post_unpack(self, parents, data):
        wave_structure = parents[-1]
        wave_data = self._get_structure_data(parents, data, wave_structure)
        version = wave_data["version"]
        if wave_structure.byte_order in "@=":
            need_to_reorder_bytes = _need_to_reorder_bytes(version)
            wave_structure.byte_order = byte_order(need_to_reorder_bytes)
            LOG.debug(
                "get byte order from version: {} (reorder? {})".format(
                    wave_structure.byte_order, need_to_reorder_bytes
                )
            )
        else:
            need_to_reorder_bytes = False

        old_format = wave_structure.fields[-1].format
        if version == 1:
            wave_structure.fields[-1].format = Wave1
        elif version == 2:
            wave_structure.fields[-1].format = Wave2
        elif version == 3:
            wave_structure.fields[-1].format = Wave3
        elif version == 5:
            wave_structure.fields[-1].format = Wave5
        elif not need_to_reorder_bytes:
            raise ValueError(f"invalid binary wave version: {version}")

        if wave_structure.fields[-1].format != old_format:
            LOG.debug(
                "change wave headers from {} to {}".format(
                    old_format, wave_structure.fields[-1].format
                )
            )
            wave_structure.setup()
        elif need_to_reorder_bytes:
            wave_structure.setup()

        # we might need to unpack again with the new byte order
        return need_to_reorder_bytes


class DynamicWaveField(DynamicField):
    def post_unpack(self, parents, data):
        return
        raise NotImplementedError()  # TODO
        checksum_size = bin.size + wave.size
        parents[-1]
        if version == 5:
            # Version 5 checksum does not include the wData field.
            checksum_size -= 4
        c = checksum(b, parents[-1].byte_order, 0, checksum_size)
        if c != 0:
            raise ValueError(
                (
                    "This does not appear to be a valid Igor binary wave file.  "
                    "Error in checksum: should be 0, is {}."
                ).format(c)
            )


Wave1 = DynamicStructure(
    name="Wave1",
    fields=[
        Field(BinHeader1, "bin_header", help="Binary wave header"),
        Field(WaveHeader2, "wave_header", help="Wave header"),
        DynamicWaveDataField1(
            "f",
            "wData",
            help="The start of the array of waveform data.",
            count=0,
            array=True,
        ),
    ],
)

Wave2 = DynamicStructure(
    name="Wave2",
    fields=[
        Field(BinHeader2, "bin_header", help="Binary wave header"),
        Field(WaveHeader2, "wave_header", help="Wave header"),
        DynamicWaveDataField1(
            "f",
            "wData",
            help="The start of the array of waveform data.",
            count=0,
            array=True,
        ),
        Field(
            "x",
            "padding",
            help="16 bytes of padding in versions 2 and 3.",
            count=16,
            array=True,
        ),
        DynamicWaveNoteField(
            "c", "note", help="Optional wave note data", count=0, array=True
        ),
    ],
)

Wave3 = DynamicStructure(
    name="Wave3",
    fields=[
        Field(BinHeader3, "bin_header", help="Binary wave header"),
        Field(WaveHeader2, "wave_header", help="Wave header"),
        DynamicWaveDataField1(
            "f",
            "wData",
            help="The start of the array of waveform data.",
            count=0,
            array=True,
        ),
        Field(
            "x",
            "padding",
            help="16 bytes of padding in versions 2 and 3.",
            count=16,
            array=True,
        ),
        DynamicWaveNoteField(
            "c", "note", help="Optional wave note data", count=0, array=True
        ),
        DynamicDependencyFormulaField(
            "c", "formula", help="Optional wave dependency formula", count=0, array=True
        ),
    ],
)

Wave5 = DynamicStructure(
    name="Wave5",
    fields=[
        Field(BinHeader5, "bin_header", help="Binary wave header"),
        Field(WaveHeader5, "wave_header", help="Wave header"),
        DynamicWaveDataField5(
            "f",
            "wData",
            help="The start of the array of waveform data.",
            count=0,
            array=True,
        ),
        DynamicDependencyFormulaField(
            "c",
            "formula",
            help="Optional wave dependency formula.",
            count=0,
            array=True,
        ),
        DynamicWaveNoteField(
            "c", "note", help="Optional wave note data.", count=0, array=True
        ),
        DynamicDataUnitsField(
            "c",
            "data_units",
            help="Optional extended data units data.",
            count=0,
            array=True,
        ),
        DynamicDimensionUnitsField(
            "c",
            "dimension_units",
            help="Optional dimension label data",
            count=0,
            array=True,
        ),
        DynamicLabelsField(
            "c", "labels", help="Optional dimension label data", count=0, array=True
        ),
        DynamicStringIndicesDataField(
            "P",
            "sIndices",
            help="Dynamic string indices for text waves.",
            count=0,
            array=True,
        ),
    ],
)

Wave = DynamicStructure(
    name="Wave",
    fields=[
        DynamicVersionField(
            "h", "version", help="Version number for backwards compatibility."
        ),
        DynamicWaveField(Wave1, "wave", help="The rest of the wave data."),
    ],
)


def load(filename):
    if hasattr(filename, "read"):
        f = filename  # filename is actually a stream object
    else:
        f = open(filename, "rb")
    try:
        Wave.byte_order = "="
        Wave.setup()
        data = Wave.unpack_stream(f)
    finally:
        if not hasattr(filename, "read"):
            f.close()

    return data


def save(filename):
    raise NotImplementedError
