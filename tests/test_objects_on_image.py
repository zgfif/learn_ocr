from app.objects_on_image import ObjectsOnImage



def test_one_object_on_image():
    image_path = 'IMG_4731.png'
    pattern_path = './img/checked.png'

    got = ObjectsOnImage(
        image_path=image_path, 
        pattern_path=pattern_path
    ).coordinates()

    expected = [(37, 404),]
    assert got == expected



def test_two_objects_on_image():
    image_path = 'IMG_4732.png'
    pattern_path = './img/checked.png'

    got = ObjectsOnImage(
        image_path=image_path, 
        pattern_path=pattern_path
    ).coordinates()

    expected = [(37, 894), (37, 1136),]
    assert got == expected


