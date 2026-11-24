import cv2 as cv
import numpy as np

cases = {
    ord("a"): "a키",
    ord("w"): "w키",
    0x64: "d키",
    int("115", 10): "s키",
    2424832: "좌",
    2409368: "상",
    2555904: "우",
    2621440: "하",
}

img = np.ones((200, 300), np.float32)
cv.namedWindow("Keyboard Event")
cv.imshow("Keyboard Event", img)

while True:
    key = cv.waitKeyEx(100)
    if key == 27:
        break

    try:
        result = cases[key]
        print(result)
    except KeyError:
        result = -1

cv.destroyAllWindows()
