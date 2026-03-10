# import cv2
# import pytesseract


# def test_something():
#     # Load image
#     image = cv2.imread('./IMG_4731.png', 0)
#     if image is None:
#         return
    
#     print(type(image))
#     print(image[0], 'image[0]')
#     # Convert to RGB (Tesseract works better with RGB)
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Get bounding box data, specifying output type 'dict' or 'data.frame'
#     # 'page_iterator' level gives block info
#     data = pytesseract.image_to_data(image_rgb, output_type=pytesseract.Output.DICT)
#     print('-----/'*10)
#     for key in data.keys():
#         print(key)
#     # Iterate through the detected blocks and draw rectangles
#     n_boxes = len(data['level'])
#     for i in range(n_boxes):
#         # Filter for relevant blocks (e.g., level 1 is page, level 2 is block)
#         if data['level'][i] == 2:
#             (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
#             cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     # Display the result
#     cv2.imshow('Text Blocks', image)
#     cv2.waitKey(0)
