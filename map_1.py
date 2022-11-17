import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('./data/infrared_road.jpg')
dst = src.copy()

hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

# cv2.inRange(dst, 하한, 상한)
# 빨간색 범위만 가져오자
# 255 - 30 = 255 ~ 255, 0 ~ 130
mask = cv2.inRange(hsv, (-30, 0, 100), (130, 255, 255))
# ret, mask2 = cv2.threshold(y, 100, 255, cv2.THRESH_BINARY)

dst = cv2.copyTo(src, mask=mask)

cv2.imshow('preview', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()