import glob
import cv2 
import numpy as np
from imutils import paths #imutils includes opencv functions
import face_recognition
import pickle
import cv2
import os
import time	
from turtle import *

class FacialRecognizer: 
      def __init__(self):
            self.cap = cv2.VideoCapture(0)
            self.faceCascade = cv2.CascadeClassifier('haarscascade/haarcascade_frontalface_default.xml')
            self.name = ''

      def learnFaces(self):

            faces_encodings = []
            faces_names = []
            cur_direc = os.getcwd()
            path = os.path.join(cur_direc, 'faces/')
            # iterate through a list of files and grab any with the extension .jpg
            list_of_files = [f for f in glob.glob(path+'*.jpg')]
            number_files = len(list_of_files)
            # as long as the file name ends in .jpg it will grab the begininning part and use it as the name 
            names = list_of_files.copy()

            for i in range(number_files):

                  globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
                  globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
                  faces_encodings.append(globals()['image_encoding_{}'.format(i)])
                  # Create array of known names
                  names[i] = names[i].replace(cur_direc, "")  
                  faces_names.append(names[i])

            return faces_encodings, faces_names

      def recognizeFace(self):

            face_locations = []
            face_encodings = []
            face_names = []
            # process_this_frame = True
            recognizing = True

            video_capture = cv2.VideoCapture(0)
      
            while recognizing:
                  ret, frame = video_capture.read()    
                  small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)    
                  rgb_small_frame = small_frame[:, :, ::-1]    
                  # if process_this_frame:
                  # For face recognition, the algorithm notes certain important measurements on the face — 
                  # like the color and size and slant of eyes, the gap between eyebrows, etc. 
                  # All these put together define the face encoding
                  # gathers the positon of frame where the face resides 
                  face_locations = face_recognition.face_locations(rgb_small_frame)
                  # gathers the face encodings for the face 
                  face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)        
                  face_names = []
                  for face_encoding in face_encodings:
                        # compares the known faces and sees if it is already in current filesystem by comparing facial encodings 
                        matches = face_recognition.compare_faces (self.learnFaces()[0], face_encoding)
                        name = "Unknown"            
                        face_distances = face_recognition.face_distance(self.learnFaces()[0], face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                              name = self.learnFaces()[1][best_match_index]            
                              face_names.append(name)
                              # process_this_frame = not process_this_frame
                              recognizing = False
                              cut_string = name.split('.')
                              newName = cut_string[0]
                              return newName
                        else:
                              # print("record")
                              # cv2.imshow('Video', frame)
                              # cv2.waitKey(0)
                              # video_capture.release()
                              # cv2.destroyAllWindows()
                              print("record1")
                              # newName = textinput("Save User", "Enter Your Name")
                              # Screen().bye()
                              newName = self.saveUser()
                              path = os.path.join(os.getcwd(), 'faces/')
                              print("record2")
                              cv2.imwrite(os.path.join(path, newName+".jpg"), frame)  
                              print("record3")     
                              # cv2.waitKey(0)
                              print("record4")
                              # process_this_frame = not process_this_frame
                              # cv2. destroyAllWindows()
                              recognizing = False
                              print("record5")
                              return newName
                              
            video_capture.release()
            cv2. destroyAllWindows()
            
      def saveUser(self):

      #       cv2.imshow('Video', frame)
      #       cv2.waitKey(0)

            sc = Screen()
            sc.setup(400, 300)
            name = textinput("Save User", "Enter Your Name")
            bye()
            print("get here")

            return name


            # Display the results
            # for (top, right, bottom, left), name in zip(face_locations, face_names):
            #       top *= 4
            #       right *= 4
            #       bottom *= 4
            #       left *= 4
            #       # Draw a rectangle around the face
            #       cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            #       # Input text label with a name below the face
            #       cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            #       font = cv2.FONT_HERSHEY_DUPLEX
            #       cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            #       # Display the resulting image
            # cv2.imshow('Video', frame)
            # # t_end = time.time() + 10
            # # if hasFace is True and time.time() == t_end:
            # #       break

                  # if cv2.waitKey(1) & 0xFF == ord('q'):
                  #       break


      
# update the region of t=intrest within the frame in real time 
# im.write to save that image and save to image dir 
# destory window closes just the camera window , gather start time -- while loop - gather current time and when they exceed a certain amoung loop ends 
# whatever we need coccurs in the while loop -- once we are done with data we break out of the loop then we close the window wirth window destroy 
# maybe have sa timestamo with the image so they save to different folders 
