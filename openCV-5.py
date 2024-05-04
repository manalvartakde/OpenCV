####################### [10] Processing MouseClicks ##################

import cv2
evt = 0
def mouseClick(event,xpos,ypos,flags,params):
    global evt 
    print(xpos,ypos)
    global pnt 
    pnt = (xpos, ypos)
    if (event == cv2.EVENT_LBUTTONDOWN):
        print("Mouse button was at: ", event)
        print(xpos, ypos)
        evt = event
    if(event == cv2.EVENT_RBUTTONDOWN):
        print("Mouse button was at: ", event)
        print(xpos, ypos)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width = 640
height = 360
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 60)
# for Codec
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cv2.namedWindow("My cam")
cv2.setMouseCallback("My cam", mouseClick)

while True:
    ignore, frame = cam.read()

    if(evt == 1):
        cv2.circle(frame,pnt,20,(0,0,255))

    cv2.imshow("My cam", frame)
    if cv2.waitKey(1) == ord("s"):
        break
cam.release()