
##################### [11] Creating Trackbars ##########################

import cv2

(xpos,ypos) = (0,0)
def track1(val):
    global xpos
    xpos = val
    print(val)

def track2(val):
    global ypos
    ypos = val
    print(val)

def track3(val):
    global rad
    rad = val
    print(val)

def track4(val):
    global thk
    thk = val
    print(val)

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("Mytrackbar-1")
cv2.resizeWindow("Mytrackbar-1",400,200)
cv2.moveWindow("Mytrackbar-1",1080,500)
cv2.createTrackbar("xpos","Mytrackbar-1",860,1920,track1)
cv2.createTrackbar("ypos","Mytrackbar-1",540,1080,track2)
cv2.createTrackbar("Radius","Mytrackbar-1",5,50,track3)
cv2.createTrackbar("Thickness","Mytrackbar-1",1,10,track4)

while True:
    ignore,  frame = cam.read()
    if (thk == 0):
        thk = -1
    cv2.circle(frame,(xpos,ypos),rad,(255,255,0),thk)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('s'):
        break
cam.release()