import cv2
import time

# format: [circle color, start eye angle, end eye angle, eye thickness]
emotions = {'negative': [(159, 159, 255), 0, 360, -1], 'positive': [(137, 240, 255), 0, 180, 20], 'neutral': [(200, 200, 200), 0, 360, -1]}

# variables for eyes
right_eye = ((433.57440185546875, 346.8737487792969), (78.96944427490234, 88.37602996826172), 178.60519409179688)
right_center = int(right_eye[0][0]), int(right_eye[0][1])
right_axes = int(right_eye[1][0]) // 2 + 2, int(right_eye[1][1]) // 2 + 2

left_eye = ((267.5984191894531, 346.9773254394531), (79.46482849121094, 88.4059066772461), 1.4226665496826172)
left_center = int(left_eye[0][0]), int(left_eye[0][1])
left_axes = int(left_eye[1][0]) // 2 + 2, int(left_eye[1][1]) // 2 + 2

theta = 178.60519409179688


def clearEyes(img):
    img = cv2.ellipse(img, left_center, (left_axes[0] + 12, left_axes[1] + 12), theta, 0, 360, (245, 245, 245),
                      thickness=-1)
    img = cv2.ellipse(img, right_center, (right_axes[0] + 12, right_axes[1] + 12), theta, 0, 360, (245, 245, 245),
                      thickness=-1)


def drawEyes(emotion, img):
    img = cv2.ellipse(img, left_center, left_axes, theta, emotions[emotion][1], emotions[emotion][2], (0, 0, 0),
                      thickness=emotions[emotion][3])
    img = cv2.ellipse(img, right_center, right_axes, theta, emotions[emotion][1], emotions[emotion][2], (0, 0, 0),
                      thickness=emotions[emotion][3])


def drawCircle(color, img):
    a = 50
    grow = True
    while True:
        cv2.circle(img, (width // 2, height - 100), a, color, -1)
        cv2.imshow('kuri', img)
        time.sleep(0.005)
        cv2.circle(img, (width // 2, height - 100), a, (248, 248, 248), -1)
        if grow:
            a += 1
        else:
            a -= 1
        if a >= 70:
            grow = False
        if a <= 50:
            grow = True
        k = cv2.waitKey(10)
        if k == 27:
            break


if __name__ == '__main__':
    img = cv2.imread('./kuri_resized.jpg')
    height, width = img.shape[0], img.shape[1]

    while True:
        emotion = input("Emotion (negative, positive, neutral) (Type 'q' to quit): ")
        if emotion.lower() == "q":
            break

        clearEyes(img)
        drawEyes(emotion, img)

        circleColor = emotions[emotion.lower()][0]
        drawCircle(circleColor, img)

    cv2.destroyAllWindows()
