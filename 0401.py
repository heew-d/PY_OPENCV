# 0401.py  영상 속성 1: 모양과 자료형

import cv2
import numpy as np

# cv2.IMREAD_UNCHANGED == -1, 
# cv2.IMREAD_GRAYSCALE == 0, 
# cv2.IMREAD_COLOR == 1
# img = cv2.imread('./data/lena.jpg')
img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('./data/lena.jpg', 0)

print('img.ndim =', img.ndim)
print('img.shape =', img.shape)
print('img.dtype =', img.dtype)

img = img.astype(np.int32)
print('img.dtype =', img.dtype)

img = np.uint8(img)
print('img.dtype =', img.dtype)