import cv2 as cv

img = cv.imread("images/pixel.jpg", cv.IMREAD_GRAYSCALE)

(x, y), (w, h) = (180, 37), (15, 10)
roi_img = img[y:y+h, x:x+w]

#print(f"[roi_img] =\n{roi_img}")
#인접한 픽셀끼리의 밝기 변화를 나타낸다
print("[roi_img] = ")
for r in roi_img:
    for px in r:
        print(f"{px:4}", end=" ")

print()

cv.rectangle(img, (x, y, w, h), 255, 1)
cv.imshow("img", img)
cv.waitKey(0)