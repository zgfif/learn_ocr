from app.find_template_coordinates import find_template_coordinates
from app.option import Option
from app.question import Question
from app.load_image import load_image
from app.extract_text import extract_text
from app.extract_option_text import extract_option_text



class QuestionExtracting:
    def __init__(self, images: list[str]) -> None:
        self.images = images


    def perform(self) -> Question:
        """
        Return the Question object.
        """
        question: str = ''
        options: list[Option] = []

        ticked_template = load_image('./img/ticked.png')
        unticked_template = load_image('./img/unticked.png')

        for image in self.images:
            image = load_image(image)
            
            if image is None:
                continue

            # list of coordinates of ticked pattern
            ticked_coordinates = find_template_coordinates(
                image=image,
                template=ticked_template
            )

            # list of coordinates of unticked pattern
            unticked_coordinates = find_template_coordinates(
                image=image, 
                template=unticked_template
            )

            # if images hasn't neither ticked nor unicked elements this is question.
            if not ticked_coordinates and not unticked_coordinates:
                question = extract_text(image=image)
                continue

            correctness = True if ticked_coordinates else False

            option = Option(
                text=extract_option_text(image), 
                correctness=correctness
            )
            options.append(option)
        
        return Question(
            text=question,
            options=options
        )


