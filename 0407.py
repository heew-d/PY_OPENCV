# 0407.py 마우스로 ROI 영역 지정
import cv2

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)


# print('roi = ', roi)
dst = src.copy()
# 원본 이미지를 띄우고, 마우스 이벤트 처리도 도와줌
roi = cv2.selectROI(src)
print('roi = ', roi)
N = 32

height, width = src.shape[0:2]

# 512/64
h = height // N
w = width // N

if roi != (0,0,0,0):
    img = src[roi[1]:roi[1] + roi[3], roi[0]: roi[0] + roi[2]]

# rect = [(roi[1],roi[0]), roi[3], roi[2]]

# startY = rect[0][0]
# startX = rect[0][1]
# endY = startY + rect[1]
# endX = startX + rect[2]

startY = roi[1]
startX = roi[0]
endY = startY + roi[3]
endX = startX + roi[2]

for y in range(startY, endY, h): #range(start, stop, step)
    for x in range(startX, endX, w):
        roi = src[y:y + h, x:x + w]
        dst[y:y + h, x:x + w] = cv2.mean(roi)[0] # [B,G,R]

    
    # cv2.imshow('Img', img)
    # cv2.waitKey()
cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()
