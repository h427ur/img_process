import cv2 as cv
import numpy as np

oliv, viol, brwn = (128, 128, 0), (221, 160, 221), (42, 42, 165)
p1, p2 = (50, 230), (50, 310)

img = np.full((350, 700, 3), 255, np.uint8)

# putText(텍스트를 그릴 이미지 객체, 텍스트, 시작 점, 폰트, 확대율, 색상,.. 굵기, 선 형태, 하단 좌측 여부)
# 시작 점으로부터 하단 우측에 텍스트가 그려진다.
cv.putText(img, "SiMPLEx hawawa", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, brwn)
cv.putText(img, "duPLEx hawawa", (50, 130), cv.FONT_HERSHEY_DUPLEX, 3, oliv)
cv.putText(img, "TriPlex hawawa", p1, cv.FONT_HERSHEY_TRIPLEX, 2, viol)

fontface = cv.FONT_HERSHEY_PLAIN | cv.FONT_ITALIC
cv.putText(img, "iTALiC hawawa", p2, fontface, 4, viol)

cv.imshow("Text", img)
cv.waitKey(0)
cv.destroyWindow("Text")
