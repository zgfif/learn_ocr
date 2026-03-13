from app.fetch_object_coordinates import fetch_object_coordinates
from app.load_image import load_image



def test_one_object_on_image():
    image = load_image('./tests/fixtures/IMG_4731.png')
    object_pattern = load_image('./img/checked.png')
    assert image is not None
    assert object_pattern is not None
    got = fetch_object_coordinates(image=image, pattern=object_pattern)
    expected = [(37, 404),]
    assert got == expected


def test_two_objects_on_image():
    image = load_image('./tests/fixtures/IMG_4732.png')
    object_pattern = load_image('./img/checked.png')
    assert image is not None
    assert object_pattern is not None
    got = fetch_object_coordinates(image=image, pattern=object_pattern)
    expected = [(37, 894), (37, 1136),]
    assert got == expected


def test_when_invalid_path_to_image():
    image = load_image('')
    object_pattern = load_image('./img/youtube_logo.jpg')
    assert image is None
    assert object_pattern is not None
    got = fetch_object_coordinates(image=image, pattern=object_pattern)
    assert got is None


def test_when_invalid_path_to_pattern():
    image = load_image('./tests/fixtures/IMG_4732.png')
    object_pattern = load_image('')
    assert image is not None
    assert object_pattern is None
    got = fetch_object_coordinates(image=image, pattern=object_pattern)
    assert got is None


def test_when_can_not_find_pattern():
    image = load_image('./tests/fixtures/IMG_4732.png')
    object_pattern = load_image('./img/youtube_logo.jpg')
    assert image is not None
    assert object_pattern is not None
    got = fetch_object_coordinates(image=image, pattern=object_pattern)
    assert got == []


def test_bug_from_4731():
    image = load_image('./tests/fixtures/part_with_bug.png')
    object_pattern = load_image('./img/unchecked.png')
    got = fetch_object_coordinates(image=image, pattern=object_pattern)
    assert got is not None
    assert len(got) == 1
