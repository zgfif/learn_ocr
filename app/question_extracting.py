from numpy import ndarray
from app.option import Option
from app.fetch_object_coordinates import ObjectsOnImage
from pytesseract import image_to_string
from app.cropping import Cropping
import cv2
from app.point import Point
from app.view_image import ViewImage
from app.question import Question
from app.normalize_string import normalize_string



class QuestionExtracting:
    def __init__(self, images: list[str]) -> None:
        self.images = images


    def perform(self) -> Question:
        """
        Return the list of options.
        """
        question: str = ''
        options: list[Option] = []

        for image in self.images:
            ticked_coordinates = ObjectsOnImage(
                image_path=image, 
                pattern_path='./img/checked.png').coordinates()

            unticked_coordinates = ObjectsOnImage(
                image_path=image, 
                pattern_path='./img/unchecked.png').coordinates()
            # print(image, 'image')
            # print('ticked_coordinates', ticked_coordinates)
            # print('unticked_coordinates', unticked_coordinates)
            # print('***' * 5)
            if not ticked_coordinates and not unticked_coordinates:
                question = image_to_string(image=image, lang='deu')
                question = normalize_string(question)
                # print('~~~~', question, '****')
                continue
            if ticked_coordinates:
                correctness = True
            else:
                correctness = False
            
            cv_image = cv2.imread(filename=image)
            if cv_image is None:
                continue
            without_box = Cropping(image=cv_image).perform(pt1=Point(220, 0), pt2=Point(cv_image.shape[1], cv_image.shape[0]))
            option_text = normalize_string(image_to_string(image=without_box, lang='deu'))
            option = Option(text=option_text, correctness=correctness)
            options.append(option)
        
        return Question(
            text=question,
            options=options
        )

