
import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread("new/sugarcane1_0027.png")

#im = cv2.imread("new/sugarcane1-GT_0002.png")

x, y, z = im.shape

#np.max(im)

#print(im)

im2 = im.copy()

for i in range (0, x):
    for j in range (0, y):
        if (im[i,j,0] == 0 and im[i,j,1] == 0 and im[i,j,2] == 0):
            im2[i,j] = [255,255,255]

plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.show()

countValues = x * y * z
countZeros = np.count_nonzero(im==0)
maxValue = np.max(im)

print("Total of values: ", countValues)
print("Count of zeros: ", countZeros)
print("Percentage of zeros: ", countZeros/countValues)
print("Max value: ", maxValue)

for i in range (0, maxValue + 1):
    print("Count of", i, ":", np.count_nonzero(im==i))

print(im)
