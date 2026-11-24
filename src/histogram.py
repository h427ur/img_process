import cv2 as cv
import numpy as np

from common.utils import calc_histo

img = cv.imread("images/pixel.jpg", cv.IMREAD_GRAYSCALE)

size = [32]
ranges = [0, 256]
gap = ranges[1] / size[0]
range_gap = np.arange(0, ranges[1] + 1, gap)
hist1 = calc_histo(img, size[0], ranges)
hist2 = cv.calcHist([img], [0], None, size, ranges)
hist3, _ = np.histogram(img, range_gap) #밑줄은 버린다는 의미

print(f"User func:\n{hist1.flatten()}")
print(f"CV func:\n{hist2.flatten()}")
print(f"Numpy func:\n{hist3}")
