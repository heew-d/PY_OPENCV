#0201.py  영상 파일 읽기 및 화면표시

import cv2
import numpy as np

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile) # 이미지 행렬을 담아둘 변수 생성, 컬러이미지
# cv2.IMREAD_UNCHANGED == -1, cv2.IMREAD_GRAYSCALE == 0, cv2.IMREAD_COLOR == 1
img2 = cv2.imread(imageFile, 0)

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

cv2.waitKey()
cv2.destroyAllWindows()