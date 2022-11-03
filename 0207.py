# 0207.py  비디오 캡쳐와 화면표시 1

import cv2

cap = cv2.VideoCapture(0) # 0번 카메라

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)

while True:
    retval, frame = cap.read() # 프레임 캡처

    if not retval:
        break

    cv2.imshow('frame', frame)

    key = cv2.waitKey(50)
    if key == 27:
        break
if cap.isOpened:
    cap.release()
cv2.destroyAllWindows()