import cv2
cam = cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    cv2.imshow("my cam", frame)
    cv2.moveWindow("my cam", 0,0)
    #cv2.waitKey(100)
    cv2.imshow("my cam 2", frame)
    cv2.moveWindow("my cam 2", 700,0)
    #cv2.waitKey(150)
    cv2.imshow("my cam 3", frame)
    cv2.moveWindow("my cam 3",0,400)
    #cv2.waitKey(200)
    cv2.imshow("my cam 4", frame)
    cv2.moveWindow("my cam 4", 700,400)
    #cv2.waitKey(250)
    if cv2.waitKey(1) == ord("s"):
        break
cv2.release()