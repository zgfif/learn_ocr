import pytest
import numpy as np
from pathlib import Path
from app.load_image import load_image



FIXTURES_DIR = Path(__file__).parent / 'fixtures'



@pytest.mark.parametrize('path, is_nparray', 
    [
        ('', False),
        ('./some/incorrect.png', False),
        (str(FIXTURES_DIR / 'IMG_4731.png'), True),
    ],
    ids=('an_empty_path', 'incorrect_path', 'valid_path')
)
def test_load_image(path, is_nparray):
    got = load_image(path=path)
    if is_nparray:
        assert isinstance(got, np.ndarray) == is_nparray, f'Expected np.ndarray for path: {path}.'
    else:
        assert got is None, f'Expected None for invalid path: {path}.'
