import cv2
from pathlib import Path
from cv2.typing import MatLike



def load_image(path: str) -> MatLike | None:
    """
    Load image by path.

    Parameters
    ----------
    path : str
        Path to image.

    Returns
    ------
    MatLike | None
        Loaded image as a NumPy array, or None if the image cannot be loaded.
    """
    if not Path(path).exists():
        return None
    return cv2.imread(path)
