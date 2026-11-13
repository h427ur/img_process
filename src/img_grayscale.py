import numpy as np
import cv2 as cv

mat = (50, 512)
img1 = np.zeros(mat, np.uint8)
img2 = img1.copy()

row, col = img1.shape[:2]

for r in range(row):
    for c in range(col):
        #img1.itemset((r, c), c // 2)
        #img2.itemset((r, c), (c // 20) * 10)
        #itemset 함수 없어짐
        img1[r, c] = c // 2
        img2[r, c] = (c // 20) * 10

cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.waitKey(0)