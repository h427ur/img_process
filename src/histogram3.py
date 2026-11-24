import cv2 as cv
import numpy as np
from common.utils import draw_histo_c

img = cv.imread("images/hue_hist.jpg", cv.IMREAD_COLOR)

hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hue_histo = cv.calcHist([hsv_img], [0], None, [18], [0, 180])
hue_histo_img = draw_histo_c(hue_histo, (200, 360, 3))

cv.imshow("img", img)
cv.imshow("hue_hist_img", hue_histo_img)
cv.waitKey(0)