# 0301.py 직선 및 사각형 그리기

import cv2
import numpy as np

# white 배경
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
# img = np.ones((512,512,3), np.uint8) * 255
# img = np.full((512,512,3), (255,255,255) , dtype= np.uint8)
# img = np.zeros((512,512,3), np.uint8) # Black 배경

# 사각형
pt1 = (100,100)
pt2 = (400,400)
# OpenCV는 BGR 컬러
cv2.rectangle(img, pt1, pt2, (0,255,0),2)

# 선 두개
cv2.line(img,(0,0),(500,0),(255,0,0),5)
cv2.line(img,(0,0),(0,500),(0,0,255),5)

# 윈도우에 표시
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()