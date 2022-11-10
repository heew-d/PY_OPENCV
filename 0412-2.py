# 0412.py 채널 병합

import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')

# shape = src.shape[0], src.shape[1], 3
# dst = np.zeros(shape, dtype=np.uint8)

# zeros = np.zeros(src.shape[:2], dtype="uint8")
zeros = np.zeros((src.shape[0], src.shape[1], 1), dtype="uint8")
b, g, r = cv2.split(src)
# merged = cv2.merge((B,G,R))
bMat = cv2.merge([b, zeros, zeros])
gMat = cv2.merge([zeros, g, zeros])
rMat = cv2.merge([zeros, zeros, r])

cv2.imshow('blue', bMat)
cv2.imshow('green', gMat)
cv2.imshow('red', rMat)

cv2.waitKey()
cv2.destroyAllWindows()