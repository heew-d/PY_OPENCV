# 0209.py 비디오 입력과 화면표시3: 유튜브 동영상
'''
    pip install youtube_dl
    pip install pafy
'''

import cv2

# ..lib\site-packages\pafy\backend_youtube_dl.py, line 53
# like_count, dislike_count

import pafy
url = 'https://www.youtube.com/watch?v=czMwy7SYZjo'
# url = 'https://youtu.be/WOww2jMyUjU'
video = pafy.new(url)
best = video.getbest()
print("video: ", video)

print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)
print('best.resolution= ', best.resolution)

cap=cv2.VideoCapture(best.url)
# print("cap: ",cap)
# frame_size = (
#     int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
#     int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
# )

while(True):
    retval, frame = cap.read()

    if not retval:
        break
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100,200)
    cv2.imshow('edges', edges)
    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()
