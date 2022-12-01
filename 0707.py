# 0707 윤곽선 검출 및 그리기2 :mode = cv2.RETR_LIST

import cv2
import numpy as np

#1
src = np.zeros(shape=(512,512,3), dtype=np.uint8)
cv2.rectangle(src, (50, 100), (450, 400), (255,255,255), -1)
cv2.rectangle(src, (100, 150), (400, 350), (0,0,0), -1)
cv2.rectangle(src, (200, 200), (300, 300), (255,255,255), -1)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

#2
mode = cv2.RETR_LIST
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(gray, mode, method)

print('len(contours)=', len(contours))
print('contours[0].shape=', contours[0].shape)
print('contours=', contours)
print('hierarchy=', hierarchy)

# 동생, 형, 첫째 자식, 부모
# next, previous, first child, parent
# [[
#   [ 1 -1 -1 -1]
#   [ 2  0 -1 -1]
#   [-1  1 -1 -1]
# ]]


#3
for cnt in contours:
    cv2.drawContours(src, [cnt], 0, (255,0,0), 3)
    
    for pt in cnt: # 윤곽선 좌표
        cv2.circle(src, (pt[0][0], pt[0][1]), 5, (0,0,255), -1)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()