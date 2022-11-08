# 0310.py 키보드 이벤트 처리

import numpy as np
import cv2

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0 # right

while True:
    key = cv2.waitKeyEx(30)
    print('key: ', key)
    if key == 0x1B:
        break
# 방향키 전환
    elif key == 65363: # right  d: 0x64
        print('right:: ')
        direction = 0
    elif key == 65364: # down  s: 0x73
        print('down:: ')
        direction = 1
    elif key == 65361: # left  a: 0x61
        print('left:: ')
        direction = 2
    elif key == 65362: # up  w:	0x77
        print('up:: ')
        direction = 3

# 방향으로 이동
    if direction == 0: #right
        x += 10
    elif direction == 1: #down
        y += 10
    elif direction == 2: # left
        x -= 10
    elif direction == 3: # up
        y -= 10

# 경계확인
    if x<R:
        x= R
        direction = 0
    if x > width - R:
        x = width -R
        direction = 2

    if y < R:
        y = R
        direction = 1
    if y>height - R:
        y = height - R
        direction = 3

# 지우고, 그리기
    img = np.zeros((width, height, 3), np.uint8) + 255 # 지우기
    cv2.circle(img, (x, y), R, (0,0,255), -1)
    cv2.imshow('img', img)

cv2.destroyAllWindows()