clearvars;
close all;
clc;

letras = 'ABCD';

N = 7683;
nomes_linhas = cell(N,1);

for teste=1:12
    resultados = zeros(N,4);
    cont = 1;
    for le = 1:4
        pasta = ['.\Recortes\Base_',letras(le),'_mask\'];
        arq = dir([pasta,'*.png']);
        Narq = length(arq);
        
        for k = 1:Narq
            nome = arq(k).name;
            nomes_linhas{cont} = nome;
            
%             im_mask = imread([pasta,nome]);
%             im_mask = im2double(im_mask);
%             im_mask = double(im_mask > 0.5);
            
            for base = 1:4
                str = sprintf('Teste_%02d%c',teste,letras(base));
                
                im_res = imread(['.\Resultados\',str,'\result-images\',nome]);
                im_res = im2double(im_res);
                im_res = double(im_res > 0.5);
                
                imwrite(im_res,['.\Resultados\',str,'\result-images\',nome],'png');
                %resultados(cont,base) = coeficienteDice(im_mask,im_res);                
            end 
            cont = cont + 1;
        end
        
    end	
%     str = sprintf('resultados_Teste_%02d.mat',teste);
    %save(str,'resultados','nomes_linhas');
end