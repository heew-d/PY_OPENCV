# 0209.py 비디오 입력과 화면표시3: 유튜브 동영상

'''
    pip install youtube_dl
    pip install pafy
'''
# import pafy
import cv2, pafy, youtube_dl
url = 'https://www.youtube.com/watch?v=czMwy7SYZjo'
# url = 'https://youtu.be/czMwy7SYZjo'
video = pafy.new(url)


print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest()

print('best.resolution= ', best.resolution)
cap=cv2.VideoCapture(best.url)

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
