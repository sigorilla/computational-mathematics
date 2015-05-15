function nwt = newton(k,e,F,dF)

for i = 1:1000000 
	Z = k - dF^(-1)*F(k);
	norma = sqrt((k(1)-Z(1))^2+(k(2)-Z(2))^2+(k(3)-Z(3))^2);

	if norma > e
        k = Z;
    else
        break;
end

end

%disp('Количество итераций'); disp(i);
nwt = Z;
