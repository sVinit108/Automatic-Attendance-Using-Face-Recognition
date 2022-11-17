import cv2
import pandas as pd
from PIL import Image

df = pd.read_csv('Attendance.csv',index_col='Index')
mail_csv = pd.read_csv('Mail_csv.csv',index_col='Index')
name='Vinit'
print(mail_csv.loc[name])

name = input('Enter your name: ')
mail = input('Enter your parents Email ID: ')
iis = int(input('IIS Attendance: '))
tcs = int(input('TCS Attendance: '))
mp = int(input('MP Attendance: '))

df.loc[len(mail_csv.index)] = [name,mail]
df.loc[len(df.index)] = [name,iis,tcs,mp]
df.to_csv('Attendance.csv')

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img = Image.fromarray(frame)
    img.convert('RGB')
    img.save(f'Images\{name}.jpg')
    cv2.imshow('Face Cropper',frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

print('Name added sucessfully')