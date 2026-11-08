import numpy as np
import cv2 as cv

data = [
    10, 200, 5, 7, 9,
    15, 35, 60, 80, 170,
    100,2, 55, 37, 70
]

mat = (3, 5)
m1 = np.reshape(data, mat)
m2 = np.full(mat, 50)

m_min = cv.min(m1, 30)
m_max = cv.max(m1, m2)

min_v, max_v, min_loc, max_loc = cv.minMaxLoc(m1)

print(f"[m1] =\n{m1}\n")

print(f"[m_min] =\n{m_min}\n")
print(f"[m_max] =\n{m_max}\n")

print(f"m1 행렬 최솟값 좌표:{min_loc}, 최솟값:{min_v}")
print(f"m1 행렬 최댓값 좌표:{max_loc}, 최댓값:{max_v}")