import cv2
import numpy as np

emotions = {'negative': (0, 0, 255), 'positive': (0, 255, 255), 'neutral': (128, 128, 128)}
img = cv2.imread('./kuri.jpg')

# resize image
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# draw circles around eyes
greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res, thresh = cv2.threshold(greyImg, 120, 255, 0)
newImg, contours, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
eyes = []
for cnt in contours:
    cntArea = cv2.contourArea(cnt)
    if 5000 < cntArea < 10000:
        eyes = cnt
        ellipse = cv2.fitEllipse(eyes)
        img = cv2.ellipse(img, ellipse, (0, 0, 0 ), thickness=-1)

# draw heart circle
img = cv2.circle(img, (width//2, height - 100), 60, (128, 128, 128), -1)
cv2.imshow('kuri', img)


# def changeEmotion(emotion):
#     color = emotions[emotion]
#     cv2.circle(img, (width // 2, height - 100), 60, color, -1)
#     cv2.imshow('kuri', img)


# emotion = input("Pick emotion (positive, negative, neutral): ")
# changeEmotion(emotion)

cv2.waitKey(0)
