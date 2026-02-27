from app.text import Text
from tests.fixtures.img_4731_full_text import img_4731_full_text
from tests.fixtures.img_4732_full_text import img_4732_full_text
from PIL import Image



def test_extracting_from_first_image():
    img = Image.open(fp='./IMG_4731.png')
    got = Text(image=img, lang='eng').extract()
    assert got == img_4731_full_text


def test_extracting_from_the_second_image():
    img = Image.open(fp='./IMG_4732.png')
    got = Text(image=img, lang='eng').extract()
    assert got == img_4732_full_text
