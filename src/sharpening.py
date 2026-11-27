import cv2 as cv
import numpy as np

from common.utils import fltr_mat

img = cv.imread("./images/filter_sharpen.jpg", cv.IMREAD_GRAYSCALE)

mask1 = [0, -1, 0, -1, 5, -1, 0, -1, 0]
mask2 = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]

m1 = np.array(mask1, np.float32).reshape(3, 3)
m2 = np.array(mask2, np.float32)

sharpen1 = fltr_mat(img, m1)
sharpen1 = cv.convertScaleAbs(sharpen1)

sharpen2 = fltr_mat(img, m2)
sharpen2 = cv.convertScaleAbs(sharpen2)

cv.imshow("img", img)
cv.imshow("sharpen1", sharpen1)
cv.imshow("sharpen2", sharpen2)
cv.waitKey(0)
