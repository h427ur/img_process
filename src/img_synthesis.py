import numpy as np
import cv2 as cv

img1 = cv.imread("./images/add1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("./images/add2.jpg", cv.IMREAD_GRAYSCALE)

alpha = .6
beta = .7

add1 = cv.add(img1, img2) # 단순 덧셈
add2 = cv.add(img1 * alpha, img2 * beta) # 비율에 따른 덧셈
add2 = np.clip(add2, 0, 255).astype("uint8") # 보정
add3 = cv.addWeighted(img1, alpha, img2, beta, 0) # 비율에 따른 덧셈 2

titles = ["img1", "img2", "add1", "add2", "add3"]

for t in titles:
    cv.imshow(t, eval(t))

cv.waitKey(0)