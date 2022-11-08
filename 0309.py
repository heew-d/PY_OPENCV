# 0309.py 문자열 출력

import numpy as np
import cv2

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
text = 'OpenCV Programming'
org = (50,100)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text, org, font, 1, (255,0,0), 2)

size, baseLine = cv2.getTextSize(text, font, 1, 2)
print('size: ', size)
print('baseLine: ', baseLine)

pts1 = (org[0] + size[0], org[1] - size[1])

cv2.rectangle(img, org, (pts1[0], pts1[1]), (0,0,255))
cv2.circle(img, org, 3, (0,255,0),2)

cv2.circle(img, pts1, 3, (255,255,0),2)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()