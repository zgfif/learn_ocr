from app.text_blocks import TextBlocks
from PIL import Image



def test_text_blocks():
    image = Image.open(fp='./IMG_4731.png')

    found = TextBlocks(image=image).find()
    
    expected: list = [
        {'start_coord': (37, 50), 'end_coord': (1200, 100)},
        {'start_coord': (37, 100), 'end_coord': (1200, 100)},
        {'start_coord': (37, 150), 'end_coord': (1200, 100)},
        {'start_coord': (37, 200), 'end_coord': (1200, 100)},
    ]

    assert expected == found
