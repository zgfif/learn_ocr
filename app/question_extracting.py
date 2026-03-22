from app.find_template_coordinates import find_template_coordinates
from app.option import Option
from app.question import Question
from app.extract_text import extract_text
from app.extract_text_from_option_area import extract_text_from_option_area
from cv2.typing import MatLike




class QuestionExtracting:
    def __init__(self, 
        images: list[MatLike], 
        ticked_template: MatLike, 
        unticked_template: MatLike
    ) -> None:
        self.images = images
        self.ticked_template = ticked_template
        self.unticked_template = unticked_template



    def extract(self) -> Question | None:
        """
        Extract question text and options from images.
        
        Parameters
        ----------
        images : list[str]
            The list of paths to images.
        ticked_template : MatLike
            template to detect ticked element.
        unticked_template : MatLike
            template to detect unticked element.

        Returns
        -------
        Question | None
            Question object if find question text and options. Else return None.
        """
        if not self.images:
            return None
        
        if self.ticked_template is None or self.unticked_template is None:
            raise ValueError('Could not load patterns')
        
        question: str = ''
        options: list[Option] = []

        for image in self.images:        
            if image is None:
                continue

            has_ticked = self._has_ticked(image)
            has_unticked = self._has_unticked(image)
    
            if not has_ticked and not has_unticked:
                if not question:
                    question = extract_text(image=image)
                continue

            if has_ticked and not has_unticked:
                correctness = True
            elif has_unticked and not has_ticked:
                correctness = False
            else:
                continue

            options.append(
                Option(
                    text=extract_text_from_option_area(image), 
                    correctness=correctness
                )
            )
        
        if not question or not options:
            return None
        
        return Question(
            text=question,
            options=options
        )



    def _has_ticked(self, image: MatLike) -> bool:
        return bool(
            find_template_coordinates(
                image=image, 
                template=self.ticked_template
            )
        )



    def _has_unticked(self, image: MatLike) -> bool:
        return bool(
            find_template_coordinates(
                image=image, 
                template=self.unticked_template
            )
        )
    