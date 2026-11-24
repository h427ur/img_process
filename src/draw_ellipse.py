import cv2 as cv
import numpy as np

# 주황, 파랑, 하늘
rng, blu, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0, 0, 0)

img = np.full((300, 700, 3), white, np.uint8)

p1, p2 = (180, 150), (550, 150)
size = (120, 60)

# 타원의 중심 점 그리기, 쓸모 없는 과정
cv.circle(img, p1, 1, black, 2)
cv.circle(img, p2, 1, black, 2)

# x축은 동쪽부터 시작해, 90도는 남쪽, 180도는 서쪽

# ellipse(타원을 그릴 이미지 객체, 중심 점, x축과 y축의 반지름, 기울기 각도, 시작 각, 종료 각, 색상,.. 굵기, 선 형태, 시프트)
cv.ellipse(img, p1, size, 0, 0, 360, blu, 1)  # 대충 평평하게 가로로 길은 타원
cv.ellipse(img, p1, size, 0, 30, 270, rng, 4)  # 호 각도

cv.ellipse(img, p2, size, 90, 0, 360, blu, 1)  # 대충 세로로 길은 타원
cv.ellipse(img, p2, size, 90, -45, 90, rng, 4)  # 호 각도

window = "Ellipse and Arc"
cv.imshow(window, img)
cv.waitKey(0)
cv.destroyWindow(window)
