import cv2 




class FacialRecognizer: 
     def __init__(self):
        self.camera = cv2.videoCapture(0) 
