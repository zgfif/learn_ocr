import cv2
from app.full_text_points import FULL_TEXT_POINTS
from app.cropping import Cropping
from app.fetch_lines import fetch_lines
from app.fetch_image_data import fetch_image_data
from app.build_groups import build_groups
from app.increase_areas import increase_areas
from numpy import ndarray
from app.question_extracting import QuestionExtracting
from app.result import Result
from app.question import Question


# list of images to extract questions.
images: tuple = (
    './tests/fixtures/IMG_4731.png', 
    './tests/fixtures/IMG_4732.png',
)

questions: list[Question] = []


# start processing every image.
for image in images:
    image = cv2.imread(image)

    if image is None:
        continue
    
    # remove unnecessary header and footer (header and footer are static for every screenshot).
    cropped_image = Cropping(image=image).perform(
        FULL_TEXT_POINTS.pt1, 
        FULL_TEXT_POINTS.pt2
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

    modified_groups = increase_areas(areas=grouped_lines)

    elements_images: list[ndarray] = []

    for group in modified_groups:
        element_image = Cropping(image=cropped_image).perform(group.pt1, group.pt2)
        if element_image is None:
            continue
        elements_images.append(element_image)
    
    i: int = 0

    for image in elements_images:
        cv2.imwrite(filename=f'part_img_{i}.png', img=image)
        i+=1

    parts_list = []

    for i in range(len(elements_images)):
        parts_list.append(f'part_img_{i}.png')

    question = QuestionExtracting(images=parts_list).perform()

    questions.append(question)

    Result(questions=questions).save('result.csv')
