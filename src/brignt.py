import cv2 as cv

img = cv.imread("images/bright.jpg", cv.IMREAD_GRAYSCALE)

#cv와 np가 값이 언더/오버플로우 날 때 처리 방법
#CV는 시작 값(0)과 종료 값(255)에 경계를 지정한다
#이 경계를 넘어가면 자동으로 0 또는 255에 맞춰지게 된다.
res1 = cv.add(img, 100)
res2 = cv.subtract(img, 100)
#numpy는 값에 타입의 길이 값을 나누어 나머지를 구한다; 즉 모듈로 연산이다.
res3 = img + 100
res4 = img - 100

cv.imshow("original", img)
cv.imshow("cv:add", res1)
cv.imshow("cv:sub", res2)
cv.imshow("np:add", res3)
cv.imshow("np:sub", res4)
cv.waitKey(0)