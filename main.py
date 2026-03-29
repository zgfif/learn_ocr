from numpy import ndarray

from app.adjust_areas_for_detection import adjust_areas_for_detection
from app.build_groups import build_groups
from app.build_question import build_question
from app.crop_image import crop_image
from app.fetch_image_data import fetch_image_data
from app.fetch_lines import fetch_lines
from app.full_text_points import FULL_TEXT_POINTS
from app.load_image import load_image
from app.result import Result
from app.question import Question



# list of images to extract questions.
screenshots: tuple = (
    load_image('./tests/fixtures/IMG_4731.png'), 
    load_image('./tests/fixtures/IMG_4732.png'),
)

ticked_template = load_image('./img/ticked.png')
unticked_template = load_image('./img/unticked.png')

if ticked_template is None or unticked_template is None:
    raise RuntimeError('can not load templates.')

questions: list[Question] = []


# start processing every image.
for screenshot in screenshots:
    if screenshot is None:
        continue
    
    # remove unnecessary header and footer (header and footer are static for every screenshot).
    cropped_image = crop_image(
        image=screenshot,
        pt1=FULL_TEXT_POINTS.pt1, 
        pt2=FULL_TEXT_POINTS.pt2
    )
    
    if cropped_image is None:
        continue

    # convert image to dict of data.
    image_data = fetch_image_data(image=cropped_image)

    if image_data is None:
        continue
    # return the list of coordinates of lines.
    lines_coordinates = fetch_lines(data=image_data)
    

    # return the list of grouped lines. each element has two coordinates pt1 and pt2.
    grouped_lines = build_groups(lines=lines_coordinates)

    areas = adjust_areas_for_detection(areas=grouped_lines)

    image_parts: list[ndarray] = []

    for area in areas:
        image_part = crop_image(
            image=cropped_image, 
            pt1=area.pt1, 
            pt2=area.pt2
        )
        if image_part is None:
            continue
        image_parts.append(image_part)

    question = build_question(
        image_parts=image_parts, 
        ticked_template=ticked_template, 
        unticked_template=unticked_template
    )
    
    questions.append(question)

    Result(questions=questions).save('result.csv')
