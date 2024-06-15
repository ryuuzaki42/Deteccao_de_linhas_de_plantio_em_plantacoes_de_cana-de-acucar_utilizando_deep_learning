import numpy as np
import cv2
from matplotlib import pyplot as plt

import sys

if len(sys.argv) < 2:
    print("Error: need file name")
    raise Exception("Error: need file name")
else:
    img_name = sys.argv[1]

def showImage(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

def showMultipleImageGrid(imgsArray, titlesArray, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showImageGrid(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y)
        fig.suptitle(titlesArray)
        yId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId].imshow(imgMPLIB)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[xId].imshow(imgMPLIB)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId, xId].set_title(titlesArray[titleId])
            axis[yId, xId].imshow(imgMPLIB)
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1

        fig.tight_layout(pad=0.5)
    plt.show()

def plotSingleImage(imgOriginal):
    # Criando grid com a imagem original apenas
    showImageGrid(imgOriginal, "Img")

def plotTwoImageVertical(imgOriginal):
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 200, 100, 50, 10, cv2.BORDER_REPLICATE)

    # Criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicada'
    showMultipleImageGrid(imgsArray, title, 1, 2)

def plotTwoImageHorizontal(imgOriginal):
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)

    # Criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicada'
    showMultipleImageGrid(imgsArray, title, 2, 1)

def plotThreeImages(imgOriginal):
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgTransparent = np.ones((imgOriginal.shape[0], imgOriginal.shape[1], 4), np.uint8) * 255

    # Criando grid com 3 imagens, a segunda com borda replicada e a terceira com borda de espelho
    # a última imagem é transparente
    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgTransparent]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', '']
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)

def plotFourImages(imgOriginal):
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgReflect101 = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)

    # Criando grid com 4 imagens, a segunda com borda replicada e a terceira e quarta com borda de espelho
    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgReflect101]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 2']
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)

def plotSixImages(imgOriginal):
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgReflect101 = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)
    imgWrap = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_WRAP)

    BLUE = [255, 0, 0]
    imgConstant = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value = BLUE)

    # Criando grid com 6 imagens, a segunda com borda replicada e a terceira e quarta com borda de espelho
    # Constant insere uma moldura e wrap só olhando pra entender =)
    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgReflect101, imgConstant, imgWrap]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 2', 'Moldura', 'Efeito Wrap']
    showMultipleImageGrid(imgsArray, titlesArray, 3, 2)

def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def main():
    imgOriginal = cv2.imread(img_name)

    showImage(imgOriginal)

    plotSingleImage(imgOriginal)

    plotTwoImageVertical(imgOriginal)
    plotTwoImageHorizontal(imgOriginal)

    plotThreeImages(imgOriginal)

    plotFourImages(imgOriginal)

    plotSixImages(imgOriginal)

if __name__ == "__main__":
    main()
