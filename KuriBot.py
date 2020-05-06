import cv2
import time
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

# format: [circle color, start eye angle, end eye angle, eye thickness]
# TODO: change attributes for somewhat negative and somewhat positive
SENTIMENT = {'very negative': [(159, 159, 255), 0, 360, -1], 'very positive': [(137, 240, 255), 0, 180, 20],
             'neutral': [(200, 200, 200), 0, 360, -1], 'somewhat negative': [(159, 159, 255), 0, 360, -1],
             'somewhat positive': [(137, 240, 255), 0, 180, 20]}

class KuriBot:

    def __init__(self, sentiment):

        self.img = cv2.imread('./kuri_resized.jpg')

        self.height, self.width = self.img.shape[0], self.img.shape[1]

        self.sentiment = sentiment

        # variables for circle
        self.color = SENTIMENT[self.sentiment][0]
        self.size = 50
        self.grow = True

        # variables for eyes
        self.right_eye = ((433.57440185546875, 346.8737487792969), (78.96944427490234, 88.37602996826172),
                          178.60519409179688)
        self.right_center = int(self.right_eye[0][0]), int(self.right_eye[0][1])
        self.right_axes = int(self.right_eye[1][0]) // 2 + 2, int(self.right_eye[1][1]) // 2 + 2

        self.left_eye = ((267.5984191894531, 346.9773254394531), (79.46482849121094, 88.4059066772461),
                         1.4226665496826172)
        self.left_center = int(self.left_eye[0][0]), int(self.left_eye[0][1])
        self.left_axes = int(self.left_eye[1][0]) // 2 + 2, int(self.left_eye[1][1]) // 2 + 2

        self.theta = 178.60519409179688

    def setSentiment(self, sentiment):
        self.sentiment = sentiment

    def drawEyes(self):
        # Clears previous eyes
        self.img = cv2.ellipse(self.img, self.left_center, (self.left_axes[0] + 12, self.left_axes[1] + 12),
                               self.theta, 0, 360, (245, 245, 245), thickness=-1)
        self.img = cv2.ellipse(self.img, self.right_center, (self.right_axes[0] + 12, self.right_axes[1] + 12),
                               self.theta, 0, 360, (245, 245, 245), thickness=-1)

        # Draws new eyes
        self.img = cv2.ellipse(self.img, self.left_center, self.left_axes, self.theta, SENTIMENT[self.sentiment][1],
                               SENTIMENT[self.sentiment][2], (0, 0, 0), thickness=SENTIMENT[self.sentiment][3])
        self.img = cv2.ellipse(self.img, self.right_center, self.right_axes, self.theta, SENTIMENT[self.sentiment][1],
                               SENTIMENT[self.sentiment][2], (0, 0, 0), thickness=SENTIMENT[self.sentiment][3])

    def drawCircle(self):
        cv2.circle(self.img, (self.width // 2, self.height - 100), self.size, self.color, -1)
        cv2.imshow('kuri', self.img)

        # Anh's experiments with using Tkinter to display OpenCV images - unsuccessful so far
        # self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        # image = ImageTk.PhotoImage(image=Image.fromarray(self.img))
        # label_image = Label(self.window, image=image)
        # label_image.image = image
        # label_image.pack(side="bottom", fill="both", expand="yes")
        # label_image.place(x=0, y=0, anchor="w")
        # mainloop()  # Start the GUI

        cv2.circle(self.img, (self.width // 2, self.height - 100), self.size, (248, 248, 248), -1)
        if self.grow:
            self.size += 1
        else:
            self.size -= 1
        if self.size >= 70:
            self.grow = False
        if self.size <= 50:
            self.grow = True
        # mainloop()

    def runKuri(self):
        # self.window = Tk()
        # self.window.title("Kuri Program")
        while True:
            self.drawEyes()
            self.drawCircle()
            # mainloop()

            k = cv2.waitKey(100)
            if k == 27:
                break

        # mainloop()
        cv2.destroyAllWindows()


# # Example of how to instantiate
# if __name__ == '__main__':
#     sentiment = 'positive'
#     kuri = KuriBot(sentiment)
#     kuri.runKuri()
#
#     cv2.destroyAllWindows()
