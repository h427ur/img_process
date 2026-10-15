import numpy as np
import cv2 as cv

def on_mouse(e, x, y, flags, params):
    if e == cv.EVENT_LBUTTONDOWN:
        print("마우스 좌버튼")
    elif e == cv.EVENT_RBUTTONDOWN:
        print("마우스 우버튼")
    elif e == cv.EVENT_LBUTTONUP:
        print("마우스 좌버튼 떼짐")
    elif e == cv.EVENT_LBUTTONDBLCLK:
        print("마우스 좌버튼 더블 클릭")

img = np.full((200, 300), 0xff/2, np.uint8)

title1, title2 = "Mouse Event 1", "Mouse Event 2"

cv.imshow(title1, img)
#cv.imshow(title2, img)

cv.setMouseCallback(title1, on_mouse)
cv.waitKey(0)
cv.destroyAllWindows()
