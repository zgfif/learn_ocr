import cv2
from app.full_text_points import FULL_TEXT_POINTS
from app.cropping import Cropping
from app.lines import Lines
from app.image_data import ImageData
from app.build_groups import Groups
from app.preparing_coordinates import PreparingCoordinates
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
    image_data = ImageData(image=cropped_image).extract()

    # print(image_data)

    # return the list of coordinates of lines.
    lines_coordinates = Lines(data=image_data).coordinates()
    

    # return the list of grouped lines. each element has two coordinates pt1 and pt2.
    grouped_lines = Groups.build(lines=lines_coordinates)

    modified_groups = PreparingCoordinates(lines=grouped_lines).perform()

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
