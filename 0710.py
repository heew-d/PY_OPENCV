# 0710 cv2.watershed() 영상 분할
import cv2
import numpy as np

#1
src = cv2.imread('./data/hand.jpg')
# src = cv2.imread('./data/flower.jpg')
mask = np.zeros(shape=src.shape[:2], dtype=np.uint8)
markers = np.zeros(shape=src.shape[:2], dtype=np.int32)
dst = src.copy()
cv2.imshow('dst', dst)

#2
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(param[0], (x, y), 10, (255,255,255), -1)
            cv2.circle(param[1], (x, y), 10, (255,255,255), -1)
    cv2.imshow('dst', param[1])

#3
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
while True:
    cv2.setMouseCallback('dst', onMouse, [mask, dst]) # 3-1
    key = cv2.waitKey(30)
    
    if key == 0x1B: # esc, 27
        break
    elif key == ord('r'): # 3-2
        mask[:,:] = 0
        dst = src.copy()
        cv2.imshow('dst', dst)
    elif key == ord(' '): # 3-3
        contours, hierarchy = cv2.findContours(mask, mode, method)
        print('len(contours)=', len(contours))
        markers[:,:] = 0
        for i, cnt in enumerate(contours):
            cv2.drawContours(markers, [cnt], 0, i+1, -1)

        # 그레이스케일 이미지에서 높은 필셀값을 가지는 부분을 언덕으로 보고,
        # 낮은 픽셀값을 가지는 부분을 계곡으로 볼 수 있다.
        # 한 이미지에 여러 개의 고립된 계곡(극소점)이 있을 수 있다.
        # 각각 다른 색의 물(라벨)로 물을 채운다고 하자
        cv2.watershed(src, markers)

        # 3-4
        dst = src.copy()
        dst[markers == -1] = [0,0,255] # 경계선 
        for i in range(len(contours)): # 분할영역
            r = np.random.randint(256)
            g = np.random.randint(256)
            b = np.random.randint(256)
            dst[markers == i+1] = [b,g,r]

            dst = cv2.addWeighted(src, 0.4, dst, 0.6,0) # 합성
            cv2.imshow('dst', dst)
cv2.destroyAllWindows()