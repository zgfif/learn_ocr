from app.group_rectangles import group_rectangles
import numpy as np
from pytest import raises



def test_group_rectangles():
    rectangles: list[tuple] = [
        (37, 893, 120, 120), 
        (37, 893, 120, 120),
        (37, 894, 120, 120), 
        (37, 894, 120, 120), 
        (37, 1136, 120, 120),
        (37, 1136, 120, 120),
        (37, 1137, 120, 120),
        (37, 1137, 120, 120)
    ]
    got = group_rectangles(rectangles=rectangles)
    assert isinstance(got, np.ndarray)
    assert len(got) == 2



def test_group_rectangles_raise_error():
    rectangles: list[tuple] = [
        (37, 893, 120, 120), 
        (37, 893, 120, 120),
        (37, 894, 120, 120), 
        (37, 894, 120, 120), 
        (37, 1136, 120, 120),
        (37, 1136, 120, 120),
        (37, 1137, 120, 120),
        (37, 1137, 120, 120)
    ]
    with raises(ValueError) as excinfo:
        group_rectangles(rectangles=rectangles, grouping_threshold=-1)
    assert 'grouping_threshold must be >= 0' in str(excinfo.value)



def test_group_rectangles_when_empty_():
    rectangles: list[tuple] = []
    got = group_rectangles(rectangles=rectangles)
    assert isinstance(got, np.ndarray)
    assert len(got) == 0