import numpy as np
import cv2 as cv

oliv, viol, brwn = (128, 128, 0), (221, 160, 221), (42, 42, 165)
p1, p2 = (50, 230), (50, 310)

img = np.full((350, 700, 3), 255, np.uint8)

cv.putText(img, "SiMPLEx hawawa", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, brwn)
cv.putText(img, "duPLEx hawawa", (50, 130), cv.FONT_HERSHEY_DUPLEX, 3, oliv)
cv.putText(img, "TriPlex hawawa", p1, cv.FONT_HERSHEY_TRIPLEX, 2, viol)

fontface = cv.FONT_HERSHEY_PLAIN | cv.FONT_ITALIC
cv.putText(img, "iTALiC hawawa", p2, fontface, 4, viol)

cv.imshow("Text", img)
cv.waitKey(0)
cv.destroyWindow("Text")