import cv2

from app.full_text_points import FULL_TEXT_POINTS
from app.crop_image import crop_image
from app.fetch_lines import fetch_lines
from app.fetch_image_data import fetch_image_data
from app.build_groups import build_groups
from app.adjust_areas_for_detection import adjust_areas_for_detection
from numpy import ndarray
from app.extract_question import extract_question
from app.result import Result
from app.question import Question
from app.load_image import load_image


# list of images to extract questions.
screenshots: tuple = (
    load_image('./tests/fixtures/IMG_4731.png'), 
    load_image('./tests/fixtures/IMG_4732.png'),
)

ticked_template = load_image('./img/ticked.png')
unticked_template = load_image('./img/unticked.png')


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

    elements_images: list[ndarray] = []

    for area in areas:
        element_image = crop_image(
            image=cropped_image, 
            pt1=area.pt1, 
            pt2=area.pt2
        )
        if element_image is None:
            continue
        elements_images.append(element_image)
    
    # i: int = 0

    # for image in elements_images:
    #     cv2.imwrite(filename=f'part_img_{i}.png', img=image)
    #     i+=1

    # parts_list = []

    # for i in range(len(elements_images)):
    #     parts_list.append(f'part_img_{i}.png')
    

    question = extract_question(
        images=elements_images, 
        ticked_template=ticked_template, 
        unticked_template=unticked_template,
    )
    if question:
        questions.append(question)

    Result(questions=questions).save('result.csv')
