cd 'E:\Backes\Segmentacao Linha Plantio CNN\'
numberImg = "0001"
numberImg = "0611"


a_mask = imread("E:\Backes\Segmentacao Linha Plantio CNN\Recortes\Base_A_mask\A_" + numberImg + ".png")
a_mask = im2double(a_mask)
a_mask = double(a_mask > 0.5)

a_pr = imread("E:\Backes\Segmentacao Linha Plantio CNN\Teste_01E\result-images\A_" + numberImg + ".png")
%a_pr = imread("E:\Backes\Segmentacao Linha Plantio CNN\Resultados\Teste_01A\result-images\A_" + numberImg + ".png")
a_pr = im2double(a_pr)
a_pr = double(a_pr > 0.5)

coeficienteDice(a_mask, a_pr)