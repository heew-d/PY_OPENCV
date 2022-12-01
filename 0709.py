# 0709 cv2.distanceTransform()거리 계산

import cv2
import numpy as np

#1
src = np.zeros(shape=(512,512), dtype=np.uint8)
cv2.rectangle(src, (50, 200), (450, 300), (255,255,255), -1)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src)
print('src:', minVal, maxVal, minLoc, maxLoc)

#2
# 거리 변환(Distance Transform)은 바이너리 이미지(Binary Image)에서
# 픽셀값이 0인 배경으로부터의 거리를 해당 픽셀 영역에 표현하는 방법
# 배경으로부터 멀리 떨어져 있을 수록 높은 픽셀 값을 가짐
dist = cv2.distanceTransform(src, distanceType=cv2.DIST_L1, maskSize=3)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)
print('dist:', minVal, maxVal, minLoc, maxLoc)

dst = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
ret, dst2 = cv2.threshold(dist, maxVal-1, 255, cv2.THRESH_BINARY)

#3
gx = cv2.Sobel(dist, cv2.CV_32F, 1, 0, ksize=3)
gy = cv2.Sobel(dist, cv2.CV_32F, 0, 1, ksize=3)
mag = cv2.magnitude(gx, gy)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(mag)
print('mag:', minVal, maxVal, minLoc, maxLoc)
ret, dst3 = cv2.threshold(mag, maxVal-2, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()