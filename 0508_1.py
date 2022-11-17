# 동영상에서 히스토그램 역투영
import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 비디오 객체 생성
# cap = cv2.VideoCapture('./data/vtest.avi') # 비디오 객체 생성

retval, frame = cap.read() # 첫 프레임 읽어오기
# bgr을 hsv로 변환 후 hsv를 쪼갬
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# 영역 선택
roi = cv2.selectROI('img', frame)
roi_h = h[roi[1]:roi[1] + roi[3], roi[0]:roi[0]+roi[2]]

# 영상이 끝나거나 esc 키를 누를 때까지 반복
while True:
    retval, frame = cap.read() # 첫 프레임 읽어오기

    if not retval:
        break
    cv2.imshow('frame', frame)

    # bgr을 hsv로 변환 후 hsv를 쪼갬
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    # 선택 영역의 h(hue)를 히스토그램으로 만들고 역투영하기
    hist = cv2.calcHist([roi_h], [0], None, [64], [0,256])
    backP = cv2.calcBackProject([h.astype(np.float32)], [0], hist, [0,256], scale=1.0)
    hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN + cv2.SORT_DESCENDING)
    k = 1
    T = hist[k][0] - 1

    # 역투영한것을 이진화 처리
    ret, dst = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)

    key = cv2.waitKey(25)
    if key == 27:
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
# hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)

# #2
# roi = cv2.selectROI(cap)
# print('roi = ', roi)
# roi_h = h[roi[1]:roi[1] + roi[3], roi[0]:roi[0]+roi[2]]
# hist = cv2.calcHist([roi_h], [0], None, [64], [0,256])
# backP = cv2.calcBackProject([h.astype(np.float32)], [0], hist, [0,256], scale=1.0)


# #3
# hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN + cv2.SORT_DESCENDING)
# k = 1
# T = hist[k][0] - 1
# print('T = ', T)
# ret, dst = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)

# dst = dst.astype(np.uint8)
# dst2 = cv2.copyTo(src, mask=dst)

# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()