import cv2
import numpy



class ViewImage:
    def __init__(self, image: numpy.ndarray) -> None:
        self.image = image


    def perform(self) -> None:
        """
        Show image on screen.
        """
        if self.image is None:
            return
        
        cv2.imshow("My Image Window", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
