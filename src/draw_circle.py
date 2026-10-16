import numpy as np
import cv2 as cv

rng, blu, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0,0,0)

img = np.full((300, 500, 3), white, np.uint8)

cent = (img.shape[1]//2, img.shape[0]//2)
p1, p2 = (300, 50), (100, 220)
shade = (p2[0] + 2, p2[1] + 2)

cv.circle(img, cent, 100, blu)
cv.circle(img, p1, 50, rng, 2)
cv.circle(img, p2, 70, cyan, -1)

font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img, "cent_blu", cent, font, 1., blu)
cv.putText(img, "p1_rng", p1, font, .8, rng)
cv.putText(img, "p2_cyan", p2, font, 1.2, black, 2)
cv.putText(img, "p2_cyan", p2, font, 1.2, cyan, 1)

cv.imshow("Draw circles", img)
cv.waitKey(0)
cv.destroyWindow("Draw circles")