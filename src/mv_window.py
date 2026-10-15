import numpy as np
import cv2

img = np.zeros((200, 400), np.uint8)
img[:] = 0xff

title1, title2 = "Position 1", "Position 2"

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # 창 생성
cv2.moveWindow(title1, 150, 150) # 창 이동

cv2.namedWindow(title2)
cv2.moveWindow(title2, 400, 50)

#imshow 함수 - image show의 약자
cv2.imshow(title1, img)
cv2.imshow(title2, img)

cv2.waitKey(0) # 키가 입력될 때까지 대기
cv2.destroyAllWindows() # 모든 창 제거
