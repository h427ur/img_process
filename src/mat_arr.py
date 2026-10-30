import cv2 as cv

path = "images/flip_test.jpg"
img = cv.imread(path, cv.IMREAD_COLOR)
if img is None:
    raise Exception("허~접")

axis_x = cv.flip(img, 0)
axis_y = cv.flip(img, 1)
axises = cv.flip(img, -1)
repeat = cv.repeat(img, 1, 2) #1*2; 1행 2열 반복
t_pose = cv.transpose(img)

titles = [
    "img",
    "axis_x",
    "axis_y",
    "axises",
    "repeat",
    "t_pose",
]

for i in titles:
    cv.imshow(i, eval(i))

cv.waitKey(0)
