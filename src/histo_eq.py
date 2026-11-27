import cv2 as cv
import numpy as np

from common.utils import draw_histo

img = cv.imread("./images/equalize.jpg", cv.IMREAD_GRAYSCALE)

bins, ranges = [256], [0, 256]
histo = cv.calcHist([img], [0], None, bins, ranges)

accum_histo = np.zeros(histo.shape[:2], np.float32)
accum_histo[0] = histo[0]

for i in range(1, histo.shape[0]):
    accum_histo[i] = accum_histo[i - 1] + histo[i]

accum_histo = (accum_histo / sum(histo)) * 255
dst1 = [[accum_histo[val] for val in row] for row in img]
dst1 = np.array(dst1, np.uint8)

dst2 = cv.equalizeHist(img)
histo2 = cv.calcHist([dst1], [0], None, bins, ranges)
histo3 = cv.calcHist([dst2], [0], None, bins, ranges)

histo_img = draw_histo(histo)
histo_img2 = draw_histo(histo2)
histo_img3 = draw_histo(histo3)

cv.imshow("img", img)
cv.imshow("user_dst1", dst1)
cv.imshow("cv_dst1", dst2)

cv.imshow("histo_img", histo_img)
cv.imshow("user_histo", histo_img2)
cv.imshow("cv_histo", histo_img3)
cv.waitKey(0)
