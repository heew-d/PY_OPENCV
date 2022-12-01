# 자동차 번호판
import cv2
import numpy as np
import matplotlib.pyplot as plt

#1
src = cv2.imread('./data/car_num1.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, res = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('res', res)

# #2 
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res)
print('ret=', ret)
print('stats=', stats)
print('centroids=', centroids)

# #3
# dst = np.zeros(src.shape, dtype=src.dtype)

#4
dst = src.copy()
for i in range(1, int(ret)):
    x, y, width, height, area = stats[i]

    print('area=', area)

    if area < 300 or area > 4000:
        continue

    cv2.rectangle(dst, (x, y), (x+width, y+height), (0,0,255), 2)
    # cx, cy = centroids[i]
    # cv2.circle(dst, (int(cx), int(cy)), 5, (255,0,0),-1)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

