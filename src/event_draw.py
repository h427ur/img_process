import cv2 as cv
import numpy as np


def on_mouse(e, x, y, flags, params):
    global title, point

    if e == cv.EVENT_LBUTTONDOWN:
        if point[0] < 0:
            point = (x, y)
        else:
            cv.rectangle(img, point, (x, y), (255, 0, 0), 2)
            cv.imshow(title, img)
            point = (-1, -1)

    elif e == cv.EVENT_RBUTTONDOWN:
        if point[0] < 0:
            point = (x, y)
        else:
            dis_x, dis_y = point[0] - x, point[1] - y
            rad = int(np.sqrt(dis_x * dis_x + dis_y * dis_y))
            cv.circle(img, point, rad, (0, 0, 255), 2)
            cv.imshow(title, img)
            point = (-1, -1)


img = np.full((300, 500, 3), (255, 255, 255), np.uint8)
point = (-1, -1)
title = "Draw Event"

cv.imshow(title, img)
cv.setMouseCallback(title, on_mouse)
cv.waitKey(0)
