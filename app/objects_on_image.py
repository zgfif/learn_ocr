import cv2
import numpy as np



class ObjectsOnImage:
    THRESHOLD: float = 0.999
    PATTERN_SIZE: tuple = (150, 150)
    GROUP_THRESHOLD: int = 1
    EPS: float = 0.2


    def __init__(self, image_path: str, pattern_path: str) -> None:
        self.image_path = image_path
        self.pattern_path =pattern_path


    def coordinates(self) -> list[tuple[int, int]]:
        """
        Return coordinates of found objects on image.
        """
        elements = []
 
        image = cv2.imread(self.image_path, 0)
        # print(type(image), 'image type')
        template = cv2.imread(self.pattern_path, 0)

        result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

        found = np.where(result > self.THRESHOLD)

        rects = []
        h, w = self.PATTERN_SIZE

        for pt in zip(*found[::-1]):
            # Формируем список прямоугольников [x, y, w, h]
            rects.append([int(pt[0]), int(pt[1]), w, h])
            rects.append([int(pt[0]), int(pt[1]), w, h]) # Добавляем дважды (нужно для работы функции)


        # Группируем близкие прямоугольники
        # groupThreshold=1 (объединять, если наложились), eps=0.2 (насколько близко)
        grouped_rects, weights = cv2.groupRectangles(rects, groupThreshold=self.GROUP_THRESHOLD, eps=self.EPS)

        for (x, y, w, h) in grouped_rects:
            # print(f"Реальный объект найден в: {x}, {y}")
            tpl = int(x), int(y)
            elements.append(tpl)
        return elements


