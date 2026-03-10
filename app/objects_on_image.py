import cv2
import numpy as np
from numpy import ndarray
from app.types import Coordinates



class ObjectsOnImage:
    THRESHOLD: float = 0.99
    PATTERN_SIZE: tuple = (120, 120)
    GROUP_THRESHOLD: int = 1
    EPS: float = 0.2


    def __init__(self, image_path: str, pattern_path: str) -> None:
        self.image = self._image(image_path)
        self.pattern = self._image(pattern_path)


    def coordinates(self) -> list[Coordinates]:
        """
        Return coordinates of found objects on image.
        """
        elements: list = []

        if self.image is None or self.pattern is None:
            return elements

        result = cv2.matchTemplate(self.image, self.pattern, cv2.TM_CCOEFF_NORMED)

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
    

    def _image(self, path: str) -> ndarray | None:
        """
        Return ndarray by image path if no image return None.
        """
        return cv2.imread(filename=path, flags=0)
