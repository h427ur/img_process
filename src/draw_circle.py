import cv2 as cv
import numpy as np

rng, blu, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0, 0, 0)

img = np.full((300, 500, 3), white, np.uint8)

# 중심, 이미지 객체의 행렬의 값을 반으로 나눠 나온 정수 값이 중심 점이다.
cent = (img.shape[1] // 2, img.shape[0] // 2)
p1, p2 = (300, 50), (100, 220)
shade = (p2[0] + 1, p2[1] + 1)  # 그림자, p2 좌표에서 1칸 멀리 한다.

# circle(원을 그릴 이미지 객체, 원이 위치 할 중심 점, 반지름, 색상,.. 굵기, 선 형태, 시프트))
cv.circle(img, cent, 100, blu)
cv.circle(img, p1, 50, rng, 2)
cv.circle(img, p2, 70, cyan, -1)  # 굵기에 -1을 주면 내부가 색상으로 채워진다.

font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img, "cent_blu", cent, font, 1.0, blu)
cv.putText(img, "p1_rng", p1, font, 0.8, rng)
cv.putText(img, "p2_cyan", shade, font, 1.2, black, 2)
cv.putText(img, "p2_cyan", p2, font, 1.2, cyan, 1)

cv.imshow("Draw circles", img)
cv.waitKey(0)
cv.destroyWindow("Draw circles")
