from helper import assert_equal_dump_no_whitespace_no_byte, dumpibw


def test_ibw01():
    act = dumpibw("mac-double.ibw")  # doctest: +REPORT_UDIFF

    exp = """{'version': 2,
             'wave': {'bin_header': {'checksum': 25137,
                                     'noteSize': 0,
                                     'pictSize': 0,
                                     'wfmSize': 166},
                      'note': '',
                      'padding': array([], dtype=float64),
                      'wData': array([ 5.,  4.,  3.,  2.,  1.]),
                      'wave_header': {'aModified': 0,
                                      'bname': 'double',
                                      'botFullScale': 0.0,
                                      'creationDate': 3001587842,
                                      'dataUnits': array(['', '', '', ''],
                  dtype='|S1'),
                                      'depID': 0,
                                      'fileName': 0,
                                      'formula': 0,
                                      'fsValid': 0,
                                      'hsA': 1.0,
                                      'hsB': 0.0,
                                      'kindBits': '\\x00',
                                      'modDate': 3001587842,
                                      'next': 0,
                                      'npnts': 5,
                                      'srcFldr': 0,
                                      'swModified': 0,
                                      'topFullScale': 0.0,
                                      'type': 4,
                                      'useBits': '\\x00',
                                      'wModified': 0,
                                      'wUnused': array(['', ''],
                  dtype='|S1'),
                                      'waveNoteH': 0,
                                      'whVersion': 0,
                                      'xUnits': array(['', '', '', ''],
                  dtype='|S1')}}}"""

    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_02():
    act = dumpibw("mac-textWave.ibw")

    exp = """
    {'version': 5,
     'wave': {'bin_header': {'checksum': 5554,
                             'dataEUnitsSize': 0,
                             'dimEUnitsSize': array([0, 0, 0, 0]),
                             'dimLabelsSize': array([0, 0, 0, 0]),
                             'formulaSize': 0,
                             'noteSize': 0,
                             'optionsSize1': 0,
                             'optionsSize2': 0,
                             'sIndicesSize': 20,
                             'wfmSize': 338},
              'data_units': '',
              'dimension_units': '',
              'formula': '',
              'labels': [[], [], [], []],
              'note': '',
              'sIndices': array([ 4,  7,  8, 14, 18]),
              'wData': array(['Mary', 'had', 'a', 'little', 'lamb'],
          dtype='|S6'),
              'wave_header': {'aModified': 0,
                              'bname': 'text0',
                              'botFullScale': 0.0,
                              'creationDate': 3001571199,
                              'dFolder': 69554896,
                              'dLock': 0,
                              'dataEUnits': 0,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 22,
                              'dimEUnits': array([0, 0, 0, 0]),
                              'dimLabels': array([0, 0, 0, 0]),
                              'dimUnits': array([['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', '']],
          dtype='|S1'),
                              'fileName': 0,
                              'formula': 0,
                              'fsValid': 0,
                              'kindBits': '\\x00',
                              'modDate': 3001571215,
                              'nDim': array([5, 0, 0, 0]),
                              'next': 0,
                              'npnts': 5,
                              'sIndices': 69557296,
                              'sfA': array([ 1.,  1.,  1.,  1.]),
                              'sfB': array([ 0.,  0.,  0.,  0.]),
                              'srcFldr': 0,
                              'swModified': 1,
                              'topFullScale': 0.0,
                              'type': 0,
                              'useBits': '\\x00',
                              'wModified': 0,
                              'waveNoteH': 0,
                              'whUnused': array([0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0]),
                              'whVersion': 1,
                              'whpad1': array(['', '', '', '', '', ''],
          dtype='|S1'),
                              'whpad2': 0,
                              'whpad3': 0,
                              'whpad4': 0}}}
    """

    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_03():
    act = dumpibw("mac-version2.ibw")
    exp = """
    {'version': 2,
     'wave': {'bin_header': {'checksum': -16803,
                             'noteSize': 15,
                             'pictSize': 0,
                             'wfmSize': 146},
              'note': 'This is a test.',
              'padding': array([], dtype=float64),
              'wData': array([ 5.,  4.,  3.,  2.,  1.], dtype=float32),
              'wave_header': {'aModified': 0,
                              'bname': 'version2',
                              'botFullScale': 0.0,
                              'creationDate': 3001251979,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 0,
                              'fileName': 0,
                              'formula': 0,
                              'fsValid': 0,
                              'hsA': 1.0,
                              'hsB': 0.0,
                              'kindBits': '\\x00',
                              'modDate': 3001573594,
                              'next': 0,
                              'npnts': 5,
                              'srcFldr': 0,
                              'swModified': 0,
                              'topFullScale': 0.0,
                              'type': 2,
                              'useBits': '\\x00',
                              'wModified': 0,
                              'wUnused': array(['', ''],
          dtype='|S1'),
                              'waveNoteH': 0,
                              'whVersion': 0,
                              'xUnits': array(['', '', '', ''],
          dtype='|S1')}}}
    """
    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_():
    act = dumpibw("mac-version3Dependent.ibw")
    exp = """
    {'version': 3,
     'wave': {'bin_header': {'checksum': -32334,
                             'formulaSize': 4,
                             'noteSize': 0,
                             'pictSize': 0,
                             'wfmSize': 126},
              'formula': ' K0',
              'note': '',
              'padding': array([], dtype=float64),
              'wData': array([], dtype=float32),
              'wave_header': {'aModified': 3,
                              'bname': 'version3Dependent',
                              'botFullScale': 0.0,
                              'creationDate': 0,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 23,
                              'fileName': 0,
                              'formula': 103408364,
                              'fsValid': 0,
                              'hsA': 1.0,
                              'hsB': 0.0,
                              'kindBits': '\\x00',
                              'modDate': 3001672861,
                              'next': 0,
                              'npnts': 10,
                              'srcFldr': 0,
                              'swModified': 1,
                              'topFullScale': 0.0,
                              'type': 2,
                              'useBits': '\\x00',
                              'wModified': 1,
                              'wUnused': array(['', ''],
          dtype='|S1'),
                              'waveNoteH': 0,
                              'whVersion': 0,
                              'xUnits': array(['', '', '', ''],
          dtype='|S1')}}}
     """
    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_04():
    act = dumpibw("mac-version5.ibw")
    exp = """
    {'version': 5,
     'wave': {'bin_header': {'checksum': -12033,
                             'dataEUnitsSize': 0,
                             'dimEUnitsSize': array([0, 0, 0, 0]),
                             'dimLabelsSize': array([64,  0,  0,  0]),
                             'formulaSize': 0,
                             'noteSize': 15,
                             'optionsSize1': 0,
                             'optionsSize2': 0,
                             'sIndicesSize': 0,
                             'wfmSize': 340},
              'data_units': '',
              'dimension_units': '',
              'formula': '',
              'labels': [['', 'Column0'], [], [], []],
              'note': 'This is a test.',
              'sIndices': array([], dtype=float64),
              'wData': array([ 5.,  4.,  3.,  2.,  1.], dtype=float32),
              'wave_header': {'aModified': 0,
                              'bname': 'version5',
                              'botFullScale': 0.0,
                              'creationDate': 3001252180,
                              'dFolder': 69554896,
                              'dLock': 0,
                              'dataEUnits': 0,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 27,
                              'dimEUnits': array([0, 0, 0, 0]),
                              'dimLabels': array([69554136, 0, 0, 0]),
                              'dimUnits': array([['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', '']],
          dtype='|S1'),
                              'fileName': 69554292,
                              'formula': 0,
                              'fsValid': 0,
                              'kindBits': '\\x00',
                              'modDate': 3001573601,
                              'nDim': array([5, 0, 0, 0]),
                              'next': 69555212,
                              'npnts': 5,
                              'sIndices': 0,
                              'sfA': array([ 1.,  1.,  1.,  1.]),
                              'sfB': array([ 0.,  0.,  0.,  0.]),
                              'srcFldr': -32349,
                              'swModified': 1,
                              'topFullScale': 0.0,
                              'type': 2,
                              'useBits': '\\x00',
                              'wModified': 0,
                              'waveNoteH': 69554032,
                              'whUnused': array([0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0]),
                              'whVersion': 1,
                              'whpad1': array(['', '', '', '', '', ''],
          dtype='|S1'),
                              'whpad2': 0,
                              'whpad3': 0,
                              'whpad4': 0}}}
     """
    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_05():
    act = dumpibw("mac-zeroPointWave.ibw")
    exp = """
    {'version': 5,
     'wave': {'bin_header': {'checksum': -15649,
                             'dataEUnitsSize': 0,
                             'dimEUnitsSize': array([0, 0, 0, 0]),
                             'dimLabelsSize': array([0, 0, 0, 0]),
                             'formulaSize': 0,
                             'noteSize': 0,
                             'optionsSize1': 0,
                             'optionsSize2': 0,
                             'sIndicesSize': 0,
                             'wfmSize': 320},
              'data_units': '',
              'dimension_units': '',
              'formula': '',
              'labels': [[], [], [], []],
              'note': '',
              'sIndices': array([], dtype=float64),
              'wData': array([], dtype=float32),
              'wave_header': {'aModified': 3,
                              'bname': 'zeroWave',
                              'botFullScale': 0.0,
                              'creationDate': 3001573964,
                              'dFolder': 69554896,
                              'dLock': 0,
                              'dataEUnits': 0,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 29,
                              'dimEUnits': array([0, 0, 0, 0]),
                              'dimLabels': array([0, 0, 0, 0]),
                              'dimUnits': array([['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', '']],
          dtype='|S1'),
                              'fileName': 0,
                              'formula': 0,
                              'fsValid': 0,
                              'kindBits': '\\x00',
                              'modDate': 3001573964,
                              'nDim': array([0, 0, 0, 0]),
                              'next': 0,
                              'npnts': 0,
                              'sIndices': 0,
                              'sfA': array([ 1.,  1.,  1.,  1.]),
                              'sfB': array([ 0.,  0.,  0.,  0.]),
                              'srcFldr': 0,
                              'swModified': 1,
                              'topFullScale': 0.0,
                              'type': 2,
                              'useBits': '\\x00',
                              'wModified': 1,
                              'waveNoteH': 0,
                              'whUnused': array([0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0]),
                              'whVersion': 1,
                              'whpad1': array(['', '', '', '', '', ''],
          dtype='|S1'),
                              'whpad2': 0,
                              'whpad3': 0,
                              'whpad4': 0}}}
     """
    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_06():
    act = dumpibw("win-double.ibw")
    exp = """
    {'version': 2,
     'wave': {'bin_header': {'checksum': 28962,
                             'noteSize': 0,
                             'pictSize': 0,
                             'wfmSize': 166},
              'note': '',
              'padding': array([], dtype=float64),
              'wData': array([ 5.,  4.,  3.,  2.,  1.]),
              'wave_header': {'aModified': 0,
                              'bname': 'double',
                              'botFullScale': 0.0,
                              'creationDate': 3001587842,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 0,
                              'fileName': 0,
                              'formula': 0,
                              'fsValid': 0,
                              'hsA': 1.0,
                              'hsB': 0.0,
                              'kindBits': '\\x00',
                              'modDate': 3001587842,
                              'next': 0,
                              'npnts': 5,
                              'srcFldr': 0,
                              'swModified': 0,
                              'topFullScale': 0.0,
                              'type': 4,
                              'useBits': '\\x00',
                              'wModified': 0,
                              'wUnused': array(['', ''],
          dtype='|S1'),
                              'waveNoteH': 0,
                              'whVersion': 0,
                              'xUnits': array(['', '', '', ''],
          dtype='|S1')}}}
     """
    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_07():
    act = dumpibw("win-textWave.ibw")
    exp = """
    {'version': 5,
     'wave': {'bin_header': {'checksum': 184,
                             'dataEUnitsSize': 0,
                             'dimEUnitsSize': array([0, 0, 0, 0]),
                             'dimLabelsSize': array([0, 0, 0, 0]),
                             'formulaSize': 0,
                             'noteSize': 0,
                             'optionsSize1': 0,
                             'optionsSize2': 0,
                             'sIndicesSize': 20,
                             'wfmSize': 338},
              'data_units': '',
              'dimension_units': '',
              'formula': '',
              'labels': [[], [], [], []],
              'note': '',
              'sIndices': array([ 4,  7,  8, 14, 18]),
              'wData': array(['Mary', 'had', 'a', 'little', 'lamb'],
          dtype='|S6'),
              'wave_header': {'aModified': 0,
                              'bname': 'text0',
                              'botFullScale': 0.0,
                              'creationDate': 3001571199,
                              'dFolder': 8108612,
                              'dLock': 0,
                              'dataEUnits': 0,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 32,
                              'dimEUnits': array([0, 0, 0, 0]),
                              'dimLabels': array([0, 0, 0, 0]),
                              'dimUnits': array([['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', '']],
          dtype='|S1'),
                              'fileName': 7814472,
                              'formula': 0,
                              'fsValid': 0,
                              'kindBits': '\\x00',
                              'modDate': 3001571215,
                              'nDim': array([5, 0, 0, 0]),
                              'next': 0,
                              'npnts': 5,
                              'sIndices': 8133100,
                              'sfA': array([ 1.,  1.,  1.,  1.]),
                              'sfB': array([ 0.,  0.,  0.,  0.]),
                              'srcFldr': -1007,
                              'swModified': 0,
                              'topFullScale': 0.0,
                              'type': 0,
                              'useBits': '\\x00',
                              'wModified': 1,
                              'waveNoteH': 0,
                              'whUnused': array([0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0]),
                              'whVersion': 1,
                              'whpad1': array(['', '', '', '', '', ''],
          dtype='|S1'),
                              'whpad2': 0,
                              'whpad3': 0,
                              'whpad4': 0}}}
     """
    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_08():
    act = dumpibw("win-version2.ibw")
    exp = """
    {'version': 2,
     'wave': {'bin_header': {'checksum': 1047,
                             'noteSize': 15,
                             'pictSize': 0,
                             'wfmSize': 146},
              'note': 'This is a test.',
              'padding': array([], dtype=float64),
              'wData': array([ 5.,  4.,  3.,  2.,  1.], dtype=float32),
              'wave_header': {'aModified': 0,
                              'bname': 'version2',
                              'botFullScale': 0.0,
                              'creationDate': 3001251979,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 0,
                              'fileName': 0,
                              'formula': 0,
                              'fsValid': 0,
                              'hsA': 1.0,
                              'hsB': 0.0,
                              'kindBits': '\\x00',
                              'modDate': 3001573594,
                              'next': 0,
                              'npnts': 5,
                              'srcFldr': 0,
                              'swModified': 0,
                              'topFullScale': 0.0,
                              'type': 2,
                              'useBits': '\\x00',
                              'wModified': 0,
                              'wUnused': array(['', ''],
          dtype='|S1'),
                              'waveNoteH': 0,
                              'whVersion': 0,
                              'xUnits': array(['', '', '', ''],
          dtype='|S1')}}}
     """
    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_09():
    act = dumpibw("win-version5.ibw")
    exp = """
    {'version': 5,
     'wave': {'bin_header': {'checksum': 13214,
                             'dataEUnitsSize': 0,
                             'dimEUnitsSize': array([0, 0, 0, 0]),
                             'dimLabelsSize': array([64,  0,  0,  0]),
                             'formulaSize': 0,
                             'noteSize': 15,
                             'optionsSize1': 0,
                             'optionsSize2': 0,
                             'sIndicesSize': 0,
                             'wfmSize': 340},
              'data_units': '',
              'dimension_units': '',
              'formula': '',
              'labels': [['', 'Column0'], [], [], []],
              'note': 'This is a test.',
              'sIndices': array([], dtype=float64),
              'wData': array([ 5.,  4.,  3.,  2.,  1.], dtype=float32),
              'wave_header': {'aModified': 0,
                              'bname': 'version5',
                              'botFullScale': 0.0,
                              'creationDate': 3001252180,
                              'dFolder': 8108612,
                              'dLock': 0,
                              'dataEUnits': 0,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 30,
                              'dimEUnits': array([0, 0, 0, 0]),
                              'dimLabels': array([8138784, 0, 0, 0]),
                              'dimUnits': array([['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', '']],
          dtype='|S1'),
                              'fileName': 8131824,
                              'formula': 0,
                              'fsValid': 0,
                              'kindBits': '\\x00',
                              'modDate': 3001573601,
                              'nDim': array([5, 0, 0, 0]),
                              'next': 8125236,
                              'npnts': 5,
                              'sIndices': 0,
                              'sfA': array([ 1.,  1.,  1.,  1.]),
                              'sfB': array([ 0.,  0.,  0.,  0.]),
                              'srcFldr': -1007,
                              'swModified': 0,
                              'topFullScale': 0.0,
                              'type': 2,
                              'useBits': '\\x00',
                              'wModified': 1,
                              'waveNoteH': 8131596,
                              'whUnused': array([0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0]),
                              'whVersion': 1,
                              'whpad1': array(['', '', '', '', '', ''],
          dtype='|S1'),
                              'whpad2': 0,
                              'whpad3': 0,
                              'whpad4': 0}}}
    """
    assert_equal_dump_no_whitespace_no_byte(act, exp)


def test_ibw_10():
    act = dumpibw("win-zeroPointWave.ibw")

    exp = """
    {'version': 5,
     'wave': {'bin_header': {'checksum': 27541,
                             'dataEUnitsSize': 0,
                             'dimEUnitsSize': array([0, 0, 0, 0]),
                             'dimLabelsSize': array([0, 0, 0, 0]),
                             'formulaSize': 0,
                             'noteSize': 0,
                             'optionsSize1': 0,
                             'optionsSize2': 0,
                             'sIndicesSize': 0,
                             'wfmSize': 320},
              'data_units': '',
              'dimension_units': '',
              'formula': '',
              'labels': [[], [], [], []],
              'note': '',
              'sIndices': array([], dtype=float64),
              'wData': array([], dtype=float32),
              'wave_header': {'aModified': 3,
                              'bname': 'zeroWave',
                              'botFullScale': 0.0,
                              'creationDate': 3001573964,
                              'dFolder': 8108612,
                              'dLock': 0,
                              'dataEUnits': 0,
                              'dataUnits': array(['', '', '', ''],
          dtype='|S1'),
                              'depID': 31,
                              'dimEUnits': array([0, 0, 0, 0]),
                              'dimLabels': array([0, 0, 0, 0]),
                              'dimUnits': array([['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', ''],
           ['', '', '', '']],
          dtype='|S1'),
                              'fileName': 8125252,
                              'formula': 0,
                              'fsValid': 0,
                              'kindBits': '\\x00',
                              'modDate': 3001573964,
                              'nDim': array([0, 0, 0, 0]),
                              'next': 8133140,
                              'npnts': 0,
                              'sIndices': 0,
                              'sfA': array([ 1.,  1.,  1.,  1.]),
                              'sfB': array([ 0.,  0.,  0.,  0.]),
                              'srcFldr': -1007,
                              'swModified': 0,
                              'topFullScale': 0.0,
                              'type': 2,
                              'useBits': '\\x00',
                              'wModified': 1,
                              'waveNoteH': 0,
                              'whUnused': array([0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0]),
                              'whVersion': 1,
                              'whpad1': array(['', '', '', '', '', ''],
          dtype='|S1'),
                              'whpad2': 0,
                              'whpad3': 0,
                              'whpad4': 0}}}
    """
    assert_equal_dump_no_whitespace_no_byte(act, exp)
