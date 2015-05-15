clear; clc;
% Initial data
h = 0.0001;
L = 3;
x = 0;
u = [2 4 6];
A = [-5 0.03 2; 0 -800 0; -1 -0.005 -2];
f = @(x, u) A * u';

% Matlab Runge-Kutta
options = odeset('RelTol',1e-4,'AbsTol',[1e-4 1e-4 1e-5]);
[T, Y] = ode45(@runge, [x:h:L], u, options);

% Plot graphics
figure(1);
plot(T,Y(:,1),'b',T,Y(:,2),'r',T,Y(:,3),'g'); grid;
legend('u(t)', 'v(t)', 'w(t)');


% Doublestep method explicit Runge-Kutta
% First iteration
x = x + h;
ui = (u + 3 * h * f(x, u)' / 2);
uii = u;
u = [u; ui];
m = L/h;
% Other iterations
for i=2:m
    u = [u; (ui + h * ( 3*f(x, ui)' - f(x-h, uii)' ) / 2)];
    ui = (ui + h * ( 3*f(x, ui)' - f(x-h, uii)' ) / 2);
    uii = ui;
    x = x + h;
end;

% Plot graphics
figure(2);
X = [0:h:L];
plot(X, u(:,1),'b',X,u(:,2),'r',X,u(:,3),'g'); grid;
legend('u(t)', 'v(t)', 'w(t)');
