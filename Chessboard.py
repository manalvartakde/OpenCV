import numpy as np
import cv2


new = np.zeros([880,880,3],dtype = np.uint8)
new[:,:] = [0,0,255]

for i in range(11):
  for j in range(11):
    if ((i%2)==0 and (j%2)==0):
      new[i*80 : (i+1)*80 , j*80 : (j+1)*80] = [255,0,120]
    elif ((i%2)!=0 and (j%2)!=0):
      new[i*80 : (i+1)*80 , j*80 : (j+1)*80] = [255,0,120]

#  # Black borders
for i in range(20):
  new[i*80 : (i*80)+10 , : ] = [0,0,0]
  new[ : , i*80 : (i*80)+10 ] = [0,0,0]
  
while True:
   cv2.imshow("abc", new)
   if cv2.waitKey(1) == ord("s"):
     break
