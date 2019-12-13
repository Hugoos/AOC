import cv2
import numpy as np
import glob
import os
 
img_array = []
for filename in sorted(glob.glob('C:/Source/husp/Misc/2019/Day13Images/*.png'), key=os.path.getmtime):
    img = cv2.imread(filename)
    #height, width, layers = img.shape
    dim = (420,210)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    img_array.append(resized)
 
#print(size)
#out = cv2.VideoWriter('breakoutIntmachine.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, dim)
out = cv2.VideoWriter('breakoutIntmachine.avi',cv2.VideoWriter_fourcc(*"xvid"), 30, dim)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
