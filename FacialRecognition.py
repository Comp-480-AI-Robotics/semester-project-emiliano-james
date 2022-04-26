import glob
import cv2 
import numpy as np
from imutils import paths #imutils includes opencv functions
import face_recognition
import pickle
import cv2
import os

class FacialRecognizer: 
      def __init__(self):
            self.cap = cv2.VideoCapture(0)
            self.faceCascade = cv2.CascadeClassifier('haarscascade/haarcascade_frontalface_default.xml')
            self.name = ''


#    def cameraCapture(self):
#       while True:
#             # Capture frame-by-frame
#             ret, frames = self.cap.read()
#             gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

#             faces = self.faceCascade.detectMultiScale(gray, 1.3, 4)
#             # Draw a rectangle around the faces
#             for (x, y, w, h) in faces:
#                   cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             # Display the resulting frame
#             cv2.imshow('Webcam', frames)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                   break
#             break 

#       # When everything is done, release the capture
#       self.cap.release()
#       cv2.destroyAllWindows()  

      # TODO: (1) ask if first time user --> record face for data training or if face not found in the database
      # (2) If not, then recognize face 

      faces_encodings = []
      faces_names = []
      cur_direc = os.getcwd()
      print(cur_direc)
      path = os.path.join(cur_direc, 'faces/')
      list_of_files = [f for f in glob.glob(path+'*.jpg')]
      number_files = len(list_of_files)
      names = list_of_files.copy()

      for i in range(number_files):
            globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
            globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
            faces_encodings.append(globals()['image_encoding_{}'.format(i)])
            # Create array of known names
            names[i] = names[i].replace(cur_direc, "")  
            faces_names.append(names[i])

      face_locations = []
      face_encodings = []
      face_names = []
      process_this_frame = True

      video_capture = cv2.VideoCapture(0)
   
      while True:
            ret, frame = video_capture.read()    
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)    
            rgb_small_frame = small_frame[:, :, ::-1]    
            if process_this_frame:
                  face_locations = face_recognition.face_locations(rgb_small_frame)
                  face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)        
                  face_names = []
                  for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces (faces_encodings, face_encoding)
                        name = "Unknown"            
                        face_distances = face_recognition.face_distance(faces_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                              name = faces_names[best_match_index]            
                              face_names.append(name)
                              process_this_frame = not process_this_frame
                              # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                  top *= 4
                  right *= 4
                  bottom *= 4
                  left *= 4
                  # Draw a rectangle around the face
                  cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                  # Input text label with a name below the face
                  cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                  font = cv2.FONT_HERSHEY_DUPLEX
                  cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                  # Display the resulting image
            cv2.imshow('Video', frame)
            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                  break


      
