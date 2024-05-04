import cv2
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width = 640
height = 360
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 60)
# for Codec
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
while True:
    ignore, frame = cam.read()
    cv2.imshow("My cam", frame)
    if cv2.waitKey(1) == ord("s"):
        break
cam.release()