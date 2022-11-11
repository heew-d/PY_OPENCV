# 0422.py  cv.randu()에 2차원 정규분포 난수 좌표

import cv2
import numpy as np
import time

nPoints = 100
pts = np.zeros((1,nPoints, 2), dtype= np.uint16)

dst = np.full((512,512,3), (255,255,255), dtype=np.uint8)

while True:
    dst[:,:,:] = 255

    cv2.setRNGSeed(int(time.time()))

    cv2.randn(pts,mean=(256,256), stddev=(50,50))

    # draw points
    for k in range(nPoints):
        x,y = pts[0][k,:]
        cv2.circle(dst, (x,y), radius=5, color=(0,0,255), thickness= -1)

    cv2.imshow('dst', dst)  
    key = cv2.waitKey()
    if key == 27:
        break

cv2.destroyAllWindows()