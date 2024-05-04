
########################### [12] HSV COLOUR SPACE (finding value of pixel colour) #######################

########################## HW ################################

import cv2
import numpy as np

a = np.zeros([255,180,3],dtype = np.uint8)
b = np.zeros([255,180,3],dtype = np.uint8)
for i in range(180):
    for j in range(255):
        a[j][i][1] = j
        a[j][i][2] = 200
for j in range(255):
    for i in range(180):
        a[j][i][0] = i
        a[j][i][2] = 200

for i in range(255):
    for j in range(180):
        b[i,j] = (j,150,i)


a = cv2.cvtColor(a,cv2.COLOR_HSV2BGR)
b = cv2.cvtColor(b,cv2.COLOR_HSV2BGR)

while True:
    cv2.imshow("My Frame",a)
    cv2.imshow("My Frame1",b)
    if cv2.waitKey(1) & 0xff ==ord('s'):
        break
