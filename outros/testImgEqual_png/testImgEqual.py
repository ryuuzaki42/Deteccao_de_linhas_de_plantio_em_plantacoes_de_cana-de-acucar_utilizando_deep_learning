
from PIL import Image

def my_function(im1, im2):
    # 1) Check if 2 images are equals
    if original.shape == duplicate.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")

im1 = Image.open("A_0001a.png")
im2 = Image.open("A_0001b.png")

pix1 = im1.load()
pix2 = im2.load()

cont = 0
for i in range(0, 256):
    for j in range(0, 256):
        if pix1[i,j] !=  pix2[i,j]:
            print(i,j)
            cont = 42
        #else:
        #    print("A")

im1 = im1.save("a.png")
im2 = im2.save("b.png")

print(cont)
