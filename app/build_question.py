from cv2.typing import MatLike
from app.process_image_part import process_image_part
from app.load_image import load_image
from app.option import Option
from app.question import Question


ERR_CAN_NOT_LOAD_TEMPLATES: str = 'Can not load templates.'
ERR_CAN_NOT_PROCESS_IMAGE: str = 'Can not process image.'
ERR_NO_OPITONS = 'No options found.'
ERR_NO_QUESTION = 'No question found.'


ticked_template = load_image('./img/ticked.png')
unticked_template = load_image('./img/ticked.png')



def build_question(
        image_parts: list[MatLike], 
        ticked_template: MatLike, 
        unticked_template: MatLike
) -> Question:
    """
    Build Question object from extracted data from images.

    Parameters
    ----------
    image_parts : list[MatLike]
        the list images which contain question or option data or nothing.
    ticked_timplate : MatLike
        template to detect image with unticked element.
    unticked_timplate : MatLike
        template to detect image with unticked element.
    
    Returns
    -------
    Question

    Raises
    ------
    ValueError
        if at least one templates is None
        if result of image processing is None
        if can not extract any options
        if can not extract question text.
    """
    if ticked_template is None or unticked_template is None:
        raise ValueError(ERR_CAN_NOT_LOAD_TEMPLATES)
    
    options: list = []
    question_text: str = ''

    for image in image_parts:
        result = process_image_part(image, ticked_template, unticked_template)
        if result is None:
            raise ValueError(ERR_CAN_NOT_PROCESS_IMAGE)
        elif isinstance(result, str):
            question_text += result
        elif isinstance(result, Option):
            options.append(result)
    if options == []:
        raise ValueError(ERR_NO_OPITONS)
    if question_text == '':
        raise ValueError(ERR_NO_QUESTION)
    return Question(text=question_text, options=options)
