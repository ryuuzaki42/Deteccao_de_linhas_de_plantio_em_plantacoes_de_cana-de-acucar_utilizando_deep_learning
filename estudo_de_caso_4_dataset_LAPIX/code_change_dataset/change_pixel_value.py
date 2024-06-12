#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:43:45 2022

@author: j
"""

import cv2
import matplotlib.pyplot as plt

imageToLoad = "sugarcane1-GT.png"
imageToSave = "sugarcane1-GT_new.png"

imageName = imageToLoad.split(".")[0]
im = cv2.imread(imageToLoad)

plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.show()

MaxX, MaxY, MaxZ = im.shape
print("Image shape", MaxX, MaxY, MaxZ)

red = [0, 0, 255] # img BGR
green = [0, 255, 0]
white = [255, 255, 255]
black = [0, 0, 0]

for i in range(0, MaxX):
    print(i, end = " ")
    for n in range(0, MaxY):
        val = im[i, n]
        #print("i", i, "n", n, " val", val)

        if (val == red).all():
            #print("red", val)
            im[i, n] = black
            
        elif (val == green).all():
            #print("green", val)
            im[i, n] = white

plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.show()

cv2.imwrite(imageToSave, im)
