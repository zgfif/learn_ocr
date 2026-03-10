from tests.fixtures.img_4731_image_dict import image_data
from app.lines import Lines



def test_lines():
    line_blocks = Lines(data=image_data).coordinates()
    assert len(line_blocks) == 14
