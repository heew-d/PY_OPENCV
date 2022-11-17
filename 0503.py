# 0503.py 히스토그램 계산 1

import cv2
import numpy as np

src = np.array([[0,0,0,0],
                [1,1,3,5],
                [6,1,1,3],
                [4,3,1,7]
                ], dtype=np.uint8)

# ranges = [0, 8] => [0, 1], [2, 3], [4, 5], [6, 7]
hist1 = cv2.calcHist(images=[src], channels= [0], mask=None, histSize=[4], ranges=[0,8])
print('hist1 =', hist1)

# ranges = [0, 4] => [0], [1], [2], [3]
hist2 = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[4], ranges=[0,4])
print('hist2 = ', hist2)