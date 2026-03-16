from app.fetch_locations import fetch_locations
import numpy as np
from pytest import raises


def test_fetch_locations():
    match_map = np.array([
        [0.1, 0.14, 0.7],
        [0.2, 0.15, 0.3],
        [0.55, 0.43, 0.21],
        [0.9, 0.65, 0.29],
    ])
    got = fetch_locations(match_map=match_map, threshold=0.5)

    assert isinstance(got, tuple)
    
    expected = (
            np.array([0, 2, 3, 3]),
            np.array([2, 0, 0, 1]),
    )
    assert np.array_equal(expected[0], got[0])
    assert np.array_equal(expected[1], got[1])



def test_fetch_locations_raise_value_erorr():
    match_map = np.array([
        [0.1, 0.14, 0.7],
        [0.2, 0.15, 0.3],
        [0.55, 0.43, 0.21],
        [0.9, 0.65, 0.29],
    ])

    with raises(ValueError) as excinfo:
        fetch_locations(match_map=match_map, threshold=1.01)
    assert 'Threshold must be in range 0..1' in str(excinfo.value)