import cv2 as cv

path1 = "images/read_color.jpg"
path2 = "out"

img = cv.imread(path1, cv.IMREAD_COLOR)
if img is None:
    raise Exception("허~접")

opt_jpg = (cv.IMWRITE_JPEG_QUALITY, 10)
opt_png = [cv.IMWRITE_PNG_COMPRESSION, 9]

cv.imwrite(f"{path2}/write_test.jpg", img)
cv.imwrite(f"{path2}/write_test.jpg", img, opt_jpg)
cv.imwrite(f"{path2}/write_test.png", img, opt_png)
cv.imwrite(f"{path2}/write_test.bmp", img)
cv.imwrite(f"{path2}/write_test.webp", img)
print("저장 완료")
