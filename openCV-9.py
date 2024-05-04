
######################### [13] OBJECT tRACKING USING HSV #########################

import cv2
import numpy as np
def fn1(val):
    global huelow
    huelow = val
    
def fn2(val):
    global huehigh
    huehigh = val

def fn3(val):
    global satlow
    satlow = val

def fn4(val):
    global sathigh
    sathigh = val

def fn5(val):
    global vallow
    vallow = val

def fn6(val):
    global valhigh
    valhigh = val    

width = 800
height = 600
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("MyTracker")
cv2.createTrackbar("Hue_low","MyTracker", 0,180,fn1)
cv2.createTrackbar("Hue_high","MyTracker", 0,180,fn2)
cv2.createTrackbar("sat_low","MyTracker", 0,255,fn3)
cv2.createTrackbar("sat_high","MyTracker", 0,255,fn4)
cv2.createTrackbar("val_low","MyTracker", 0,255,fn5)
cv2.createTrackbar("val_high","MyTracker", 0,255,fn6)
huelow, huehigh, satlow, sathigh, vallow, valhigh = 0,0,0,0,0,0
while True:
    ignore,  frame = cam.read()
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowbound = np.array([huelow,satlow,vallow])
    highbound = np.array([huehigh,sathigh,valhigh])
    mymask = cv2.inRange(frameHSV,lowbound,highbound)
    mymask = cv2.bitwise_and(frame,frame,mask = mymask)
    mymask = cv2.resize(mymask,(600,450))
    cv2.imshow("Mask", mymask)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('s'):
        break
cam.release()