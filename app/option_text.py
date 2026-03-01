from pytesseract import image_to_string
from PIL import Image



class ImageText:
    LANG: str = 'deu'
    DEFAULT_CROPPED_NAME: str = 'cropped.png'


    def __init__(
            self, 
            image_path: str, 
            start_coord: tuple[int, int] | None = None, 
            end_coord: tuple[int, int] | None = None
        ) -> None:
        self.image = Image.open(fp=image_path)
        self.start_coord = start_coord
        self.end_coord = end_coord


    def fetch(self) -> str:
        """Return text from image."""
        self.crop()
        return image_to_string(image=self.image, lang=self.LANG)
        

    def crop(self, save_cropped: bool = True) -> None:
        """Crop image. And cropped image could be saved."""
        if not self.start_coord or not self.end_coord:
            return
        coordinates = *self.start_coord, *self.end_coord
        self.image = self.image.crop(coordinates)
        if not save_cropped:
            return
        self.image.save(self.DEFAULT_CROPPED_NAME)
