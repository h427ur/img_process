import numpy as np
import cv2 as cv

data = [
    10, 200, 5, 7, 9,
    15, 35, 60, 80, 170,
    100,2, 55, 37, 70
]

mat = (3, 5) #3행 5열
m1 = np.reshape(data, mat) #리스트를 3행 5열짜리 ndarray로 재구성 및 형변환
m2 = np.full(mat, 50) #3행 5열 ndarray에 값 50을 채움

#min() 함수: m1 요소와 30을 비교하여 30 이상은 전부 30으로 변경; 즉 30 이하는 유지한다
m_min = cv.min(m1, 30)
#max() 함수: 두 배열의 요소를 비교하여 큰 값을 반환한다.
#m2의 모든 요소가 50이므로 50 이하 50으로 변경된다.
m_max = cv.max(m1, m2)

#m1 배열의 최솟값과 최솟값의 위치, 최댓값과 최댓값의 위치를 추출한다.
min_v, max_v, min_loc, max_loc = cv.minMaxLoc(m1)
#행렬 순서는 열 기준; 열행 순서다.

print(f"[m1] =\n{m1}\n")

print(f"[m_min] =\n{m_min}\n")
print(f"[m_max] =\n{m_max}\n")

print(f"m1 행렬 최솟값 좌표:{min_loc}, 최솟값:{min_v}")
print(f"m1 행렬 최댓값 좌표:{max_loc}, 최댓값:{max_v}")