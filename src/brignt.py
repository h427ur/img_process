import cv2 as cv

img = cv.imread("images/bright.jpg", cv.IMREAD_GRAYSCALE)

res1 = cv.add(img, 100)
res2 = cv.subtract(img, 100)
res3 = img + 100
res4 = img - 100

cv.imshow("original", img)
cv.imshow("cv:add", res1)
cv.imshow("cv:sub", res2)
cv.imshow("np:add", res3)
cv.imshow("np:sub", res4)
cv.waitKey(0)