# 0610.py morphologyEx() 모폴로지 연산

import cv2
import numpy as np

src = cv2.imread('./data/morphology.jpg', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))

# 침식 -> 팽창
closing = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel, iterations=5)
# 팽창 -> 침식
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=5)

# 팽창 - 침식
gradient = cv2.morphologyEx(opening, cv2.MORPH_GRADIENT, kernel)

# 원본 - 열림
tophat = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel, iterations=5)
# 닫힘 - 원본
blackhat = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel, iterations=5)

cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('gradient', gradient)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)
cv2.waitKey()
cv2.destroyAllWindows()