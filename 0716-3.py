# 자동차 번호판

import cv2
import numpy as np
import matplotlib.pyplot as plt

#1
src = cv2.imread('./data/car_num2.jpg')

dst = src.copy()

# 이미지의 비율이 번호판의 비율이 되도록
h, w = src.shape[:2]
print('src.shape=', src.shape)
cx = w //2
cy = h //2

roiH = int(w * 0.25)
print('roiH: ', roiH)
dst = dst[cy -(roiH//2): cy+(roiH//2), :]
# dst = dst[h//3:(h//3)*2, :]


data = dst.reshape((-1,3)).astype(np.float32)

K = 3
term_crit = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, labels, centers = cv2.kmeans(data, K, None, term_crit, 5, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
res = centers[labels.flatten()]
dst = res.reshape(dst.shape)

gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res)
# print('ret=', ret)
# print('stats=', stats)
# print('centroids=', centroids)


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

