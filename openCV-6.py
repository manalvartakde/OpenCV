
####################### [10] Processing MouseClicks ##################
########################### HW ###########################
import cv2  
(evt,xp1,xp2,yp1,yp2) = (0,1,50,1,50)
def click(event,xpos,ypos,a,b):
    global evt
    global xp1
    global yp1
    global xp2
    global yp2
    
    if (event == 1):
        xp1 = xpos
        yp1 = ypos 
        evt = event
        
    if (event == 4):
        xp2 = xpos
        yp2 = ypos
        evt = event

cam =cv2.VideoCapture(0)
width = 600
height = 400
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cv2.namedWindow("My_Cam")
cv2.setMouseCallback("My_Cam", click)
while True:
    ignore , frame = cam.read()
    if(evt == 4):
        ROI = frame[yp1:yp2, xp1:xp2]
        cv2.imshow("ROI", ROI)
        cv2.moveWindow("ROI", 800,200)
    cv2.rectangle(frame, (xp1,yp1),(xp2,yp2), (255,255,255), 1)
    cv2.imshow("My_Cam", frame)
    if(cv2.waitKey(1) == ord("s")):
        break
cam.release()