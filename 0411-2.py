# 0411.py 채널 분리

import cv2
import numpy as np

# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_COLOR)
src = cv2.imread('./data/lena.jpg')

def split(src):
    dst = []
    shape = src.shape
    if len(shape) < 3:
        # 한채널만
        dst.append(src)
        return dst
    channel = shape[2]

    for i in range(channel):

        dst.append(src[:,:, i])
    
    return dst

shape = src.shape[0], src.shape[1], 3
blue = np.zeros(shape, dtype=np.uint8)
green = np.zeros(shape, dtype=np.uint8)
red = np.zeros(shape, dtype=np.uint8)

# b, g, r = cv2.split(src)
# dst = cv2.split(src)
dst = split(src)

blue[:,:,0] = dst[0]
green[:,:,1] = dst[1]
red[:,:,2] = dst[2]

# dst = cv2.split(src)
cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

cv2.waitKey()
cv2.destroyAllWindows()