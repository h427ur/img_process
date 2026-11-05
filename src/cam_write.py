import cv2 as cv

cam = cv.VideoCapture(0)

if not cam.isOpened():
    raise Exception("카메라도 연결 못하는 허~접")

fps = 29.97
delay = round(1000 / fps)
size = (640, 360)
codec = cv.VideoWriter_fourcc(*"DX50")

print(f"너비 * 길이: {size}")
print(f"압축 코덱: {codec}")
print(f"지연 시간: {delay:2d}ms")
print(f"초 당 프레임 수: {fps:.2f}%")

cam.set(cv.CAP_PROP_ZOOM, 1)
cam.set(cv.CAP_PROP_FOCUS, 0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, size[0])
cam.set(cv.CAP_PROP_FRAME_HEIGHT, size[1])

path = "images/video_file.avi"
out = "out/"

writer = cv.VideoWriter(path, codec, fps, size)

if not writer.isOpened():
    raise Exception("동영상 파일이 안 열렸다구~")


while True:
    ret, frame = cam.read()
    if not ret:
        break
    if cv.waitKey(delay) >= 0:
        break

    writer.write(frame)
    cv.imshow("카메라로 프레임 저장", frame)

writer.release()
cam.release()
