#0710-3.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

# 비디오 캡쳐준비 0번 카메라가 메인 카메라, 간혹 1번일때도 있음
# 해당 웹캠의 usb는 다른곳에서 사용중이면 안됨(usb 포트는 하나의 연결만 지원)
cap = cv2.VideoCapture(0)

frame_size = (
    int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)
print('frame_size =', frame_size)

# mask = np.zeros(shape=(frame_size[0], frame_size[1]), dtype=np.uint8)
# markers = np.zeros(shape=(frame_size[0], frame_size[1]), dtype=np.int32)

# cv2.circle(mask, (10,10), 10, (255,255,255), -1)
# cv2.circle(mask, (frame_size[0]//2,frame_size[1]//2), 10, (255,255,255), -1)

if not cap.isOpened():
    print('fail')

while True:
    retval, frame = cap.read()
    key = cv2.waitKey(50)
    
    if key == 0x1B:  #esc, 27
        break

    if retval == False:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, gray = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    dist = cv2.distanceTransform(gray, cv2.DIST_L1, 3)
    dist8 = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)
    mask = (dist > maxVal * 0.5).astype(np.uint8) * 255
    mode = cv2.RETR_EXTERNAL
    method = cv2.CHAIN_APPROX_SIMPLE
    contours, hierarchy = cv2.findContours(mask, mode, method)
    # contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    markers = np.zeros(shape=frame.shape[:2], dtype=np.int32)
    for i, cnt in enumerate(contours):
        cv2.drawContours(markers, [cnt], 0, i+1, -1)
    
    dst = frame.copy()
    cv2.watershed(frame, markers)

    dst[markers == -1] = [0,0,255]
    for i in range(len(contours)):
        r = np.random.randint(256)
        g = np.random.randint(256)
        b = np.random.randint(256)
        dst[markers == i+1] = [b,g,r]

    dst = cv2.addWeighted(frame, 0.4, dst, 0.6, 0) 

    cv2.imshow('dst', dst)

cv2.destroyAllWindows()