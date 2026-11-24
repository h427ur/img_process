import cv2 as cv
import numpy as np

img = cv.imread("images/bit_test.jpg", cv.IMREAD_COLOR)
logo = cv.imread("images/logo.jpg", cv.IMREAD_COLOR)

if img is None or logo is None:
    raise Exception("허!접")

masks = cv.threshold(logo, 220, 255, cv.THRESH_BINARY)[1]
# 220 이상은 255로,
masks = cv.split(masks)

mask_fg_pass = cv.bitwise_or(masks[0], masks[1])  # blu + grn
mask_fg_pass = cv.bitwise_or(mask_fg_pass, masks[2])  # (blu+grn) + red

mask_bg_pass = cv.bitwise_not(mask_fg_pass)  # 반전

#이미지의 사이즈와 로고의 사이즈를 구함
(H, W), (h, w) = img.shape[:2], logo.shape[:2]
x, y = (W - w) // 2, (H - h) // 2 #이미지에서 로고 사이즈를 빼고 2로 나눈 값 = 시작 좌표
#이미지 정중앙에 로고를 그리려면, 좌우상하의 여백을 계산해야한다.
#이미지의 너비에서 로고의 너비를 빼고, 우측 여백을 좌측 여백에 맞추기 위해 2로 나눔.
#똑같은 논리로 이미지의 높이에 로고의 높이를 빼고 상단 여백을 하단 여백에 맞추기 위해 2로 나눈다.
roi = img[y : y + h, x : x + w]
#시작좌표로부터 로고의 사이즈를 계산
#roi - Region of Interset; 관심 영역

fg = cv.bitwise_and(logo, logo, mask=mask_fg_pass)
bg = cv.bitwise_and(roi, roi, mask=mask_bg_pass)

dst = cv.add(bg, fg)
img[y : y + h, x : x + w] = dst

cv.imshow("BG", bg)
cv.imshow("FG", fg)
cv.imshow("DST", dst)
cv.imshow("IMG", img)
cv.waitKey(0)
