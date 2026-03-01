from app.text_blocks import TextBlocks
from PIL import Image



def test_text_blocks():
    image = Image.open(fp='./IMG_4731.png')

    found = TextBlocks(image=image).find()
    
    expected: list = [
        {'pt_1': (37, 50), 'pt_2': (1200, 100)},
        {'pt_1': (37, 100), 'pt_2': (1200, 100)},
        {'pt_1': (37, 150), 'pt_2': (1200, 100)},
        {'pt_1': (37, 200), 'pt_2': (1200, 100)},
    ]

    assert expected == found
