from tests.fixtures.img_4731_image_dict import image_data
from app.lines import LineBlocks
import cv2
from app.rectangle import Rectangle
from app.view_image import ViewImage



def test_line_blocks():
    line_blocks = LineBlocks(data=image_data).fetch()
    image = cv2.imread(filename='./IMG_4731.png')
    if image is None:
        return
    for line_block in line_blocks:
        image = Rectangle(image=image).draw(*line_block)
    
    ViewImage(image=image).perform()

    assert len(line_blocks) == 5