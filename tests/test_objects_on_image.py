from app.objects_on_image import ObjectsOnImage



def test_one_object_on_image():
    image_path = './tests/fixtures/IMG_4731.png'
    pattern_path = './img/checked.png'

    got = ObjectsOnImage(
        image_path=image_path, 
        pattern_path=pattern_path
    ).coordinates()

    expected = [(37, 404),]
    assert got == expected



def test_two_objects_on_image():
    image_path = './tests/fixtures/IMG_4732.png'
    pattern_path = './img/checked.png'

    got = ObjectsOnImage(
        image_path=image_path, 
        pattern_path=pattern_path
    ).coordinates()

    expected = [(37, 894), (37, 1136),]
    assert got == expected



def test_when_invalid_path_to_image():
    # image_path = 'IMG_4732.png'
    image_path = ''
    pattern_path = './img/youtube_logo.jpg'

    got = ObjectsOnImage(
        image_path=image_path, 
        pattern_path=pattern_path
    ).coordinates()

    expected = []
    assert got == expected


def test_when_invalid_path_to_pattern():
    image_path = './tests/fixtures/IMG_4732.png'
    pattern_path = ''

    got = ObjectsOnImage(
        image_path=image_path, 
        pattern_path=pattern_path
    ).coordinates()

    expected = []
    assert got == expected


def test_when_can_not_find_pattern():
    image_path = './tests/fixtures/IMG_4732.png'
    pattern_path = './img/youtube_logo.jpg'

    got = ObjectsOnImage(
        image_path=image_path, 
        pattern_path=pattern_path
    ).coordinates()

    expected = []
    assert got == expected


def test_bug_from_4731():
    image_path='./tests/fixtures/part_with_bug.png' 
    pattern_path='./img/unchecked.png'
    
    got = ObjectsOnImage(
        image_path=image_path, 
        pattern_path=pattern_path
    ).coordinates()
    
    assert len(got) == 1
