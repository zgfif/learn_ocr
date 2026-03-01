from app.image_to_data import ImageToData



def test_image_to_data():
    data = ImageToData(image_path='./IMG_4731.png').transform()
    print(data)
    assert isinstance(data, dict)
