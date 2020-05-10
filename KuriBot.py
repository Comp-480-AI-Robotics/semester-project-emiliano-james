"""  =================================================================
File: KuriBot.py
This file contains code for the KuriBot class that simulates a Kuri
robot by changing its facial expressions and heart light.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
 ==================================================================="""

import cv2
import os
import sys
import fcntl

# Stores the graphical variables for all 5 sentiments
# Format: [circle color, start eye angle, end eye angle, eye thickness]
SENTIMENT = {"very negative": [(112, 122, 255), 0, 360, -1],
             "very positive": [(130, 209, 126), 0, 180, 20],
             "neutral": [(200, 200, 200), 0, 360, -1],
             "somewhat negative": [(184, 188, 255), 0, 360, -1],
             "somewhat positive": [(167, 209, 165), 0, 180, 20]}


class KuriBot:
    """Represents a Kuri robot object"""

    def __init__(self, sentiment):
        """Sets up and manages all the variables for a Kuri robot simulation"""
        self.img = cv2.imread("./kuri_resized.jpg")
        self.height, self.width = self.img.shape[0], self.img.shape[1]
        self.sentiment = sentiment

        # Variables for heart
        self.color = SENTIMENT[self.sentiment][0]
        self.size = 50
        self.grow = True

        # Variables for eyes
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
        """Sets the sentiment of the Kuri robot to the given sentiment"""
        self.sentiment = sentiment
        self.color = SENTIMENT[self.sentiment][0]

    def drawEyes(self):
        """Draws the eyes of the Kuri robot"""
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

    def drawHeart(self):
        """Draws the circles that represent the Kuri robot's glowing heart light"""
        cv2.circle(self.img, (self.width // 2, self.height - 100), self.size, self.color, -1)
        cv2.imshow("KuriBot", self.img)
        cv2.circle(self.img, (self.width // 2, self.height - 100), self.size, (248, 248, 248), -1)

        # Continuously changes the radius of the heart light
        if self.grow:
            self.size += 1
        else:
            self.size -= 1
        if self.size >= 70:
            self.grow = False
        if self.size <= 50:
            self.grow = True

    def runKuri(self):
        """Starts the Kuri robot simulation"""
        self.drawEyes()
        self.drawHeart()
        cv2.waitKey(100)


# Implements threading to run the Kuri robot simultaneously with the user input loop
if __name__ == "__main__":
    kuri = KuriBot("neutral")

    fd = sys.stdin.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    while True:
        kuri.runKuri()
        try:
            sentiment = sys.stdin.readline()
            sentiment = sentiment.strip()
            if sentiment == 'q':
                cv2.destroyAllWindows()
                break
            if sentiment in SENTIMENT:
                kuri.setSentiment(sentiment)
        except:
            pass
