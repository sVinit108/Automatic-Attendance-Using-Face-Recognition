import cv2
import numpy as np
import face_recognition
import os
import pandas as pd
from Encodings import findEncodings
#from Automail import automail_generator

csv = pd.read_csv('Attendance.csv',index_col='Index')

path = 'Images'
imgs = []
Names = []
List = os.listdir(path)
for pics in List:
    temp_img = cv2.imread(f'{path}/{pics}')
    imgs.append(temp_img)
    Names.append(os.path.splitext(pics)[0])

print(Names)

def markAttendance(attendance_list,subject):
    for name in attendance_list:
        csv.loc[(csv.Student_name==name),[subject]]= csv.loc[(csv.Student_name==name),[subject]]+1
        csv.to_csv('Attendance.csv')
        print('Attendance updated\n')
        print(csv)

encodeListKnown = findEncodings(imgs)

cap = cv2.VideoCapture(0)

attendance_list=[]
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceLocation = face_recognition.face_locations(imgS)
    faceEncoding = face_recognition.face_encodings(imgS, faceLocation)

    for encodeFace, faceLoc in zip(faceEncoding, faceLocation):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = Names[matchIndex]
            if name not in attendance_list:
                attendance_list.append(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1+10, y1+10), (x2+10, y2+10), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Webcam', img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

print(attendance_list)

Subject = input('Attendance for which subject?: ')
markAttendance(attendance_list,Subject.upper())

# absentee = [i for i in attendance_list not in Names]
# automail_generator(absentee)