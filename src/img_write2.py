import cv2 as cv
import numpy as np

path1 = "images/read_color.jpg"
path2 = "out"
img8 = cv.imread(path1, cv.IMREAD_COLOR)
if img8 is None:
    raise Exception("허~접")

img16 = np.uint16(img8 * (65525 / 255))
img32 = np.float32(img8 * (1 / 255))

print(f"img8 행렬의 일부\n {img8[10:12, 10:13]}\n")
print(f"img16 행렬의 일부\n {img16[10:12, 10:13]}\n")
print(f"img32 행렬의 일부\n {img32[10:12, 10:13]}\n")

cv.imwrite(f"{path2}/write_test_16.tif", img16)
cv.imwrite(f"{path2}/write_test_32.tif", img32)
# print("저장 완료")

cv.imshow("img16", img16)
cv.imshow("img32", (img32 * 32).astype("uint8"))
cv.waitKey(0)
