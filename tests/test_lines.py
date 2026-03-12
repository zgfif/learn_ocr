from tests.fixtures.img_4731_image_dict import image_data
from app.fetch_lines import fetch_lines



def test_fetch_lines():
    lines = fetch_lines(data=image_data)
    assert isinstance(lines, list)
    assert len(lines) == 14
