# 0506.py 히스토그램 계산 4: 컬러 영상의 2채널 히스토그램

import cv2
from matplotlib import pyplot as plt

bgr = cv2.imread('./data/lena.jpg')
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

#1
hist01 = cv2.calcHist([bgr],[0,1],None, [32,32],[0,256,0,256])

plt.title('hist01')
plt.ylim(0,31)
plt.imshow(hist01, interpolation="nearest")
plt.show()

#2
hist02 = cv2.calcHist([bgr], [0,2], None,[32,32], [0,256,0, 256])
plt.title('hist02')
plt.ylim(0,31)
plt.imshow(hist02, interpolation="nearest")
plt.show()

#3
hist12 = cv2.calcHist([bgr], [1,2], None, [32,32], [0,256,0,256])
plt.title('hist12')
plt.ylim(0,31)
plt.imshow(hist12, interpolation="nearest")
plt.show()