from cv2.typing import MatLike
from app.extract_text import extract_text


def extract_question_text(image: MatLike) -> str:
    return extract_text(image)
