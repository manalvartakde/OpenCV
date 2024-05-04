import cv2
#print(cv2.__version__)
cam = cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    frame_bnw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    ROI = frame[150:300,300:550]
    ROI = cv2.cvtColor(ROI,cv2.COLOR_BGR2GRAY)
    ROI = cv2.cvtColor(ROI,cv2.COLOR_GRAY2BGR)
    frame[100:250,100:350] = ROI

    cv2.imshow("ROI", ROI)
    cv2.imshow('My WEBcam', frame)
    cv2.imshow("bnw", frame_bnw)
    cv2.moveWindow('My WEBcam', 500,200)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
cam.release()