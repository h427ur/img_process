import cv2 as cv
import numpy as np

img = cv.imread("./images/bit_test.jpg", cv.IMREAD_COLOR)
logo = cv.imread("./images/logo.jpg", cv.IMREAD_COLOR)

if img is None or logo is None:
    raise Exceptions("허!접")

masks = cv.threshold(logo, 220, 255, cv.THRESH_BINARY)[1]
#220 이상은 255로,
masks = cv.split(masks)

mask_fg_pass = cv.bitwise_or(masks[0], masks[1]) #blu + grn
mask_fg_pass = cv.bitwise_or(mask_fg_pass, masks[2]) #(blu+grn) + red

mask_bg_pass = cv.bitwise_not(mask_fg_pass) # 반전

(H, W), (h, w) = img.shape[:2], logo.shape[:2]
x, y = (W-w)//2, (H-h)//2
roi = img[y:y+h, x:x+w]

fg = cv.bitwise_and(logo, logo, mask=mask_fg_pass)
bg = cv.bitwise_and(roi, roi, mask=mask_bg_pass)

dst = cv.add(bg, fg)
img[y:y+h, x:x+w] = dst

cv.imshow("BG", bg)
cv.imshow("FG", fg)
cv.imshow("DST", dst)
cv.imshow("IMG", img)
cv.waitKey(0)
