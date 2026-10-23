import numpy as np
import cv2 as cv

def on_mouse(e, x, y, flags, params):
    global img, bar_name

    if e == cv.EVENT_RBUTTONDOWN:
        if img[0][0] < 246 :
            img[:] = img + 10

        cv.setTrackbarPos(bar_name, title, img[0][0])
        cv.imshow(title, img)

    elif e == cv.EVENT_LBUTTONDOWN:
        if img[0][0] >= 10:
            img[:] = img - 10

            cv.setTrackbarPos(bar_name, title, img[0][0])
            cv.imshow(title, img)

def on_change(v):
    global img, title

    add_v = v - int(img[0][0])
    print(f"추가 화소 값: {add_v}")
    img[:] = v

    cv.imshow(title, img)

img = np.full((400, 800), 128, np.uint8)
title = "Trackbar & Mouse Event"
bar_name = "Brightness"

cv.imshow(title, img)

#createTrackbar(트랙바 이름, 트랙바를 생성시킬 창 이름, 트랙바가 가리킬 값, 최대 값, 콜백 함수)
cv.createTrackbar(bar_name, title, img[0][0], 0xff, on_change)
#setMouseCallback(마우스 이벤트를 발생시킬 창 이름, 콜백 함수)
cv.setMouseCallback(title, on_mouse)
cv.waitKey(0)
cv.destroyWindow(title)
