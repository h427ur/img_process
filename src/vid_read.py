import cv2 as cv

from common.utils import put_str

path = "images/test.mp4"
vid = cv.VideoCapture(path)

if not vid.isOpened():
    raise Exception("동영상 파일이 안 열렸는 걸~")

fps = vid.get(cv.CAP_PROP_FPS)
delay = int(1000 / fps)
frame_cnt = 0

while True:
    ret, frame = vid.read()
    if not ret or cv.waitKey(delay) >= 0:
        break

    blu, grn, red = cv.split(frame)
    frame_cnt += 1

    if 100 <= frame_cnt < 200:
        cv.add(blu, 100, blu)
    elif 200 <= frame_cnt < 300:
        cv.add(grn, 100, grn)
    elif 300 <= frame_cnt < 400:
        cv.add(red, 100, red)

    frame = cv.merge([blu, grn, red])
    put_str(frame, "프레임: ", (20, 30), frame_cnt)

    cv.imshow("동영상 읽기", frame)

vid.release()
