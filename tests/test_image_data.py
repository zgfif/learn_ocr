from app.image_data import ImageData



def test_image_data():
    data = ImageData(image_path='./IMG_4731.png').extract()
    print(data)
    print(len(data['level']), 'count of level list')
    print(len(data['page_num']), 'page num')
    print(len(data['block_num']), 'block num')
    assert isinstance(data, dict)
