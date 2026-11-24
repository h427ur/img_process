import numpy as np
import cv2 as cv

def on_change(v):
    global img, title

    add_v = v - int(img[0][0])
    print(f"추가 화소 값: {add_v}")
    img[:] = v

    cv.imshow(title, img)

img = np.zeros((800, 400), np.uint8)
title = "Trackbar Event"

cv.imshow(title, img)

cv.createTrackbar("Brightness", title, img[0][0], 0xff, on_change)
cv.waitKey(0)
cv.destroyAllWindows()
