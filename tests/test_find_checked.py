# import cv2
# import numpy as np

# template_path = './img/checked.png'
# image_path = './IMG_4731.png'
# thredhold = 0.999


# def test_find_checked():
#     image = cv2.imread(image_path, 0)
#     template = cv2.imread(template_path, 0)

#     result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

#     print(type(result))
#     found = np.where(result > thredhold)
#     print(found)

#     points = list(zip(*found[::-1]))
#     print(points)

#     rects = []
#     h, w = (150, 150) # Предположим, размер вашего шаблона 20x20 пикселей

#     for pt in zip(*found[::-1]):
#         # Формируем список прямоугольников [x, y, w, h]
#         rects.append([int(pt[0]), int(pt[1]), w, h])
#         rects.append([int(pt[0]), int(pt[1]), w, h]) # Добавляем дважды (нужно для работы функции)


#     # Группируем близкие прямоугольники
#     # groupThreshold=1 (объединять, если наложились), eps=0.2 (насколько близко)
#     grouped_rects, weights = cv2.groupRectangles(rects, groupThreshold=1, eps=0.2)

#     elements = []
#     for (x, y, w, h) in grouped_rects:
#         print(f"Реальный объект найден в: {x}, {y}")
#         tpl = int(x), int(y)
#         elements.append(tpl)

    
#     assert len(elements) == 2
#     assert elements[0] == (37, 894)
#     assert elements[1] == (37, 1136)
