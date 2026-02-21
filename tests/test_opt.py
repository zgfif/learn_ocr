import cv2
import numpy as np

# Загружаем область с ответами (уже в ЧБ и инвертированную)
# Где 255 — это пометка, 0 — пустота
question_roi = cv2.imread('IMG_4731.png', 0)

# Допустим, мы разделили строку на 5 равных частей (варианты A, B, C, D, E)
options = np.array_split(question_roi, 5, axis=1)

bubbled_index = None
max_pixels = 0

for i, opt in enumerate(options):
    # Считаем количество белых пикселей в каждом кружке
    total_pixels = cv2.countNonZero(opt)
    
    if total_pixels > max_pixels:
        max_pixels = total_pixels
        bubbled_index = i

print(f"Пользователь выбрал вариант под индексом: {bubbled_index}")