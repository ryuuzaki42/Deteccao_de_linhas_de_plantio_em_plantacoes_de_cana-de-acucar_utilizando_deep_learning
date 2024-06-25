
import cv2
import numpy as np

def imgEqual(im1, im2):
    # 1) Check if 2 images are equals
    if False:
        if im1.shape == im2.shape:
            # print("The images have same size and channels")
            difference = cv2.subtract(im1, im2)
            b, g, r = cv2.split(difference)

            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                print("The images are completely Equal")
                pass

            else:
                print("A - The images are different")
                input()

    if np.array_equal(im1, im2):
        print("The images are Equal")
    else:
        print("B - The images are not Equal")

    sizeX, sizeY, sizeZ = im1.shape
    for i in range(0, sizeX):
        for j in range(0, sizeY):
            for k in range(0, sizeZ):
                if im1[i,j,k] !=  im2[i,j, k]:
                    print("C - The images are not Equal")
                    print(i, j, k)
                    print(im1[i,j,k], im2[i,j, k])
                    input()


im1 =  im = cv2.imread("A_0001a.png")
im2 =  im = cv2.imread("A_0001b.png")

imgEqual(im1, im2)

## Teste in folder
import glob

folder1="/run/media/j/tmp_ntfs/0_t_mest_bkp/tests/Segmentacao Linha Plantio CNN/Recortes/"
folder2="/run/media/j/tmp_ntfs/0_t_mest_bkp/recorte/"

# All files and directories ending with .png and that don't begin with a dot:
fileList = glob.glob(folder1 + "Base_A/*.png")

print(fileList)

for file in fileList:
    print("file:", file)

    im1 =  im = cv2.imread(folder1 + file)
    im2 =  im = cv2.imread(folder2 + file)

    imgEqual(im1, im2)
