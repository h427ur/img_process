import cv2 as cv
import numpy as np

from common.utils import fltr_mat, fltr_px

img = cv.imread("./images/filter_blur.jpg", cv.IMREAD_GRAYSCALE)

m = np.full((3, 3), 1 / 9, np.float32)
blur1 = fltr_mat(img, m)
blur1 = blur1.astype("uint8")

blur2 = fltr_px(img, m)
blur2 = cv.convertScaleAbs(blur2)

cv.imshow("img", img)
cv.imshow("blur1", blur1)
cv.imshow("blur2", blur2)
cv.waitKey(0)
