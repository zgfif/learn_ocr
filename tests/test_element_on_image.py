# from app.impage import Image



# ticked_path: str = './img/ticked.png'
# unticked_path: str = './img/unticked.png'


# def test_image_0_has_no_ticked_and_no_unticked():
#     image_path = './tests/fixtures/parts/part_img_0.png'
#     assert Image(image_path=image_path).has_element(element_path=ticked_path) is False
#     assert Image(image_path=image_path).has_element(element_path=unticked_path) is False


# def test_image_1_has_only_unticked():
#     image_path = './tests/fixtures/parts/part_img_1.png'
#     assert Image(image_path=image_path).has_element(element_path=ticked_path) is False
#     assert Image(image_path=image_path).has_element(element_path=unticked_path) is True


# def test_image_2_has_only_ticked():
#     image_path = './tests/fixtures/parts/part_img_2.png'
#     assert Image(image_path=image_path).has_element(element_path=ticked_path) is True
#     assert Image(image_path=image_path).has_element(element_path=unticked_path) is False


# def test_image_3_has_only_unticked():
#     image_path = './tests/fixtures/parts/part_img_3.png'
#     assert Image(image_path=image_path).has_element(element_path=ticked_path) is False
#     assert Image(image_path=image_path).has_element(element_path=unticked_path) is True
