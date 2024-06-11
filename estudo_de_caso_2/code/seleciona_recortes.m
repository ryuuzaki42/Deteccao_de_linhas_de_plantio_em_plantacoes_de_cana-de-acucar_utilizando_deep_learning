clc;
close all;
clearvars;

%%
% letra = 'ABCD';
% tam = [678 3291 1552 2162];
% selecao = [];
% 
% for k=1:4
%     selecao = [selecao; k*ones(500,1), randperm(tam(k),500)'];
% end
% 
% save('selecao.mat','selecao');

%%
load('selecao.mat');
letra = 'ABCD';

C = 1;
for k=1:4
    pasta = sprintf('.\\Base_%c\\',letra(k));
    pastaM = sprintf('.\\Base_%c_mask\\',letra(k));
    arq = dir([pasta,'*.png']);
    
    pasta_dest = '.\Base_E\';
    pasta_destM = '.\Base_E_mask\';
    
    for idx = 1:500
        nome = arq(selecao(C,2)).name;
        
        copyfile([pasta,nome],[pasta_dest,nome]);
        copyfile([pastaM,nome],[pasta_destM,nome]);
        C = C + 1;
    end
end
