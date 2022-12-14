# 0416.py  영상 어파인 변환(확대/축소, 회전)

import cv2
src = cv2.imread('./data/lena.jpg')

rows, cols, channels = src.shape
M1 = cv2.getRotationMatrix2D((rows / 2, cols / 2), 45, 0.5)
M2 = cv2.getRotationMatrix2D((rows / 2, cols / 2), -45, 1.0)

print('M1', M1)

dst1 = cv2.warpAffine(src, M1, (rows, cols))
dst2 = cv2.warpAffine(src, M2, (rows, cols))

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()