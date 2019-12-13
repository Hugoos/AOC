import cv2
import numpy as np
import glob
import os
 
img_array = []
for filename in sorted(glob.glob('C:/Source/husp/Misc/2019/Day13Images/*.png'), key=os.path.getmtime):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('breakoutIntmachine.avi',cv2.VideoWriter_fourcc(*"XVID"), 30, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
