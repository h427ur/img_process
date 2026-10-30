import cv2 as cv

path = "images/color.jpg"
img = cv.imread(path, cv.IMREAD_COLOR)

if img is None or img.ndim != 3:
    raise Exception("허접~")

chan = cv.split(img)

print("channel 자료형:", type(chan), type(chan[0]), type(chan[0][0][0]))
print(f"channel 원소 개수: {len(chan)}")

cv.imshow("img", img)
#이 밑으로 다 흑백으로 띄워짐
cv.imshow("blu", chan[0])
cv.imshow("grn", chan[1])
cv.imshow("red", chan[2])
cv.waitKey(0)