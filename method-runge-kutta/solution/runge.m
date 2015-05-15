% Differencial equations
function Dy = runge(t, y)
Dy = zeros(3, 1);
Dy(1) = -5*y(1) + 0.03*y(2) + 2*y(3);
Dy(2) = -800*y(2);
Dy(3) = -y(1) - 0.005*y(2) - 2*y(3);
