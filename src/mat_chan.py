import numpy as np
import cv2 as cv

mat = (2, 4)

blu = np.zeros(mat, np.uint8) + 10
grn = np.ones(mat, np.uint8) * 20
red = np.full(mat, 30, np.uint8)

chan = [blu, grn, red]
chan_m = cv.merge(chan)
chan_s = cv.split(chan_m)

print(f"chan_s: {np.array(chan_s).shape}")
print(f"chan_m: {np.array(chan_m).shape}")

print(f"[blu]: \n{blu}")

print(f"[grn]: \n{grn}")
print(f"[red]: \n{red}\n")

print(f"[chan_m]: \n {chan_m}\n")

print(f"[chan_s[0]]: \n {chan_s[0]}")
print(f"[chan_s[1]]: \n {chan_s[1]}")
print(f"[chan_s[2]]: \n {chan_s[2]}")