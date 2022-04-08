import cv2
import numpy as np
import face_recognition

imgstudent=face_recognition.load_image_file('student/Hermione_Granger.jpg')
imgstudent=cv2.cvtColor(imgstudent,cv2.COLOR_BGR2RGB)
imgtest=face_recognition.load_image_file('student test/image.jpg')
imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)
print()
# finding the faces in the image
faceloc=face_recognition.face_locations(imgstudent)[0]
faceenc=face_recognition.face_encodings(imgstudent)[0]
cv2.rectangle(imgstudent,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
faceloc_test=face_recognition.face_locations(imgtest)[0]
faceenc_test=face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceloc_test[3],faceloc_test[0]),(faceloc_test[1],faceloc_test[2]),(255,0,255),2)

#comparing the images
results = face_recognition.compare_faces([faceenc],faceenc_test)
faceDis=face_recognition.face_distance([faceenc],faceenc_test)
print(results,faceDis)

cv2.imshow('Hermione Granger',imgstudent)
cv2.imshow('test',imgtest)
cv2.waitKey(0)

