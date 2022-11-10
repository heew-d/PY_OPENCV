# 0411.py 채널 분리

import cv2

src = cv2.imread('./data/lena.jpg')

# row, col, color[1-3]
# bPx = src[0][0][0]
# bMat = src[:,:,0]
# gMat = src[:,:,1]
# rMat = src[:,:,2]
# dst = [bMat, gMat, rMat]
dst = cv2.split(src)

print(type(dst))
print(type(dst[0]))

cv2.imshow('blue', dst[0])
cv2.imshow('green', dst[1])
cv2.imshow('red', dst[2])

cv2.waitKey()
cv2.destroyAllWindows()