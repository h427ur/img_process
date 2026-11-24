import cv2 as cv
import numpy as np
from common.utils import draw_histo

def get_val_idx(hist, b=0):
    for i in range(hist.shape[0]):
        idx = np.abs(b - i)
        if hist[idx] > 0: return idx

    return -1

img = cv.imread("images/hist_stretch.jpg", cv.IMREAD_GRAYSCALE)

bsize = [64]
ranges = [0, 256]
hist = cv.calcHist([img], [0], None, bsize, ranges)

bin_width = ranges[1] / bsize[0]
low = get_val_idx(hist, 0) * bin_width
high = get_val_idx(hist, bsize[0] - 1) * bin_width

idx = np.arange(0, 256)
idx = (idx - low) / (high - low) * 255
idx[0:int(low)] = 0
idx[int(high+1):] = 255

dst = cv.LUT(img, idx.astype("uint8"))

hist_dst = cv.calcHist([dst], [0], None, bsize, ranges)
hist_img = draw_histo(hist, (200, 360))
hist_dst_img = draw_histo(hist_dst, (200, 360))

print(f"high value = {high}")
print(f"low value = {low}")
cv.imshow("img", img)
cv.imshow("dst", dst)
cv.imshow("hist_img", hist_img)
cv.imshow("hist_dst_img", hist_dst_img)

cv.waitKey(0)