""" ABRINDO AS IMAGENS PROCESSADAS """

import cv2 as cv
import os
from processing import process_image

forms = 'data/form'
letters = 'data/letter'
reports = 'data/scientific_report'
blank = 'data/blank'

images = []
for dir in [blank, letters, reports, forms]:
    for file in os.listdir(dir):
        if file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')):
            images.append(os.path.join(dir, file))

for path in images:
    img, canny_edges, img_class, contours = process_image(path)
     
    cv.imshow('Documento', img)
    print(f"{path} -> {img_class} ({contours} contornos)")

    key = cv.waitKey(0)

    if key == 27:
        break;

cv.destroyAllWindows()