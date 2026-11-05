import cv2 as cv
import numpy as np


def on_mouse(e, x, y, flags, param):
    global title
    pt = (x, y)
    if e == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, pt, 5, 100, 1)
    elif e == cv.EVENT_RBUTTONDOWN:
        pt2 = (pt[0] + 30, pt[1] + 30)
        cv.rectangle(img, pt, pt2, 100, 2)
        cv.imshow(title, img)


img = np.ones((300, 300), np.uint8) * 0xFF

title = "Draw Event"

cv.namedWindow(title)
cv.imshow(title, img)
cv.setMouseCallback(title, on_mouse)
cv.waitKey(0)
cv.destroyAllWindows()
