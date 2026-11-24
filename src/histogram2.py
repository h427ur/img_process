import numpy as np
import cv2 as cv
from common.utils import draw_histo

img = cv.imread("images/pixel.jpg", cv.IMREAD_GRAYSCALE)

size = [32]
ranges = [0, 256]
hist = cv.calcHist([img], [0], None, size, ranges)
hist_img = draw_histo(hist)

cv.imshow("img", img)
cv.imshow("hist_img", hist_img)
cv.waitKey(0)