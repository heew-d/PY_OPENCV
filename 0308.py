# 0308.py 다각형 채우기

import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

pts1 = np.array([[100,100],[200,100],[200,200],[100,200]])
pts2 = np.array([[300,200],[400,100],[400,200]])

# pts3 = np.array([[110, 110], [270,110], [300, 330], [170,170], [150,250]])


cv2.fillConvexPoly(img, pts1, color=(255,0,0))

cv2.fillPoly(img, [pts2], color=(0,0,255))
# cv2.fillPoly(img, [pts1,pts2], color=(0,0,255))
# cv2.fillConvexPoly(img, pts3, color=(255,255,0))
# cv2.fillPoly(img, [pts3], color=(255,0,255))
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()