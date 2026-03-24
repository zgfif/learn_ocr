from cv2.typing import MatLike

from app.find_template_coordinates import find_template_coordinates
from app.option import Option
from app.question import Question
from app.extract_text import extract_text
from app.extract_text_from_option_area import extract_text_from_option_area



def extract_question(
    images: list[MatLike], 
    ticked_template: MatLike | None, 
    unticked_template: MatLike | None
    ) -> Question | None:
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
    # check our images if no images return None
    if not images:
        return None
    
    # if we have no templates we raise Value error
    if ticked_template is None or unticked_template is None:
        raise ValueError('Could not load patterns')
    
    # initialize our Question and options list.
    question: str = ''
    options: list[Option] = []


    for image in images:        
        if image is None:
            continue

        ticked = find_template_coordinates(
            image=image, 
            template=ticked_template
        )
        unticked = find_template_coordinates(
            image=image, 
            template=unticked_template
        )

        has_ticked = bool(ticked)
        has_unticked =  bool(unticked)
    
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
