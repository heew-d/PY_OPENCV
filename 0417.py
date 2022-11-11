# 0417.py  영상 연산 1: 영상 덧셈

import cv2
import numpy as np

src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(shape=(512, 512), dtype=np.uint8) + 100

# r = (x + 100) % 256
dst1 = src1 + src2

# r = min(255, x+100)
dst2 = cv2.add(src1, src2)

dst3 = cv2.add(src1, src2, dtype=cv2.CV_8U)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()