# 0302.py 직선-사각형 교차점

import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

x1, x2 = 100, 400
y1, y2 = 100, 400
cv2.rectangle(img, (x1,y1), (x2,y2),(0,0,255))

pt1 = 120,50
pt2 = 300, 500
cv2.line(img, pt1, pt2, (255,0,0), 2)

imgRect = (x1,y1,x2-x1, y2-y1) # (x축, y축, 넓이, 높이)
retval, rpt1, rpt2 = cv2.clipLine(imgRect, pt1, pt2)

print('retval: ', retval)
print('rpt1: ', rpt1)
print('rpt2: ', rpt2)

if retval:
    cv2.circle(img, rpt1, radius=5, color=(0,255,0), thickness=-1)
    cv2.circle(img, rpt2, radius=5, color=(0,255,0), thickness= -1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()