import cv2
from matplotlib import pyplot as plt

import sys

print ("Number of arguments:", len(sys.argv), "arguments.")
print ("Argument List:", str(sys.argv))

# Create bin
# Advanced > --hidden-import > and add PIL._tkinter_finder
#pyinstaller --noconfirm --onefile --console --hidden-import "PIL._tkinter_finder"  "/media/sda2/home/j/Downloads/0del/00/show_img.py"

print("sys.argv:", sys.argv)
#img_name="/media/sda2/home/j/Dropbox_maestral/ufu/projeto/dissertacao/img/cana_estagios.jpg"

if len(sys.argv) < 2:
    print("Error: need file name")
    raise Exception("Error: need file name")
else:
    img_name = sys.argv[1]

def showImage(img_name):
    img = cv2.imread(img_name)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

def main():
    showImage(img_name)

if __name__ == "__main__":
    main()
