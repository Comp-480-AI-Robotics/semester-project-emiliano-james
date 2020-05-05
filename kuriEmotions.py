import cv2
import time


class kuriGUI:

    def __init__(self):

        self.img = cv2.imread('./kuri_resized.jpg')
        self.height, self.width = self.img.shape[0], self.img.shape[1]

        # format: [circle color, start eye angle, end eye angle, eye thickness]
        self.emotions = {'negative': [(159, 159, 255), 0, 360, -1], 'positive': [(137, 240, 255), 0, 180, 20], 'neutral': [(200, 200, 200), 0, 360, -1]}

        # variables for eyes
        self.right_eye = ((433.57440185546875, 346.8737487792969), (78.96944427490234, 88.37602996826172), 178.60519409179688)
        self.right_center = int(self.right_eye[0][0]), int(self.right_eye[0][1])
        self.right_axes = int(self.right_eye[1][0]) // 2 + 2, int(self.right_eye[1][1]) // 2 + 2

        self.left_eye = ((267.5984191894531, 346.9773254394531), (79.46482849121094, 88.4059066772461), 1.4226665496826172)
        self.left_center = int(self.left_eye[0][0]), int(self.left_eye[0][1])
        self.left_axes = int(self.left_eye[1][0]) // 2 + 2, int(self.left_eye[1][1]) // 2 + 2

        self.theta = 178.60519409179688

    def clearEyes(self):
        self.img = cv2.ellipse(self.img, self.left_center, (self.left_axes[0] + 12, self.left_axes[1] + 12), self.theta, 0, 360,
                               (245, 245, 245), thickness=-1)
        self.img = cv2.ellipse(self.img, self.right_center, (self.right_axes[0] + 12, self.right_axes[1] + 12), self.theta, 0, 360,
                               (245, 245, 245), thickness=-1)

    def drawEyes(self, emotion):
        self.img = cv2.ellipse(self.img, self.left_center, self.left_axes, self.theta, self.emotions[emotion][1],
                               self.emotions[emotion][2], (0, 0, 0), thickness=self.emotions[emotion][3])
        self.img = cv2.ellipse(self.img, self.right_center, self.right_axes, self.theta, self.emotions[emotion][1],
                               self.emotions[emotion][2], (0, 0, 0), thickness=self.emotions[emotion][3])

    def drawCircle(self, color):
        a = 50
        grow = True
        while True:
            cv2.circle(self.img, (self.width // 2, self.height - 100), a, color, -1)
            cv2.imshow('kuri', self.img)
            time.sleep(0.005)
            cv2.circle(self.img, (self.width // 2, self.height - 100), a, (248, 248, 248), -1)
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

    def runKuri(self):
        while True:
            emotion = input("Emotion (negative, positive, neutral) (Type 'q' to quit): ")
            if emotion.lower() == "q":
                break

            self.clearEyes()
            self.drawEyes(emotion)

            circleColor = self.emotions[emotion.lower()][0]
            self.drawCircle(circleColor)


if __name__ == '__main__':
    kuri = kuriGUI()
    kuri.runKuri()

    cv2.destroyAllWindows()
