
import cv2
import numpy as np
import matplotlib.pyplot as plt

import os

from PIL import Image

# mkdir black new percentage small

# rm black/* new/* percentage/* small/*

# ----------------------------------------- #
#imageToLoad = "sugarcane1.png"
#imageToLoad = "sugarcane1-GT.png"

#imageToLoad = "sugarcane2.png"
#imageToLoad = "sugarcane2-GT.png"

#sizeX = 512
#sizeY = sizeX

#percentageToSave = 0.0 # 1%

# ----------------------------------------- #

#imageToLoad= "corte_2152.tif"

pathImgs="/run/media/j/tmp_ntfs/0_t_mest_bkp/tests/dados_linha/dados_linha/Treinamento 2018-11-09/"

folderName="Base_A" # 678 images
imageToLoad1 = pathImgs + "corte_2152.tif"
imageToLoad2 = pathImgs + "corte_2152_linhas.tif"

#folderName="Base_B" # 3291 images
#imageToLoad1 = pathImgs + "corte_2388.tif"
#imageToLoad2 = pathImgs + "corte_2388_linhas.tif"

#folderName="Base_C" # 1552 images
#imageToLoad1 = pathImgs + "corte_2360.tif"
#imageToLoad2 = pathImgs + "corte_2360_linhas.tif"

#folderName="Base_D" # 2162 images
#imageToLoad1 = pathImgs + "corte_2255.tif"
#imageToLoad2 = pathImgs + "corte_2255_linhas.tif"

sizeX = 256
sizeY = sizeX

percentageToSave = 80.0 # 80%

# ----------------------------------------- #
imageName = os.path.basename(imageToLoad1) # Get file name and extension
imageName = imageName.split(".")[0] # remove extension (after .)
print("imageName:", imageName)

imageStartName = folderName.split("_")[1]
print("imageStartName:", imageStartName)

im = cv2.imread(imageToLoad1)

#plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
#plt.show()

MaxX, MaxY, MaxZ = im.shape
print("Image shape", MaxX, MaxY, MaxZ)

cont = 1
percentageToSave = 100.0 - percentageToSave
test = 1
countValues = sizeX * sizeY * MaxZ

os.mkdir(folderName)
if not os.path.exists("delete"):
    os.mkdir("delete")

os.mkdir("delete/" + folderName + "/")
os.mkdir("delete/" + folderName + "/small/")
os.mkdir("delete/" + folderName + "/black/")
os.mkdir("delete/" + folderName + "/percentage/")

fileSaved = []

imgCont = 1
for i in range(0, MaxX, sizeX):
    for n in range(0, MaxY, sizeY):
        imTmp = im[i:i+sizeX, n:n+sizeY].copy()

        ## test if gettin values correct in image space
        #limiteX = i + sizeX
        #limiteY = n + sizeY
        #if (limiteX > MaxX):
            #limiteX = MaxX
        #if (limiteY > MaxY):
            #limiteY = MaxY

        #for a in range (i, limiteX):
            #for b in range (n, limiteY):
                #im[a, b] = [255, 255, 255]

        #if (test == 10 ):
            #test = 1
            #plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
            #plt.show()
        #else:
            #test = test + 1

        #print("im[",i,":",i,"+",sizeX,", ",n,":",n,"+",sizeY,"]")
        print(cont, " im[",i,":",i+sizeX,", ",n,":",n+sizeY,"]")

        #plt.imshow(cv2.cvtColor(imTmp, cv2.COLOR_BGR2RGB))
        #plt.show()


        if (imgCont < 10):
            add = "000"
        elif (imgCont < 100):
            add = "00"
        elif (imgCont < 1000):
            add = "0"
        else:
            add = ""

        name = "_" + add + str(imgCont) + ".png"

        tmpX, tmpY, _ = imTmp.shape

        if ( tmpX < sizeX or tmpY < sizeY):
            print("small")
            cv2.imwrite("./deletes/" + folderName + "/small/" + imageStartName + name, imTmp)
        else:
            maxPixelValue = np.max(imTmp)

            if (maxPixelValue == 0):
                print("black")
                cv2.imwrite("./deletes/" + folderName + "/black/" + imageStartName + name, imTmp)
            else:
                countZeros = np.count_nonzero(imTmp==0)
                percentageZeros = countZeros/countValues * 100

                print("Total of values: ", countValues)
                print("Count of zeros: ", countZeros)
                print("Percentage of zeros: ", percentageZeros)
                print("maxPixelValue: ", maxPixelValue)

                if (percentageZeros > percentageToSave):
                    print("percentage")

                    cv2.imwrite("./deletes/" + folderName + "/percentage/" + imageStartName + name, imTmp)
                else:
                    print("new")
                    cv2.imwrite("./" + folderName +"/" + imageStartName + name, imTmp, [cv2.IMWRITE_PNG_COMPRESSION, 9])
                    #Image.save("./" + folderName +"/" + imageStartName + name, imTmp)
                    imgCont += 1
                    fileSaved.append(cont)

        cont += 1

        #print("Continue")
        #stepContinue = input()

print(fileSaved)

im = cv2.imread(imageToLoad2, cv2.IMREAD_GRAYSCALE) # GRAYSCALE image

cont = 1
imgCont = 1

os.mkdir(folderName + "_mask")
os.mkdir("delete/" + folderName + "/del_mask/")

for i in range(0, MaxX, sizeX):
    for n in range(0, MaxY, sizeY):
        imTmp = im[i:i+sizeX, n:n+sizeY].copy()

        if (imgCont < 10):
            add = "000"
        elif (imgCont < 100):
            add = "00"
        elif (imgCont < 1000):
            add = "0"
        else:
            add = ""

        name = "_" + add + str(imgCont) + ".png"

        # Checking if image name exists in list
        print("cont:", cont)

        if (cont in fileSaved):
            print(folderName + "_mask")
            cv2.imwrite("./" + folderName + "_mask/" + imageStartName + name, imTmp)
            imgCont += 1
        else:
            print("del_mask")
            cv2.imwrite("./delete/" + folderName + "/del_mask/" + imageStartName + name, imTmp)

        cont += 1
