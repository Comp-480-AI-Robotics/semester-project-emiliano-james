import cv2
import numpy as np

img = cv2.imread('./kuri.jpg')

# resize image
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# draw circles around eyes
# newImg, contours, hier = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
#     cntArea = cv2.contourArea(cnt)
#     if cnt.Area > 1000:
#         ellipse = cv2.fitEllipse(cnt)


# draw heart circle
img = cv2.circle(img, (width//2, height - 100), 60, (255, 0, 0), -1)
cv2.imshow('kuri', img)

cv2.waitKey(0)
