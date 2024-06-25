#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

import os
print("Current working directory: {0}".format(os.getcwd()))

imgFolder="/run/media/j/tmp_ntfs/0_t_mest_bkp/tests/dados_linha/dados_linha/Treinamento 2018-11-09/"
os.chdir(imgFolder)

imgWork = "A" #A
#imgWork = "B"
#imgWork = "C"
#imgWork = "D"

if imgWork == "A" :
    imgName="corte_2152.tif"
    imgNameSave="datasetA_thumbnail.png"

elif imgWork == "B" :
    imgName="corte_2388.tif"
    imgNameSave="datasetB_thumbnail.png"

elif imgWork == "C" :
    imgName="corte_2360.tif"
    imgNameSave="datasetC_thumbnail.png"

elif imgWork == "D" :
    imgName="corte_2255.tif"
    imgNameSave="datasetD_thumbnail.png"

## DecompressionBombError: Image size (600047415 pixels) exceeds limit
## of 178956970 pixels, could be decompression bomb DOS attack.

#Image.MAX_IMAGE_PIXELS = None
#print(MAX_IMAGE_PIXELS)

sizeThumbnail = (800, 800)

image = Image.open(imgName)
print(image.size)

##xx = int(image.size[0]/20)
##yy = int(image.size[1]/20)
##print(xx, yy)
##sizeThumbnail = (xx, yy)

#image.thumbnail((800, 800))
image.thumbnail(sizeThumbnail, Image.ANTIALIAS)

image.save(imgNameSave)

print(image.size) # Output: (605, 800)
