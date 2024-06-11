
import cv2
import numpy as np
import matplotlib.pyplot as plt

# cd /media/sda2/home/j/Downloads/0del/lapix/

# ----------------------------------------- #

# mkdir -p img/black img/new img/percentage img/small
# mkdir -p mask/black mask/new mask/percentage mask/small

# rm */black/* */new/* */percentage/* */small/*

# ----------------------------------------- #

image_load = "sugarcane1.png"
#mask_load = "sugarcane1-GT.png"
mask_load = "sugarcane1-GT_new.png"

#image_load = "sugarcane2.png"
#mask_load = "sugarcane2-GT.png"

#image_load = "corte_2152.tif"
#mask_load

size_x = 256
size_y = 256

percentage_save = 80.0 # 80% of valid values, different of zero

# ----------------------------------------- #

image_name = image_load.split(".")[0]

img = cv2.imread(image_load)
mask = cv2.imread(mask_load)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.show()

max_x, max_y, max_z = img.shape
print("Image shape", max_x, max_y, max_z)

cont = 1
max_percentage_zero = 100.0 - percentage_save
test = 1
count_values = size_x * size_y * max_z

img_path_add = "img"
mask_path_add = "mask"

for i in range(0, max_x, size_x):
    for n in range(0, max_y, size_y):
        img_tmp = img[i:i+size_x, n:n+size_y].copy()
        mask_tmp = mask[i:i+size_x, n:n+size_y].copy()

        ## test if getting values correct in image space
        #limite_x = i + size_x
        #limite_y = n + size_y
        #if (limite_x > max_x):
            #limite_x = max_x
        #if (limite_y > max_y):
            #limite_y = max_y

        #for a in range (i, limite_x):
            #for b in range (n, limite_y):
                #im[a, b] = [255, 255, 255]

        #if (test == 10 ):
            #test = 1
            #plt.imshow(cv2.cvtColor(img_tmp, cv2.COLOR_BGR2RGB))
            #plt.show()
        #else:
            #test = test + 1

        print(f"{cont} img[ {i} : {i + size_x}, {n} : {n+size_y}]")


        if (cont < 10):
            add = "000"
        elif (cont < 100):
            add = "00"
        elif (cont < 1000):
            add = "0"
        else:
            add = ""

        name = "_" + add + str(cont) + ".png"

        tmpX, tmpY, _ = img_tmp.shape

        if (tmpX < size_x) or (tmpY < size_y):
            print("small")
            cv2.imwrite(img_path_add + "/small/" + image_name + name, img_tmp)
            cv2.imwrite(mask_path_add + "/small/" + image_name + name, mask_tmp)
        else:
            max_pixel_value = np.max(img_tmp)

            if (max_pixel_value == 0):
                print("black")
                cv2.imwrite(img_path_add + "/black/" + image_name + name, img_tmp)
                cv2.imwrite(mask_path_add + "/black/" + image_name + name, mask_tmp)
            else:
                count_zero = np.count_nonzero(img_tmp == 0)
                percentage_zero = count_zero/count_values * 100
   
                print("Total of values: ", count_values)
                print("Count of zeros: ", count_zero)
                print("Percentage of zeros: ", percentage_zero)
                #print("maxPixelValue: ", max_pixel_value)

                if (percentage_zero > max_percentage_zero):
                    print("percentage")
                    cv2.imwrite(img_path_add + "/percentage/" + image_name + name, img_tmp)
                    cv2.imwrite(mask_path_add + "/percentage/" + image_name + name, mask_tmp)
                else:
                    print("new")
                    cv2.imwrite(img_path_add + "/new/" + image_name + name, img_tmp)
                    cv2.imwrite(mask_path_add + "/new/" + image_name + name, mask_tmp)

        cont = cont + 1
