import cv2 as cv

from common.utils import get_matInfo

title1, title2 = "16bit", "32bit"
path1 = "images/read_16.tif"
path2 = "images/read_32.tif"
color1 = cv.imread(path1, cv.IMREAD_UNCHANGED)
color2 = cv.imread(path2, cv.IMREAD_UNCHANGED)

if color1 is None or color2 is None:
    raise Exception("영상 파일 읽기 오류")

print("16/32비트 영상 행렬 좌표 (10, 10) 화소 값")

print(f"{title1} 원소 자료형 {type(color1[10, 10, 0])}")
print(f"{title1} 화소 값(3원소) {color1[10, 10]}")

print(f"{title2} 원소 자료형 {type(color2[10, 10, 0])}")
print(f"{title2} 화소 값(3원소) {color2[10, 10]}")
print()

get_matInfo(title1, color1)
get_matInfo(title2, color2)

cv.imshow(title1, color1)
cv.imshow(title2, color2)
cv.waitKey(0)
