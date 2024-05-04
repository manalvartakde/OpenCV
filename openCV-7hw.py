
##################### [11] Creating Trackbars using oops  ##########################

########################### HW #############################

import cv2

(xpos,ypos) = (0,0)
class Tracks:

    def track1(self,val):
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, val)

    def track2(self,val):
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT,val)


t = Tracks()

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("Mytrackbar-1")
cv2.resizeWindow("Mytrackbar-1",400,200)
cv2.moveWindow("Mytrackbar-1",1080,500)
cv2.createTrackbar("width","Mytrackbar-1",860,1920,t.track1)
cv2.createTrackbar("height","Mytrackbar-1",540,1080,t.track2)

while True:
    ignore,  frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('s'):
        break
cam.release()