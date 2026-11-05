import cv2 as cv

from common.utils import get_matInfo

title1, title2 = "gray", "gray2color"
path = "images/read_gray.jpg"
gray = cv.imread(path, cv.IMREAD_GRAYSCALE)
gray2color = cv.imread(path, cv.IMREAD_COLOR)

if gray is None or gray2color is None:
    raise Exception("영상 파일 읽기 오류")

print("행렬 좌표 (100, 100) 화소 값")
print(f"{title1} {gray[100, 100]}")
print(f"{title1} {gray2color[100, 100]}")

get_matInfo(title1, gray)
get_matInfo(title2, gray2color)

cv.imshow(title1, gray)
cv.imshow(title2, gray2color)
cv.waitKey(0)
