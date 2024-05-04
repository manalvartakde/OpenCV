######################### [16] FACE Recognition using open CV ##############

import cv2
import face_recognition as fr

image = cv2.imread(r"C:/Users/manal/Documents/Python/Demo_images/known/Donald Trump.jpg")
font = cv2.FONT_HERSHEY_SIMPLEX

don_face = fr.load_image_file(r"C:/Users/manal/Documents/Python/Demo_images/known/Donald Trump.jpg")
face_loc = fr.face_locations(don_face)

don_face = cv2.cvtColor(don_face, cv2.COLOR_RGB2BGR)

print(face_loc)
newimg = cv2.rectangle(don_face,(face_loc[0][0],face_loc[0][1]), (face_loc[0][2], face_loc[0][3]), (0,255,0), 3)
while(1):
    cv2.imshow("don", don_face)
    if(cv2.waitKey(1) == ord("s")):
        break
