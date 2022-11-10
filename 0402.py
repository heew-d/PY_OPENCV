# 0402.py 영상 속성 2: 모양 변경하기

import cv2 
import numpy as np

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
print('img.shape =', img.shape)
img = img.flatten()
print('img.shape= ', img.shape)

img = img.reshape(-1, 512, 512)
print('img.shape = ', img.shape)

cv2.imshow('img', img[0])
cv2.waitKey()
cv2.destroyAllWindows()