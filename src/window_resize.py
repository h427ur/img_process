import numpy as np
import cv2 as cv

img = np.zeros((200, 300), np.uint8)
img.fill(0x00) #16진수로 0, 검은 새끼다.

title1, title2 = "Auto", "Normal"
cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)
cv.namedWindow(title2, cv.WINDOW_NORMAL)

cv.imshow(title1, img)
cv.imshow(title2, img)

cv.resizeWindow(title1, 400, 300)
cv.resizeWindow(title2, 400, 300)

#0보다 작거나 같으면 무한 대기
# 0보다 크면 그 값만큼 대기
cv.waitKey(0) #밀리초 단위다
cv.destroyAllWindows()
