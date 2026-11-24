import cv2 as cv

from common.utils import get_matInfo

title1, title2 = "color2gray", "color"
path = "images/read_color.jpg"
color2gray = cv.imread(path, cv.IMREAD_GRAYSCALE)
color = cv.imread(path, cv.IMREAD_COLOR)

if color2gray is None or color is None:
    raise Exception("영상 파일 읽기 오류")

print("행렬 좌표 (100, 100) 화소 값")
print(f"{title1} {color2gray[100, 100]}")
print(f"{title1} {color[100, 100]}")

get_matInfo(title1, color2gray)
get_matInfo(title2, color)

cv.imshow(title1, color2gray)
cv.imshow(title2, color)
cv.waitKey(0)
