import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('./data/infrared_road.jpg')
# print('shape: ', src.shape)
height, width, channel = src.shape

dst = src.copy()

hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

# cv2.inRange(dst, 하한, 상한)
# 빨간색 범위만 가져오자
# 255 - 30 = 255 ~ 255, 0 ~ 130
mask = cv2.inRange(hsv, (-30, 0, 100), (130, 255, 255))

dst = cv2.copyTo(src, mask=mask)

# N = 6
h = height // 5
w = width // 7

for i in range(6):
    for j in range(8):
        y = i * h
        x = j * w
        roi = dst[y:y+h, x:x+w]
        dst[y:y+h, x:x+w]= cv2.mean(roi)[0:3]
        cv2.putText(dst[y:y+h, x:x+w], f'{i,j}', (5,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        # cv2.putText(dst[y:y+h, x:x+w], f'{src[y:y+1, x,1]}', (5,40),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# 선 그리기
for i in range(w,width-w,w):
    pt1 = i, 0
    pt2 = i, height
    cv2.line(dst, pt1, pt2, (255,255,255), 2)
    print()
for i in range(h,height,h):
    pt1 = 0,i
    pt2 = width, i
    cv2.line(dst, pt1, pt2, (255,255,255), 2) 



# print('hsv', hsv)

# 0 < B < 100, 128 < G < 255, 0 < R < 100
# img_mask = cv2.inRange(hsv, (0,100,0), (255, 255, 255))
# print('img_mask:', img_mask)

# img_result= cv2.bitwise_and(src, src, mask=mask)
# print('img_result:', img_result)
# h, s, v = cv2.split(hsv)


cv2.imshow('dst', dst)
# cv2.imshow('mask', mask)
# cv2.imshow('img_result', img_result)
cv2.waitKey()
cv2.destroyAllWindows()