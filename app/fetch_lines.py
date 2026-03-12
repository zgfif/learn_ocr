from app.point import Point
from app.area import Area
from app.ocr_data import OCRData


TESS_LINE_LEVEL: int = 4


def fetch_lines(data: OCRData) -> list[Area]:
    """
    Return bounding boxes of lines detected by Tesseract.
    """
    lines: list[Area] = []

    for level, x, y, w, h in zip(data.level, data.left, data.top, data.width, data.height):
        if level != TESS_LINE_LEVEL:
            continue        
        lines.append(
            Area(
                Point(x, y), 
                Point(x + w, y + h)
            )
        )
    return lines
