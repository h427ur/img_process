import numpy as np
import cv2 as cv

rng, blu, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0,0,0)

img = np.full((300, 700, 3), white, np.uint8)

p1, p2 = (180, 150), (550, 150)
size = (120, 60)

cv.circle(img, p1, 1, black, 2)
cv.circle(img, p2, 1, black, 2)

cv.ellipse(img, p1, size, 0, 0, 360, blu, 1)
cv.ellipse(img, p1, size, 0, 30, 270, rng, 4)

cv.ellipse(img, p2, size, 90, 0, 360, blu, 1)
cv.ellipse(img, p2, size, 90, -45, 90, rng, 4)

name = "Ellipse and Arc"
cv.imshow(name, img)
cv.waitKey(0)
cv.destroyWindow(name)