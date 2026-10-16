import numpy as np
import cv2 as cv

red, grn, blu, blk = (0xff, 0, 0), (0, 0xff, 0), (0, 0, 0xff), (0, 0, 0)

img = np.full((400, 500, 3), (255, 255, 255), np.uint8)

p1, p2 = (50, 50), (250, 150)
p3, p4 = (400, 150), (500, 50)
roi = (50, 200, 150, 100)

cv.line(img, p1, p2, red)
cv.line(img, p3, p4, grn, 3, cv.LINE_AA)

cv.rectangle(img, p1, p2, blu, 3, 4)
cv.rectangle(img, roi, red, 3, 8)
cv.rectangle(img, (400, 200, 50, 100), grn, cv.FILLED)

cv.imshow("Line and Rect", img)
cv.waitKey(0)
cv.destroyWindow("Line and Rect")