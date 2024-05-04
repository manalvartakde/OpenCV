import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    #grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    cv2.rectangle(frame,(250,50),(500,400),(200,255,0),3)
    cv2.putText(frame, "Hello",(50,400),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),3)
    cv2.imshow('My WEBcam', frame)
    cv2.moveWindow('My WEBcam', 500,200)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
cam.release()