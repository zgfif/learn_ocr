from app.types import Coordinates, ImageType
from app.point import Point


class Cropping:
    DEFAULT_CROPPED_NAME: str = 'cropped.png'


    def __init__(self, image: ImageType) -> None:
        self.image = image


    def perform(self,
                start_coord: Point,
                end_coord: Point,
                save_image: bool = True
        ) -> ImageType:
        """
        Crop image. And cropped image could be saved.
        """
        coordinates = (start_coord.x, start_coord.y, end_coord.x ,end_coord.y)
        self.image = self.image.crop(coordinates)
        if save_image:
            self.image.save(self.DEFAULT_CROPPED_NAME)
        return self.image
