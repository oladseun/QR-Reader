import cv2
import numpy as np
from pyzbar.pyzbar import decoder


#img = cv2.imread('.png')
cap.set(3,640)
cap.set(4,480)
cp = cv2.VideoCapture(0)

with open('myDatafile.txt') as f:
    myDataList = f.read.splitlines()
    
print(myDataList)

while True:
    success, img = cap.read()

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        
        if myData in myDataList:
            MyOutput = 'Authorised'
            MyColor = (0,255,0)
            
            else:
                MyOutput = 'Unauthorised'
                MyColor = (0,0,255)
                
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts], True, (55,0,255), 5)
        pts2 = barcode.rect
        cv2.putText(img, MyOutput,(pts2[0], pts2[1]), cv2.FONT,
                    0.9,MyColor,2)
    
    cv2.imshow('Result', img)
    cv2.waitKey(1)
    
    