from pathlib import Path
from pygor.binarywave import load_ibw
from pygor import load

TEST_DATA_DIRECTORY = Path(__file__).parent / "data"


def test_windows_ibw():
    try:
        igor_waves = [
            load_ibw(str(TEST_DATA_DIRECTORY / filename))
            for filename in [
                "win-double.ibw",
                "win-textWave.ibw",
                "win-version2.ibw",
                "win-version5.ibw",
                "win-zeroPointWave.ibw",
            ]
        ]
        assert True
    except Exception:
        assert False, "Loading Igor Binary Waves ran into an exception."


def test_load_pxp():
    try:
        load(str(TEST_DATA_DIRECTORY / "polar-graphs-demo.pxp"))
        assert True
    except Exception:
        assert False, "Loading PXP ran into an exception."
