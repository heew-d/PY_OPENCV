# 0212-2.py  비디오 디스플레이 1
from copy import deepcopy
import cv2 
import time

class Animator():
    def __init__(self, winname, initFunc, updateFrameFunc, stopFunc, pauseFunc, interval):
        self.__winname = winname
        
        self.__initFunc = initFunc
        self.__updateFrameFunc = updateFrameFunc
        self.__stopFunc = stopFunc
        self.__pauseFunc = pauseFunc
        self.__interval = interval

    def show(self):
        # 처음으로 한번만 동작하는 초기화 함수를 호출
        # 타이밍, 처리구조를 설계(방법을 설계). 값이 처리는게 아님
        self.__initFunc(self.__winname)
        
        frameCount = 1
        # 루프 지정된 간격으로 프레임을 갱신하는 함수 호출
        while True:
            retval = self.__updateFrameFunc(self.__winname, frameCount)

            # if not retval:
            #     break

            # interval의 값만큼 지연
            # time.sleep(self.__interval / 1000)
            key = cv2.waitKey(self.__interval)

            if key == 27: # esc
                # 영상 정지 호출
                self.__stopFunc(self.__winname)
                break

            if key == 32: # 스페이스
                # 영상 일시정지
                self.__pauseFunc(self.__winname)
                while True:
                    key = cv2.waitKey()
                    if key == 32:
                        break

            frameCount += 1

def videoInit(winname):
    retval, frame = cap.read()

    # 여기에 문구를 합성
    cv2.putText(frame, text="READY", org=(50,50), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,0,0), thickness=2)
    cv2.imshow(winname, frame)


currentFrame = None

def updateFrame(winname, k):

    retval, frame = cap.read()

    global currentFrame
    currentFrame = frame.copy()

    if retval:
        # 여기에 문구를 합성
        cv2.putText(frame, text="PLAY", org=(50,50), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,0,0), thickness=2)
        cv2.imshow(winname, frame)

    return retval

def videoStop(winname):
    # retval, frame = cap.read()
    frame = currentFrame.copy()

    cv2.putText(frame, text="STOP", org=(50,50), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2)
    cv2.imshow(winname, frame)

    cv2.waitKey()
    pass

def videoPause(winname):
    # TODO 현재프레임을 읽어올 방법이 필요!
    frame = currentFrame.copy()
    # retval, frame = cap.read() # 다음 프레임

    cv2.putText(frame, text="PAUSE", org=(50,50), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,255), thickness=2)
    cv2.imshow(winname, frame)

cap = cv2.VideoCapture('./data/vtest.avi')
# retval, frame = cap.read()
# cv2.imshow('video', frame)

# 콜백함수를 연결
# ani : 생성자를 통해 완성된 인스턴스
ani = Animator('video1', videoInit, updateFrame, videoStop, videoPause, 50)

# show, 재생시작
ani.show()

# 열어뒀던 버퍼를 닫는다. 하드웨어와의 연결 해제
if cap.isOpened():
    cap.release()