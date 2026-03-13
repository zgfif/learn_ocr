from cv2 import imread
from cv2.typing import MatLike



def load_image(path: str) -> MatLike | None:
    """
    Load image by path.
    """
    return imread(path)
