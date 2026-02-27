from app.types import Coordinates, ImageType



class Cropping:
    DEFAULT_CROPPED_NAME: str = 'cropped.png'


    def __init__(self, image: ImageType) -> None:
        self.image = image


    def perform(self,
                start_coord: Coordinates,
                end_coord: Coordinates,
                save_image: bool = True
        ) -> ImageType:
        """
        Crop image. And cropped image could be saved.
        """
        coordinates = *start_coord, *end_coord
        self.image = self.image.crop(coordinates)
        if save_image:
            self.image.save(self.DEFAULT_CROPPED_NAME)
        return self.image
