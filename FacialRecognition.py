import cv2 
import numpy as np

class FacialRecognizer: 
   def __init__(self):
      self.cap = cv2.VideoCapture(0)
      self.faceCascade = cv2.CascadeClassifier('haarscascade/haarcascade_frontalface_default.xml')


   def cameraCapture(self):
      while True:
            # Capture frame-by-frame
            ret, frames = self.cap.read()
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(gray, 1.3, 4)
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                  cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Display the resulting frame
            cv2.imshow('Webcam', frames)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                  break
            break 

      # When everything is done, release the capture
      self.cap.release()
      cv2.destroyAllWindows()  


      
