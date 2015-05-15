% before run you should import data
step = 0.01;
lengthX = 1;
lengthY = 1;
[X, Y] = meshgrid(step:step:lengthX, step:step:lengthY);
figure(1), surf(X, Y, data), grid on;
title('Poisson Equation Solution');
xlabel('X');
ylabel('Y');
zlabel('Temperature');
