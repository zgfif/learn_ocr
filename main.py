import cv2
from app.view_image import ViewImage
from app.full_text_points import FULL_TEXT_POINTS
from app.cropping import Cropping
from app.lines import Lines
from app.image_data import ImageData
from app.rectangle import Rectangle
from app.groups import Groups
from app.preparing_coordinates import PreparingCoordinates



images = ('./IMG_4731.png', './IMG_4732.png',)

# cropped_images = []

for image in images:
    image = cv2.imread(image)

    if image is None:
        continue
    
    cropped_image = Cropping(image=image).perform(
        FULL_TEXT_POINTS.pt1, 
        FULL_TEXT_POINTS.pt2
    )
    
    if cropped_image is None:
        continue

    image_data = ImageData(image=cropped_image).extract()

    # print(image_data)

    lines_coordinates = Lines(data=image_data).coordinates()

    # print(lines_coordinates)
    print( '___*' * 10)

    # for coordinates in lines_coordinates:
    #     Rectangle(image=cropped_image).draw(pt1=coordinates.pt1, pt2=coordinates.pt2)    
    


    grouped_lines = Groups(lines=lines_coordinates).build()

    modified_groups = PreparingCoordinates(lines=grouped_lines).perform()

    for line in modified_groups:
        Rectangle(image=cropped_image).draw(pt1=line.pt1, pt2=line.pt2)    
    


    ViewImage(image=cropped_image).perform()
