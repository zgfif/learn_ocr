from app.image_text import ImageText


EXPECTED2: str = """Anordnung zur Teilnahme an einem
Aufbauseminar für Fahranfänger
"""


def test_image1_text():
    expected: str = '2 Jahre\n'

    image_path: str = './IMG_4731.png'
    start_coord: tuple = (37 + 170, 404)
    end_coord: tuple = (37 + 1200, 404 + 150)

    got = ImageText(
        image_path=image_path, 
        start_coord=start_coord, 
        end_coord=end_coord
    ).fetch()

    assert expected == got



def test_image2_text():
    image_path: str = './IMG_4732.png'
    start_coord: tuple = (37 + 150, 894)
    end_coord: tuple = (37 + 1200, 894 + 150)

    got = ImageText(
        image_path=image_path, 
        start_coord=start_coord, 
        end_coord=end_coord
    ).fetch()

    assert EXPECTED2 == got


EXPECTED3 = """Wie lange dauert normalerweise die Probezeit?

n 2 Jahre
Ü 1 Jahr
Ü 3 Jahre
"""

def test_question_extracting_text1():
    image_path: str = './IMG_4731.png'

    got = ImageText(image_path=image_path, start_coord=(0, 215), end_coord=(1286, 2235)).fetch()

    assert EXPECTED3 == got




def test_question_extracting_text2():
    image_path: str = './IMG_4732.png'

    got = ImageText(image_path=image_path, start_coord=(0, 215), end_coord=(1286, 2235)).fetch()

    assert EXPECTED3 == got

