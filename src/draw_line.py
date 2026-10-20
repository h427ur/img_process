import cv2 as cv
import numpy as np

red, grn, blu, blk = (0, 0, 0xFF), (0, 0xFF, 0), (0xFF, 0, 0), (0, 0, 0)
# 영상 처리에서 빛의 3원소 순서는 청녹적(bgr)이다.

img = np.full((400, 500, 3), (255, 255, 255), np.uint8)

# 튜플 형으로 2차원 좌표 변수 선언
# x, y 순 즉 열 -> 행 순서다.
p1, p2 = (50, 50), (250, 150)
p3, p4 = (400, 150), (500, 50)
roi = (50, 200, 150, 100)

# line(img, x, y, color, thickness, linetype)
# 순서대로 선을 그릴 이미지 객체, 열, 행, 색상, 굵은 정도, 선 형태
# 우측 하단으로 그어지는 빨간 선
cv.line(img, p1, p2, red)

# 우측 상단으로 그어지는 초록 선, 마지막 인자는 안티엘리어싱(AA)이다.
cv.line(img, p3, p4, grn, 3, cv.LINE_AA)

# line 함수와 똑같다, 좌표 점 두 개만 줘도 사각형이 그려진다.
cv.rectangle(img, p1, p2, blu, 3, 4)

# roi는 두 좌표를 하나의 튜플형으로 담은 것, 이렇게 줘도 사각형은 그려진다.
# (x, y, w, h) - 열 -> 행 -> 너비 -> 길이 이므로 두 좌표 점을 준 것
cv.rectangle(img, roi, red, 3, 8)
cv.rectangle(img, (400, 200, 50, 100), grn, cv.FILLED)

cv.imshow("Line and Rect", img)
cv.waitKey(0)
cv.destroyWindow("Line and Rect")
