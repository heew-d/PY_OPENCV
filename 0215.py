# 0215.py animation.FuncAnimation 4 : 서브플롯

import cv2 
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
from matplotlib import pyplot as plt, animation

class Video(animation.FuncAnimation):
    def __init__(self, device = 0, fig = None, frames = None, interval = 80, repeat_delay = 5, blit = False, **kwargs):
        # self.im1.set_array(cv2.merge((gray, gray, gray)))

        if fig is None:
            self.fig, self.ax = plt.subplots(1,2,figsize = (10,5))
            self.fig.canvas.manager.set_window_title('Video Capture')
            self.ax[0].set_position([0,0,0.5,1])
            self.ax[0].axis('off')

            self.ax[1].set_position([0.5,0,0.5, 1])
            self.ax[1].axis('off')

        super(Video, self).__init__(self.fig, self.updateFrame, init_func=self.videoInit, frames=frames, interval = interval, blit = blit, repeat_delay = repeat_delay, **kwargs)
        self.cap = cv2.VideoCapture(device)
        print('start capture ...')

    def videoInit(self):
        retval, self.frame = self.cap.read()
        if retval:
            self.im0 = self.ax[0].imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB), aspect='auto')

            print(f'frame shape: {self.frame.shape}, dtype: {self.frame.dtype}')

            # self.im1 = self.ax[1].imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB), aspect='auto')
            self.im1 = self.ax[1].imshow(np.zeros(self.frame.shape, self.frame.dtype), aspect = 'auto')
    
    def updateFrame(self, k):
        retval, self.frame = self.cap.read()
        if retval:
            self.im0.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            self.im1.set_array(cv2.merge((gray, gray, gray)))

    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture.')

# 프로그램 시작
camera = Video('./data/vtest.avi')
plt.show()
camera.close()