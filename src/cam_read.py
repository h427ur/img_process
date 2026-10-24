import cv2 as cv

from common.utils import put_str

cam = cv.VideoCapture(0)
if not cam.isOpened():
    raise Exception("카메라 연결 안됨, 허~접")

width, height, exposure, bright = (
    cam.get(cv.CAP_PROP_FRAME_WIDTH),
    cam.get(cv.CAP_PROP_FRAME_HEIGHT),
    cam.get(cv.CAP_PROP_EXPOSURE),
    cam.get(cv.CAP_PROP_BRIGHTNESS),
)

print(f"너비: {width}")
print(f"높이: {height}")
print(f"노출: {exposure}")
print(f"밝기: {bright}")

while 1:
    ret, frame = cam.read()

    if not ret:
        break
    if cv.waitKey(30) >= 0:
        break

    exposure = cam.get(cv.CAP_PROP_EXPOSURE)
    put_str(frame, "노출: ", (10, 40), exposure)

    title = "카메라의 프레임 보기"
    cv.imshow(title, frame)

cam.release()
