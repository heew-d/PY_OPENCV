# 0421.py 2차원 균등분포 난수 좌표

import cv2
import numpy as np
import time

nPoints =100
pts = np.zeros((1,nPoints, 2), dtype=np.uint16)

while True:
    dst = np.full((512,512,3), (255,255,255), dtype=np.uint8)

    cv2.setRNGSeed(int(time.time()))
    cv2.randu(pts,(0,0), (512,512)) # 점이 어디에 찍힐지 기록

    #draw points
    for k in range(nPoints): # 100개의 x,y 값이 난수로 생성됨
        x,y = pts[0,k][:] # 0번 인덱스 안에 k번째
        cv2.circle(dst, (x,y), radius=5, color=(255,120,120), thickness=-1)

    cv2.imshow('dst', dst)

    key = cv2.waitKey()
    if key == 27:
        break

cv2.destroyAllWindows()