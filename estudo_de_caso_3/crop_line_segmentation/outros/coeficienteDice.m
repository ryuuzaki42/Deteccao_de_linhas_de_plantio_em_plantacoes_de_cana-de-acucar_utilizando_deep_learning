function d = coeficienteDice(A,B)
    inter = A + B;
    
    inter = 2 * length(find(inter == 2));
    
    d = inter / (sum(A(:)) + sum(B(:)));
end
