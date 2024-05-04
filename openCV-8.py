
########################### [12] HSV COLOUR SPACE (finding value of pixel colour) #######################

import cv2
import numpy as np
evt = 0
def click(event, xpos, ypos, *a):
    global evt
    global xval
    global yval
    if(event == 1):
        evt = event
        xval = xpos
        yval = ypos

        

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("my WEBcam")
cv2.setMouseCallback("my WEBcam", click)

while True:
    ignore,  frame = cam.read()

    if(evt == 1):
        a = np.zeros([250,250,3],dtype = np.uint8)
        b = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        print(b)
        clr = frame[yval][xval]
        clr_hsv = b[yval][xval]
        print(clr)
        print(clr_hsv)
        a[:,:] = clr
        clr_hsv = str(clr_hsv)
        cv2.putText(a, clr_hsv, (0,20), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),1)
        cv2.imshow("Colour", a)
        evt = 0    

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('s'):
        break
cam.release()