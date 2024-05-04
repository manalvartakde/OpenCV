######################### [15] FACE DETECTION [HW] ##################
# Detecting eyes

import cv2

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

FaceCascade = cv2.CascadeClassifier("haar\haarcascade_frontalface_default.xml")
EyesCascade = cv2.CascadeClassifier("haar\haarcascade_eye.xml")
(x,y,w,h) = (0,0,0,0)
(xe,ye,we,he) = (0,0,0,0)
while True:
    ignore,  frame = cam.read()
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = FaceCascade.detectMultiScale(frame1, 1.3, 5)

    newframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(faces)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0), 2)
        # a = x//25
        # b = y//5
        # c = x//25
        # d = 2 * y//5

        # cv2.rectangle(frame,(x + a, y + b), (x + w - c, y + h - d), (0,0,255), 2)

    newframeROI = newframe[y:y+h, x:x+h]

    eyes = EyesCascade.detectMultiScale(newframeROI, 1.3, 5)

    for eye in eyes:
        xe,ye,we,he = eye
        cv2.rectangle(frame[y:y+h, x:x+h],(xe,ye),(xe+we, ye+he),(0,0,255), 2)

    # cv2.imshow('my WEBcam', newframeROI)
  
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
cam.release()