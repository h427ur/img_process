import cv2 as cv
import numpy as np

img1 = np.zeros((300, 300), np.uint8)
img2 = img1.copy()

h, w = img1.shape[:2]
cent_x, cent_y = w//2, h//2

cv.circle(img1, (cent_x, cent_y), 100, 255, -1)
cv.rectangle(img2, (0, 0, cent_x, h), 255, -1)

img3 = cv.bitwise_or(img1, img2) #합연산
img4 = cv.bitwise_and(img1, img2) #교집합
img5 = cv.bitwise_xor(img1, img2)
img6 = cv.bitwise_not(img1, img2) #반전

cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("img3", img3)
cv.imshow("img4", img4)
cv.imshow("img5", img5)
cv.imshow("img6", img6)

cv.waitKey(0)
