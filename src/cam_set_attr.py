import cv2 as cv

from common.utils import put_str


def zoom_bar(value):
    global cam
    cam.set(cv.CAP_PROP_ZOOM, value)


def focus_bar(value):
    global cam
    cam.set(cv.CAP_PROP_FOCUS, value)


cam = cv.VideoCapture(0)
if not cam.isOpened():
    raise Exception("카메라 연결 안됨, 허~접")

width, height, exposure, bright = (
    cam.get(cv.CAP_PROP_FRAME_WIDTH),
    cam.get(cv.CAP_PROP_FRAME_HEIGHT),
    cam.get(cv.CAP_PROP_EXPOSURE),
    cam.get(cv.CAP_PROP_BRIGHTNESS),
)

cam.set(cv.CAP_PROP_FRAME_WIDTH, 400)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 300)
cam.set(cv.CAP_PROP_AUTOFOCUS, 0)
cam.set(cv.CAP_PROP_BRIGHTNESS, 100)

title = "카메라 속성 변경"
cv.namedWindow(title)
cv.createTrackbar("zoom", title, 0, 10, zoom_bar)
cv.createTrackbar("focus", title, 0, 40, focus_bar)

while 1:
    ret, frame = cam.read()

    if not ret:
        break
    if cv.waitKey(30) >= 0:
        break

    zoom = int(cam.get(cv.CAP_PROP_ZOOM))
    focus = int(cam.get(cv.CAP_PROP_FOCUS))
    put_str(frame, "확대율: ", (10, 240), zoom)
    put_str(frame, "포커스: ", (10, 270), focus)

    cv.imshow(title, frame)

cam.release()
