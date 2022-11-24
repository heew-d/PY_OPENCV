# 0511.py 배열의 히스토그램 평활화
import cv2
import numpy as np

src = np.array([
    [2,2,4,4],
    [2,2,4,4],
    [4,4,4,4],
    [4,4,4,4]
], dtype=np.uint8)

#1
dst = cv2.equalizeHist(src)
print('dst =', dst)

#2
hist, bins = np.histogram(src.flatten(), 256, [0,256])
cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf, 0)
T = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
T = np.ma.filled(T, 0).astype('uint8')
dst2 = T[src]