import numpy as np
import cv2 as cv

img = cv.imread("images/contrast.jpg", cv.IMREAD_GRAYSCALE)

dummy = np.zeros(img.shape[:2], img.dtype)
avg = cv.mean(img)[0]/2.0

#대비에 관한 것
#명암 대비를 줄이면 영상이 부드럽게 느껴지고,
#높이면 뚜렷하게 느껴진다.
dst1 = cv.scaleAdd(img, .5, dummy)
dst2 = cv.scaleAdd(img, 2, dummy)
dst3 = cv.addWeighted(img, .5, dummy, 0, avg)
dst4 = cv.addWeighted(img, 2, dummy, 0, -avg)

cv.imshow("original", img)
cv.imshow("decrease contrast", dst1)
cv.imshow("increase contrast2", dst2)
cv.imshow("decrease contrast3 using average", dst3)
cv.imshow("increase contrast4 using average", dst4)
cv.waitKey(0)