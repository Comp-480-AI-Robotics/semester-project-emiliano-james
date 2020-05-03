import cv2
import time

emotionColors = {'negative': (0, 0, 255), 'positive': (0, 255, 255), 'neutral': (128, 128, 128)}
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
left_center, left_axes, right_center, right_axes, theta = None, None, None, None, None
for cnt in contours:
    cntArea = cv2.contourArea(cnt)
    if 5000 < cntArea < 10000:
        eyes = cnt
        ellipse = cv2.fitEllipse(eyes)
        img = cv2.ellipse(img, ellipse, (0, 0, 0), thickness=-1)
        if ellipse[0][0] < width//2:
            left_center = int(ellipse[0][0]), int(ellipse[0][1])
            left_axes = int(ellipse[1][0])//2 + 2, int(ellipse[1][1])//2 + 2
        else:
            theta = ellipse[2]
            right_center = int(ellipse[0][0]), int(ellipse[0][1])
            right_axes = int(ellipse[1][0]) // 2 + 2, int(ellipse[1][1]) // 2 + 2

# Happy Eyes
img = cv2.ellipse(img, left_center, left_axes, theta, 0, 360, (245, 245, 245), thickness=-1)
img = cv2.ellipse(img, right_center, right_axes, theta, 0, 360, (245, 245, 245), thickness=-1)

img = cv2.ellipse(img, left_center, left_axes, theta, 0, 180, (0, 0, 0), thickness=20)
img = cv2.ellipse(img, right_center, right_axes, theta, 0, 180, (0, 0, 0), thickness=20)

# draw heart circle

# For transparency (not working right now)
# overlay = img.copy()
# output = img.copy()


def changeCircle(color):
    a = 40
    grow = True
    while True:
        cv2.circle(img, (width//2, height - 100), a, color, -1)
        # cv2.addWeighted(overlay, 0.4, output, 0.6, 0, output) # doesn't work correctly
        time.sleep(0.005)
        cv2.imshow('kuri', img)
        cv2.circle(img, (width // 2, height - 100), a, (248, 248, 248), -1)
        if grow:
            a += 2
        else:
            a -= 2
        if a >= 80:
            grow = False
        if a <= 40:
            grow = True
        k = cv2.waitKey(10)
        if k == 27:
            break


if __name__ == '__main__':
    cv2.imshow('kuri', img)
    cv2.waitKey(0)

    while True:
        txt = input("Emotion (negative, positive, neutral) (Type 'q' to quit): ")

        if txt.lower() == "q":
            break

        color = emotionColors[txt.lower()]
        changeCircle(color)

changeCircle((0, 0, 255))
cv2.destroyAllWindows()
