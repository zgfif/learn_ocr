from app.extract_option_text import extract_option_text
from app.load_image import load_image
import pytest



def test_extract_option_text():
    image = load_image(path='./tests/fixtures/parts/part_img_1.png')
    if image is None:
        pytest.skip('Image is None, so skip the test.')

    expected = 'Anordnung zum erneuten Ablegen einer theoretischen Fahrerlaubnisprüfung'

    got = extract_option_text(image=image)

    assert got == expected